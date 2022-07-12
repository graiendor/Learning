import random


def __roll__(roll):
    roll.value = random.randint(1, 10)
    roll.result = "SUCCESS" if roll.value >= 6 else "FAIL"
