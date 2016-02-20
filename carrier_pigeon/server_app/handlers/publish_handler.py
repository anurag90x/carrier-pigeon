from tornado.web import RequestHandler

class PublishHandler(RequestHandler):
    def get(self):
        self.write("hello world!")
