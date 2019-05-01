
import tornado.web

from handlers.choose_music_handler import ChooseMusic
from handlers.login_handler import LoginHandler
from handlers.registration_handler import RegistrationHandler
from handlers.ws import WSMusicHandler
from handlers.music_room import MusicRoom

urls = [
    (r"/login", LoginHandler),
    (r"/choose_music", ChooseMusic),
    (r"/registration", RegistrationHandler),
    (r"/ws/", WSMusicHandler),
    (r"/music-room", MusicRoom),

    (r"/static/(.*)/?", tornado.web.StaticFileHandler, {"path": "./static"}),
    (r"/src/(.*)/?", tornado.web.StaticFileHandler, {"path": "./static/src"},),
]
