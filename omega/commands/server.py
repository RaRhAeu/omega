from flask_script import Server as BaseServer
from omega.app import create_app


class Server(BaseServer):
    def handle(self, app, *args, **kw):
        app = create_app()
        super(Server, self).handle(app, *args, **kw)
