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
            print(response.passed, response.intensity, response.end)
        return response

    def restart(self):
        self.get_response(False, True)


class InputClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8082

    def get_response(self, intensity):
        respiration = int(input())
        hearth_rate = int(input())
        blushing_level = int(input())
        pupillary_dilation = float(input())
        with grpc.insecure_channel('localhost:8082') as channel:
            stub = input_pb2_grpc.ProcessInputStub(channel)
            message = input_pb2.Input(respiration=respiration, hearth_rate=hearth_rate, blushing_level=blushing_level,
                                      pupillary_dilation=pupillary_dilation, intensity=intensity)
            response = stub.GetInputResult(message)
            print(response.result, response.valid)
        return response

    # def restart(self):
        # self.get_response(False, True)


def run():
    json_client = JsonClient()
    input_client = InputClient()
    json_client.restart()
    end = False
    while end != True:
        json_response = json_client.get_response(True, False)
        input_response = input_client.get_response(json_response.intensity)
        print(input_response)
        if json_response.end:
            end = True


if __name__ == '__main__':
    run()



