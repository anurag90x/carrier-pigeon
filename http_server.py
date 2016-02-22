from carrier_pigeon.app import (
    get_config,
    make_http_server)
import tornado.ioloop

config = get_config()
server = make_http_server()

server.listen(config["http_server"]["port"])
tornado.ioloop.IOLoop.current().start()
