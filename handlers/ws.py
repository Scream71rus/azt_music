
from tornado.websocket import WebSocketHandler


ws_users = []


class WSMusicHandler(WebSocketHandler):

    def open(self, *args):
        ws_users.append(self)

    def on_message(self, message):
        pass

    def on_close(self):
        ws_users.remove(self)
