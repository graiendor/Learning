import grpc
from concurrent import futures
import input_pb2_grpc as pb2_grpc
import input_pb2 as pb2


class InputService(pb2_grpc.ProcessInputServicer):
    def __init__(self):
        self.intensity = 0

    def GetInputResult(self, request, context):
        result = {'result': False}
        if request.respiration and request.hearth_rate and request.blushing_level and request.pupillary_dilation:
            self.intensity = request.intensity
            valid: bool = self.respiration_validate(request.respiration) and \
                          self.hearth_rate_validate(request.hearth_rate) and \
                          self.blushing_level_validate(request.blushing_level) and \
                          self.pupillary_dilation_validate(request.pupillary_dilation)
            result = {'result': valid}
        return pb2.InputResult(**result)

    def respiration_validate(self, respiration):
        valid: bool = False
        if self.intensity == 1:
            valid = respiration in range(8, 13)
        if self.intensity == 2:
            valid = respiration in range(12, 17)
        if self.intensity == 3:
            valid = respiration in range(12, 21)
        return valid

    def hearth_rate_validate(self, hearth_rate):
        valid: bool = False
        if self.intensity == 1:
            valid = hearth_rate in range(40, 80)
        if self.intensity == 2:
            valid = hearth_rate in range(60, 100)
        if self.intensity == 3:
            valid = hearth_rate in range(80, 120)
        return valid

    def blushing_level_validate(self, blushing_level):
        valid: bool = False
        if self.intensity == 1:
            valid = blushing_level in range(1, 3)
        if self.intensity == 2:
            valid = blushing_level in range(2, 5)
        if self.intensity == 3:
            valid = blushing_level in range(5, 7)
        return valid

    def pupillary_dilation_validate(self, pupillary_dilation):
        valid: bool = False
        if self.intensity == 1:
            valid = pupillary_dilation in range(2, 4)
        if self.intensity == 2:
            valid = pupillary_dilation in range(3, 7)
        if self.intensity == 3:
            valid = pupillary_dilation in range(6, 9)
        return valid


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProcessInputServicer_to_server(InputService(), server)
    server.add_insecure_port('[::]:8091')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
