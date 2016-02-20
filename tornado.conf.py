from carrier_pigeon.app import (
    get_config,
    make_app)
import tornado.ioloop

app = make_app()
config = get_config()

app.listen(config["tornado"]["port"])
tornado.ioloop.IOLoop.current().start()
