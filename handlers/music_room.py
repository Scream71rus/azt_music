
import base64

from handlers.base_handler import BaseHandler


class MusicRoom(BaseHandler):
    async def get(self):
        a = open('handlers/1.mp3', 'rb')
        fd = a.read()
        a.close()

        track_base64 = base64.b64encode(fd)

        self.render('music_room.html', track_base64=track_base64)
