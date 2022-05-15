from enum import IntEnum

import grpc
from concurrent import futures
import time
import server_pb2_grpc as pb2_grpc
import server_pb2 as pb2
from random import choice, uniform


class ReportService(pb2_grpc.ReportServicer):

    def __init__(self):
        pass



    class Spaceship:
        class Vessel_class(IntEnum):
            Corvette = 0
            Frigate = 1
            Cruiser = 2
            Destroyer = 3
            Carrier = 4
            Dreadnought = 5

        def __init__(self):
            self.alignment: int = choice([0, 1])
            with open('known_officers.txt', 'r') as file:
                lines = file.read().splitlines()
                self.name = choice(lines)

            self.vessel_class: int = choice(list(self.Vessel_class))
            self.length = self.define_length()

        def define_length(self) -> float:
            length: float = 0
            if self.vessel_class == self.Vessel_class.Corvette:
                length = uniform(10, 150)
            if self.vessel_class == self.Vessel_class.Frigate:
                length = uniform(30, 250)
            if self.vessel_class == self.Vessel_class.Cruiser:
                length = uniform(75, 500)
            if self.vessel_class == self.Vessel_class.Destroyer:
                length = uniform(160, 750)
            if self.vessel_class == self.Vessel_class.Carrier:
                length = uniform(1000, 1200)
            if self.vessel_class == self.Vessel_class.Dreadnought:
                length = uniform(1000, 2500)
            return length

    def GetSpaceship(self, request, context):
        # message = request.message

        spaceship = self.Spaceship()

        result = {'alignment': spaceship.alignment, 'name': spaceship.name, 'length': spaceship.length,
                  'class': spaceship.vessel_class, 'size': 4, 'armed': True,
                  'officers': ["Nick", "NeNick"]}

        return pb2.SpaceshipInfo(**result)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ReportServicer_to_server(ReportService(), server)
    server.add_insecure_port('[::]:6666')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()

# class UnaryService(pb2_grpc.UnaryServicer):
#
#     def __init__(self, *args, **kwargs):
#         pass
#
#     def GetServerResponse(self, request, context):
#
#         # get the string from the incoming request
#         message = request.message
#         result = f'Hello I am up and running received "{message}" message from you'
#         result = {'message': result, 'received': True}
#
#         return pb2.MessageResponse(**result)
#
#
# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
#     server.add_insecure_port('[::]:6666')
#     server.start()
#     server.wait_for_termination()
#
#
# if __name__ == '__main__':
#     serve()