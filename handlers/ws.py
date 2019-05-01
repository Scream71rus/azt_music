
from tornado.websocket import WebSocketHandler

from handlers.base_handler import BaseHandler

ws_users = []


class WSMusicHandler(WebSocketHandler, BaseHandler):

    def open(self, *args):
        ws_users.append(self)
        print(ws_users)

    def on_message(self, message):
        pass

    def on_close(self):
        print(1)
        ws_users.remove(self)
