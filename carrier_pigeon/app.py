from carrier_pigeon.config import read_config
from carrier_pigeon.server_app.handlers.publish_handler import PublishHandler
import tornado.web

def get_config(config_file='./development.ini'):
   return read_config(config_file)

def make_app():
    routes = [(r"/publish", PublishHandler)]
    app = tornado.web.Application(routes)
    return app
