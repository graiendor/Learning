import redis
import json
from time import sleep
from sys import argv


def stream():
    """Launches the everlasting stream, whick reads messages from the channel and prints them, if
    they the receiver and sender are the same and if the first argument in the arg list is a receiver and
    the amount of money is not negative"""
    subscriber.subscribe('bad guyz')
    for message in subscriber.listen():
        message = message['data'].decode('utf8').replace("'", '"')
        message = json.loads(message)
        if message.get('metadata').get('from') == sender and message.get('metadata').get('to') == receiver:
            print(message)
        elif message.get('metadata').get('to') == sender and int(message.get('amount')) > 0:
            message.update({'metadata': {'from': sender, 'to': message.get('metadata').get('from')}})
            print(message)


if __name__ == '__main__':
    if argv[1] == '-e':
        sender: int = int(argv[2])
        receiver: int = int(argv[3])
        if len(argv[2]) == 10 and len(argv[3]) == 10:
            server = redis.Redis(host='localhost', port=6379, db=0)
            server.set('test_result', 'works')
            subscriber = server.pubsub()
            subscriber.ignore_subscribe_messages = True
            stream()
