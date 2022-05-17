import json
import threading
from enum import IntEnum
from typing import List, Dict
import google.protobuf.json_format as js

import grpc
from concurrent import futures
import time
import input_pb2_grpc as pb2_grpc
import input_pb2 as pb2
from random import choice, uniform, randint
from pydantic import BaseModel, ValidationError, Field, root_validator


class InputService(pb2_grpc.ProcessInputServicer):
    def __init__(self):
        pass

    def GetInputResult(self, request, context):
        result = {'valid': False}
        if request.respiration and request.hearth_rate and request.blushing_level and request.pupillary_dilation:
            valid: bool = self.respiration_validate(request.respiration) and \
                          self.hearth_rate_validate(request.hearth_rate) and \
                          self.blushing_level_validate(request.blushing_level) and \
                          self.pupillary_dilation_validate(request.pupillary_dilation)
            result = {'result': True, 'valid': valid}
        return pb2.InputResult(**result)

    def respiration_validate(self, respiration):
        return respiration in range(12, 16)

    def hearth_rate_validate(self, hearth_rate):
        return hearth_rate in range(60, 100)

    def blushing_level_validate(self, blushing_level):
        return blushing_level in range(1, 6)

    def pupillary_dilation_validate(self, pupillary_dilation):
        return pupillary_dilation in range(2, 8)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProcessInputServicer_to_server(InputService(), server)
    server.add_insecure_port('[::]:8082')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
