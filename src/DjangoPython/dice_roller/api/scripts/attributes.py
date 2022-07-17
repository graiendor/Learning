def __attributes__(attributes, request):
    attributes.strength = 0
    for req in request.GET:
        print(req, 'on')
        if 'strength' in req:
            print('ok')
            attributes.strength += 1
