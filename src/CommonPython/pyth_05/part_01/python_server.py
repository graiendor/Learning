import grpc
from concurrent import futures
import time
import server_pb2_grpc as pb2_grpc
import server_pb2 as pb2


class ReportService(pb2_grpc.ReportServicer):

    def __init__(self):
        pass

    def GetSpaceship(self, request, context):
        # message = request.message
        # result = f'Hello I am up and running received "{message}" message from you'

        result = {'alignment': 1, 'name': 'Rachehan', 'length': 450.32, 'class': 3, 'size': 4, 'armed': True,
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