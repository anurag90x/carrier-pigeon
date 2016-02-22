from tornado.websocket import WebSocketHandler

class MessageHandler(WebSocketHandler):
    def open(self):
        print("Socket opened")

    def on_message(self, message):
        self.write_message("You said " + message)

    def on_close(self):
        print("Socket closed")

    def check_origin(self, origin):
        return True
