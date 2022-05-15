from typing import List

import grpc
import server_pb2_grpc as pb2_grpc
import server_pb2 as pb2


class ReportClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 6666

    def get_spaceship(self):
        with grpc.insecure_channel('localhost:6666') as channel:
            stub = pb2_grpc.ReportStub(channel)
            main_coordinates: List[int] = [24, 54, 30, 32]
            second_coordinates: List[float] = [24.32, 31.24]
            # message = pb2.Coordinates(coordinates='24 54 24.32 30 32 31.24')
            message = pb2.Coordinates(coordinate1=main_coordinates[0], coordinate2=main_coordinates[1],
                                      coordinate3=second_coordinates[0], coordinate4=main_coordinates[2],
                                      coordinate5=main_coordinates[3], coordinate6=second_coordinates[1])
            print(f'{message}')
            response = stub.GetSpaceship(message)
        return response


if __name__ == '__main__':
    client = ReportClient()
    result = client.get_spaceship()
    print(f'{result}')