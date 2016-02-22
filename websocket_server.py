from carrier_pigeon.app import (
    get_config,
    make_websocket_server)
import tornado.ioloop

config = get_config()
server = make_websocket_server()

server.listen(config["websocket_server"]["port"])
tornado.ioloop.IOLoop.current().start()
