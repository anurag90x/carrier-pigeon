from carrier_pigeon.config import read_config
from carrier_pigeon.server_app.handlers.publish_handler import PublishHandler
from carrier_pigeon.websocket_server.handlers.message_handler import MessageHandler
import tornado.web

def get_config(config_file='./development.ini'):
   return read_config(config_file)

def make_http_server():
    routes = [
        (r"/publish", PublishHandler)]
    app = tornado.web.Application(routes)
    return app

def make_websocket_server():
    routes = [
        (r"/message", MessageHandler)]
    app = tornado.web.Application(routes)
    return app
