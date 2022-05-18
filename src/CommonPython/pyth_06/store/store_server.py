import json
from os import remove
from os.path import exists, getsize

import grpc
from concurrent import futures
import store_pb2_grpc as pb2_grpc
import store_pb2 as pb2


class StoreDataService(pb2_grpc.ProcessDataServicer):
    def __init__(self):
        self.path = 'subjects'

    def SendData(self, request, context):
        path = f'{self.path}/subject_{request.test_subject}.json'
        if not exists(path):
            open(path, 'w').close()
        with open(path, 'r+') as file:
            if getsize(path):
                subject = json.load(file)
                subject.append({
                    "test": request.test_result,
                    "input": request.input_result
                })
            else:
                subject = json.loads('[{"test": 1, "input": 1}]')
                subject[0]["test"] = request.test_result
                subject[0]["input"] = request.input_result
            file.seek(0)
            json.dump(subject, file)
            result = {'test_subject': request.test_subject}
        return pb2.TestSubject(**result)

    def DeleteData(self, request, context):
        if exists(f'{self.path}/subject_{request.test_subject}.json'):
            remove(f'{self.path}/subject_{request.test_subject}.json')
        result = {'test_subject': request.test_subject}
        return pb2.TestSubject(**result)

    def GetVerdict(self, request, context):
        file_exists: bool = False
        data_list: list[bool] = []
        path = f'{self.path}/subject_{request.test_subject}.json'
        if exists(path) and getsize(path):
            file_exists = True
            with open(path) as file:
                subject = json.load(file)
                for data in subject:
                    data_list.append(data["test"] == data["input"])
                verdict = data_list.count(True) > len(subject)
        result = {'exists': file_exists, 'verdict': verdict}
        return pb2.Verdict(**result)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ProcessDataServicer_to_server(StoreDataService(), server)
    server.add_insecure_port('[::]:8093')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run()