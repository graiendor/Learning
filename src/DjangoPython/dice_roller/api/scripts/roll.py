import random


def __roll__(roll, dices):
    values: list[str] = []
    for _ in range(dices):
        values.append(str(random.randint(1, 10)))
    roll.value = ', '.join(values)
        # roll.result = "SUCCESS" if roll.value >= 6 else "FAIL"
