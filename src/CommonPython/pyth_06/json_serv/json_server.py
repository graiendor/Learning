import json

import grpc
from concurrent import futures
import json_pb2_grpc as pb2_grpc
import json_pb2 as pb2
from random import choice


class JsonService(pb2_grpc.ProcessJsonServicer):
    def __init__(self):
        self.end = False
        self.low = 0
        self.middle = 0
        self.high = 0
        self.intensity = 1
        with open('QA.json') as QA:
            self.qa = json.load(QA)

    def Restart(self):
        self.low = 0
        self.middle = 0
        self.high = 0
        self.intensity = 1

    def GetJsonResult(self, request, context):
        result = {}
        if request.restart:
            self.Restart()
            self.end = False
        if request.allow:
            result = {'passed': self.define_result(), 'intensity': self.intensity, 'end': self.end}
        return pb2.JsonResult(**result)

    def define_result(self) -> bool:
        result = False
        if self.low in range(len(self.qa['low_intensity_questions'])):
            result = choice(['1', '2', '3']) == choice(self.qa['low_intensity_questions'][self.low][f'answer{choice([1, 2, 3])}'])
            self.low += 1
        elif self.middle in range(len(self.qa['middle_intensity_questions'])):
            self.intensity = 2
            result = choice(['1', '2', '3']) == choice(self.qa['middle_intensity_questions'][self.middle][f'answer{choice([1, 2, 3])}'])
            self.middle += 1
        elif self.high in range(len(self.qa['high_intensity_questions'])):
            self.intensity = 3
            result = choice(['1', '2', '3']) == choice(self.qa['high_intensity_questions'][self.high][f'answer{choice([1, 2, 3])}'])
            self.high += 1
        else:
            self.end = True
        return result


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProcessJsonServicer_to_server(JsonService(), server)
    server.add_insecure_port('[::]:8092')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
