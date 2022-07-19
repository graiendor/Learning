def __attributes__(attributes, request):
    attributes.strength = request.POST.get('strength')
    attributes.dexterity = request.POST.get('dexterity')
    attributes.stamina = request.POST.get('stamina')
    attributes.charisma = request.POST.get('charisma')
    attributes.manipulation = request.POST.get('manipulation')
    attributes.composure = request.POST.get('composure')
    attributes.intelligence = request.POST.get('intelligence')
    attributes.wits = request.POST.get('wits')
    attributes.resolve = request.POST.get('resolve')


def __load_attributes__(attributes):
    attributes.strength = 1
    attributes.dexterity = 1
    attributes.stamina = 1
    attributes.charisma = 1
    attributes.manipulation = 1
    attributes.composure = 1
    attributes.intelligence = 1
    attributes.wits = 1
    attributes.resolve = 1