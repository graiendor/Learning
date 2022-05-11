import redis
import json
from time import sleep
from sys import argv


def stream():
    """Launches the everlasting stream, whick reads messages from the channel and prints them, if
    they the receiver and sender are the same, as stated in arg line and if amount of money is not negative"""
    subscriber.subscribe('bad guyz')
    for message in subscriber.listen():
        message = message['data'].decode('utf8').replace("'", '"')
        message = json.loads(message)
        if message.get('metadata').get('from') == sender and message.get('metadata').get('to') == receiver:
            print(message)


if __name__ == '__main__':
    if argv[1] == '-e':
        sender: int = int(argv[2])
        receiver: int = int(argv[3])
        if len(argv[2]) == 4 and len(argv[3]) == 4:
            server = redis.Redis(host='localhost', port=6379, db=0)
            server.set('test_result', 'works')
            subscriber = server.pubsub()
            subscriber.ignore_subscribe_messages = True
            stream()
