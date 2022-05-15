import json
from enum import Enum

import google.protobuf.json_format as js
# import pydantic
from pydantic import BaseModel, ValidationError, Field, root_validator
from typing import List, Dict
from python_server import ReportService

from random import choice

import grpc
import server_pb2_grpc as pb2_grpc
import server_pb2 as pb2


class ReportClient(object):
    class SpaceShip(BaseModel):
        alignment: str
        name: str
        length: float
        vessel_class: str = Field(alias='class')
        size: int
        armed: bool
        officers: List[Dict]

        @root_validator
        def check(cls, values):
            index: int = 0
            for count, value in enumerate(list(ReportService.Spaceship.__Vessel_class__)):
                if value.name == values["vessel_class"]:
                    index = count + 1
                    break
            length_ranges: list[list[int]] = [[], [80, 250], [300, 600], [500, 1000], [800, 2000], [1000, 4000], [5000, 20000]]
            size_ranges: list[list[int]] = [[], [4, 10], [10, 15], [15, 30], [50, 80], [120, 250], [300, 500]]
            armed_ranges: list[bool] = [True, True, True, True, True, False, True]
            hostile_ranges: list[bool] = [True, True, False, True, False, True, True]
            if index != 0:
                if values['length'] not in range(length_ranges[index][0], length_ranges[index][1]):
                    raise ValueError
                if values['size'] not in range(size_ranges[index][0], size_ranges[index][1]):
                    raise ValueError
                if values['armed'] is not armed_ranges[index]:
                    raise ValueError
                if values['alignment'] == 'enemy' and hostile_ranges[index] is False:
                    raise ValueError
            return values

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 6666

    def get_spaceship(self):
        with grpc.insecure_channel('localhost:6666') as channel:
            stub = pb2_grpc.ReportStub(channel)
            main_coordinates: List[int] = [24, 54, 30, 32]
            second_coordinates: List[float] = [24.32, 31.24]
            message = pb2.Coordinates(coordinate1=main_coordinates[0], coordinate2=main_coordinates[1],
                                      coordinate3=second_coordinates[0], coordinate4=main_coordinates[2],
                                      coordinate5=main_coordinates[3], coordinate6=second_coordinates[1])

            response = self.generate_json(js.MessageToJson(stub.GetSpaceship(message)))
            try:
                self.SpaceShip.parse_raw(response)
            except ValidationError as error:
                response = None

        return response

    def generate_json(self, response):
        data = json.loads(response)
        officers = data.get('officers')
        if not data.get('armed'):
            data['armed'] = False
        if officers:
            grouped_officers: List[Dict] = []
            for i in range(0, len(officers), 3):
                grouped_officers.append(
                    {'first_name': officers[i], 'last_name': officers[i + 1], 'rank': officers[i + 2]})
            data['officers'] = grouped_officers
        else:
            data['officers'] = []
        data = json.dumps(data)
        return data


if __name__ == '__main__':
    client = ReportClient()
    for _ in range(choice([1, 10])):
        result = client.get_spaceship()
        if result is not None:
            print(f'{result}')
