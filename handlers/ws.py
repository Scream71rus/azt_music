
import datetime
import time

from tornado.websocket import WebSocketHandler

from handlers.base_handler import BaseHandler

ws_users = []
status_to_start = []


class WSMusicHandler(WebSocketHandler, BaseHandler):

    def open(self, *args):
        ws_users.append(self)

    def on_message(self, message):
        if message == 'Go to start!':
            status_to_start.append(self)
            if len(ws_users) == len(status_to_start):
                t = time.time()
                start = int((t + 60) * 1000)
                self.write_message(str(start))

    def on_close(self):
        ws_users.remove(self)
