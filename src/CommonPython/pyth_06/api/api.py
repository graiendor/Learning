import input_pb2, input_pb2_grpc
import json_pb2, json_pb2_grpc
import grpc

class JsonClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8081

    def get_response(self, allow: bool, restart: bool):
        with grpc.insecure_channel('localhost:8081') as channel:
            stub = json_pb2_grpc.ProcessJsonStub(channel)
            message = json_pb2.AllowJson(allow=allow, restart=restart)
            response = stub.GetJsonResult(message)
        return response

    def restart(self):
        self.get_response(False, True)


class InputClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8082

    def get_response(self, intensity):
        respiration: int = self.check_if_integer()
        hearth_rate: int = self.check_if_integer()
        blushing_level: int = self.check_if_integer()
        pupillary_dilation: int = self.check_if_integer()
        with grpc.insecure_channel('localhost:8082') as channel:
            stub = input_pb2_grpc.ProcessInputStub(channel)
            message = input_pb2.Input(respiration=respiration, hearth_rate=hearth_rate, blushing_level=blushing_level,
                                      pupillary_dilation=pupillary_dilation, intensity=intensity)
            response = stub.GetInputResult(message)
        return response

    def check_if_integer(self):
        integer: bool = False
        value = 0
        while not integer:
            value = input()
            try:
                value = int(value)
                integer = True
            except ValueError:
                print('You have entered invalid data. Try again!')
        return value


def run():
    json_client = JsonClient()
    input_client = InputClient()
    json_client.restart()
    end = False
    while end != True:
        json_response = json_client.get_response(True, False)
        input_response = input_client.get_response(json_response.intensity)
        print(input_response.result, json_response.passed)
        if json_response.end:
            end = True


if __name__ == '__main__':
    run()



