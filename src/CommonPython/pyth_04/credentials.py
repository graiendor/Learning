import cherrypy
import json

config = {
    'global': {
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8888
    }
}


class Credentials(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def credentials(self, specie):
        base = {"Cyberman": "John Lumic",
                "Dalek": "Davros",
                "Judoon": "Shadow Proclamation Convention 15 Enforcer",
                "Human": "Leonardo da Vinci",
                "Ood": "Klineman Halpen",
                "Silence": "Tasha Lem",
                "Slitheen": "Coca-Cola salesman",
                "Sontaran": "General Staal",
                "Time Lord": "Rassilon",
                "Weeping Angel": "The Division Representative",
                "Zygon": "Broton"}
        result = base.get(specie)

        cherrypy.response.status = 404
        if result != None:
            cherrypy.response.status = 200
            result = {specie: result}
        else:
            result = {specie: "Unknown"}
        return json.dumps(result)


if __name__ == '__main__':
    cherrypy.quickstart(Credentials(), '/', config)
