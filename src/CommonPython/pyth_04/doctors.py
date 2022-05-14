from asyncio import wait
from time import sleep
import threading
import concurrent.futures
import random

doctors = []
thread_local = threading.local()

class Screwdriver:
    is_free = True


class Doctor(int):
    def __init__(self, Doctor):
        self.name = Doctor

    state: str = 'waiting'
    right_hand = None
    left_hand = None
    screwdriver = Screwdriver()
    left_doctor = 0

    def acting(self):
        self.left_doctor = self.name
        for _ in range(2):
            self.left_doctor -= 1
            if self.left_doctor < 0:
                self.left_doctor = 4
        self.wait()
        self.take_screwdrivers()
        self.blast()
        self.put_screwdrivers()

    def wait(self):
        time: int = random.randrange(1, 6, 1)
        sleep(time / 10)

    def take_screwdrivers(self):
        lock = threading.Lock()
        with lock:
            if doctors[self.left_doctor].screwdriver.is_free:
                self.right_hand = self.screwdriver
                self.screwdriver.is_free = False
                self.left_hand = doctors[self.left_doctor].screwdriver
                doctors[self.left_doctor].screwdriver.is_free = False
                # print(f'I am {self.name} Doctor and I took the {self.left_doctor + 1} Doctor screwdriver {doctors[self.left_doctor].screwdriver.is_free}')

    def blast(self):
        # print(self.right_hand, self.left_hand)
        if self.right_hand is not None and self.left_hand is not None:
            print(f'Doctor {self.name}: BLAST!')

    def put_screwdrivers(self):
        lock = threading.Lock()
        with lock:
            self.right_hand = None
            self.left_hand = None
            self.screwdriver.is_free = True
            doctors[self.left_doctor].screwdriver.is_free = True


if __name__ == "__main__":
    doctors = [Doctor(i + 1) for i in range(5)]

    actions_list = [doctors[0].acting, doctors[1].acting, doctors[2].acting, doctors[3].acting, doctors[4].acting]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map(doctors[0].acting)
        futures = [executor.submit(action) for action in actions_list]

        # wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
        # executor.
        # print(f1.result())
        # print(f2.result())
        # print(f3.result())
        # print(f4.result())
        # print(f5.result())

    # t1 = threading.Thread(target=doctors[0].acting)
    # t2 = threading.Thread(target=doctors[1].acting)
    # t3 = threading.Thread(target=doctors[2].acting)
    # t4 = threading.Thread(target=doctors[3].acting)
    # t5 = threading.Thread(target=doctors[4].acting)
    #
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
