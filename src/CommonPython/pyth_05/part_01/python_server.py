from enum import IntEnum
from typing import List, Dict

import grpc
from concurrent import futures
import time
import server_pb2_grpc as pb2_grpc
import server_pb2 as pb2
from random import choice, uniform, randint


class ReportService(pb2_grpc.ReportServicer):

    def __init__(self):
        pass

    class Spaceship:
        class __Vessel_class__(IntEnum):
            Corvette = 1
            Frigate = 2
            Cruiser = 3
            Destroyer = 4
            Carrier = 5
            Dreadnought = 6

        __ranks__: List[str] = ['Commander', 'Lieutenant', 'Warchief', 'Sergeant', 'Chief', 'Captain', 'Colonel', 'Admiral']

        def __init__(self):
            self.alignment: int = choice([1, 2])
            with open('spaceship_names.txt', 'r') as file:
                lines = file.read().splitlines()
                self.name: str = choice(lines)
            self.vessel_class = choice(list(self.__Vessel_class__))
            if self.alignment == 2:
                self.vessel_class = choice([self.vessel_class, 7])

            self.length: float = self.define_length()
            self.size: int = self.define_size()
            self.armed: bool = choice([True, False])
            self.officers: List[str] = []

            with open('known_officers.txt') as file:
                lines = file.read().splitlines()
                for _ in range(randint(0, 4)):
                    self.officers += choice(lines).split(' ')
                    self.officers.append(choice(self.__ranks__))

        def define_length(self) -> float:
            length: int = 0
            if self.vessel_class == 7:
                length = randint(60, 25000)
            if self.vessel_class == self.__Vessel_class__.Corvette:
                length = randint(60, 280)
            if self.vessel_class == self.__Vessel_class__.Frigate:
                length = randint(250, 820)
            if self.vessel_class == self.__Vessel_class__.Cruiser:
                length = randint(75, 500)
            if self.vessel_class == self.__Vessel_class__.Destroyer:
                length = randint(480, 1200)
            if self.vessel_class == self.__Vessel_class__.Carrier:
                length = randint(1000, 4200)
            if self.vessel_class == self.__Vessel_class__.Dreadnought:
                length = randint(7000, 25000)
            return float(length)

        def define_size(self) -> int:
            size: int = 0
            if self.vessel_class == 7:
                size = randint(3, 570)
            if self.vessel_class == self.__Vessel_class__.Corvette:
                size = randint(3, 8)
            if self.vessel_class == self.__Vessel_class__.Frigate:
                size = randint(7, 25)
            if self.vessel_class == self.__Vessel_class__.Cruiser:
                size = randint(12, 35)
            if self.vessel_class == self.__Vessel_class__.Destroyer:
                size = randint(45, 96)
            if self.vessel_class == self.__Vessel_class__.Carrier:
                size = randint(102, 310)
            if self.vessel_class == self.__Vessel_class__.Dreadnought:
                size = randint(280, 570)
            return size

    def GetSpaceship(self, request, context):
        spaceship = self.Spaceship()

        result = {'alignment': spaceship.alignment, 'name': spaceship.name, 'length': spaceship.length,
                  'class': spaceship.vessel_class, 'size': spaceship.size, 'armed': spaceship.armed,
                  'officers': spaceship.officers}

        return pb2.SpaceshipInfo(**result)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ReportServicer_to_server(ReportService(), server)
    server.add_insecure_port('[::]:6666')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
