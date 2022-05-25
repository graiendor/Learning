import input_server
import input_pb2_grpc
import input_pb2
import grpc
from pytest import raises

service = input_server.InputService()

channel = grpc.insecure_channel('localhost:8091')
stub = input_pb2_grpc.ProcessInputStub(channel)


def test_input_out_of_range():
    message = input_pb2.Input(respiration=1, hearth_rate=2, blushing_level=3,
                              pupillary_dilation=4, intensity=5)
    assert stub.GetInputResult(message).result is False

    with raises(TypeError):
        input_pb2.Input(respiration='gg', hearth_rate=2, blushing_level=3,
                        pupillary_dilation=4, intensity=5)

    message = input_pb2.Input(respiration=16, hearth_rate=96, blushing_level=6,
                              pupillary_dilation=8, intensity=15)
    assert stub.GetInputResult(message).result is False


def test_input_in_of_range():
    message = input_pb2.Input(respiration=11, hearth_rate=60, blushing_level=1,
                              pupillary_dilation=2, intensity=1)
    assert stub.GetInputResult(message).result is True

    message = input_pb2.Input(respiration=14, hearth_rate=70, blushing_level=3,
                              pupillary_dilation=3, intensity=2)
    assert stub.GetInputResult(message).result is True

    message = input_pb2.Input(respiration=16, hearth_rate=96, blushing_level=6,
                              pupillary_dilation=8, intensity=3)
    assert stub.GetInputResult(message).result is True

    message = input_pb2.Input(respiration=19, hearth_rate=110, blushing_level=7,
                              pupillary_dilation=8, intensity=3)
    assert stub.GetInputResult(message).result is False

    message = input_pb2.Input(respiration=16, hearth_rate=-96, blushing_level=6,
                              pupillary_dilation=8, intensity=3)
    assert stub.GetInputResult(message).result is False
