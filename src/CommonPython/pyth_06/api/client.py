import input_pb2, input_pb2_grpc
import json_pb2, json_pb2_grpc
import store_pb2, store_pb2_grpc
import grpc


class JsonClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8092

    def get_response(self, allow: bool, restart: bool):
        with grpc.insecure_channel('localhost:8092') as channel:
            stub = json_pb2_grpc.ProcessJsonStub(channel)
            message = json_pb2.AllowJson(allow=allow, restart=restart)
            response = stub.GetJsonResult(message)
        return response

    def restart(self):
        self.get_response(False, True)


class InputClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8091

    def get_response(self, intensity):
        respiration: int = check_if_integer()
        hearth_rate: int = check_if_integer()
        blushing_level: int = check_if_integer()
        pupillary_dilation: int = check_if_integer()
        with grpc.insecure_channel('localhost:8091') as channel:
            stub = input_pb2_grpc.ProcessInputStub(channel)
            message = input_pb2.Input(respiration=respiration, hearth_rate=hearth_rate, blushing_level=blushing_level,
                                      pupillary_dilation=pupillary_dilation, intensity=intensity)
            response = stub.GetInputResult(message)
        return response


class StoreClient(object):
    def put_data(self, subject, test_result, input_result):
        with grpc.insecure_channel('localhost:8093') as channel:
            stub = store_pb2_grpc.ProcessDataStub(channel)
            message = store_pb2.Data(test_subject=subject, test_result=test_result, input_result=input_result)
            response = stub.SendData(message)
        return response

    def delete_data(self, subject):
        with grpc.insecure_channel('localhost:8093') as channel:
            stub = store_pb2_grpc.ProcessDataStub(channel)
            message = store_pb2.TestSubject(test_subject=subject)
            response = stub.DeleteData(message)
        return response

    def get_verdict(self, subject):
        with grpc.insecure_channel('localhost:8093') as channel:
            stub = store_pb2_grpc.ProcessDataStub(channel)
            message = store_pb2.TestSubject(test_subject=subject)
            response = stub.GetVerdict(message)
        return response

def check_if_integer():
    integer: bool = False
    value = 0
    while not integer:
        value = input()
        try:
            value = int(value)
            assert value > 0
            integer = True
        except ValueError:
            print('You have entered invalid data. Try again!')
    return value


def run():
    json_client = JsonClient()
    input_client = InputClient()
    store_client = StoreClient()
    print("Enter the test subject's number")
    subject: int = check_if_integer()
    store_client.delete_data(subject)
    json_client.restart()
    end = False
    while not end:
        json_response = json_client.get_response(True, False)
        input_response = input_client.get_response(json_response.intensity)
        store_client.put_data(subject, json_response.passed, input_response.result)
        if json_response.end:
            end = True
    print('Subject is replicant: ', store_client.get_verdict(subject).verdict)


if __name__ == '__main__':
    run()



