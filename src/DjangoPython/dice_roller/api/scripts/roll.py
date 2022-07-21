import random


def __roll__(roll, dices):
    values: list[str] = []
    for _ in range(dices):
        values.append(str(random.randint(1, 10)))
    roll.value = ', '.join(values)
        # roll.result = "SUCCESS" if roll.value >= 6 else "FAIL"

def __dices__(fields):
    dices = 0
    print()
    if fields['strength_check']: dices += fields['strength']
    if fields['dexterity_check']: dices += fields['dexterity']
    if fields['stamina_check']: dices += fields['stamina']
    if fields['charisma_check']: dices += fields['charisma']
    if fields['manipulation_check']: dices += fields['manipulation']
    if fields['composure_check']: dices += fields['composure']
    if fields['intelligence_check']: dices += fields['intelligence']
    if fields['wits_check']: dices += fields['wits']
    if fields['resolve_check']: dices += fields['resolve']
    return dices
