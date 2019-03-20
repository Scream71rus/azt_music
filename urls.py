
from handlers.choose_music_handler import ChooseMusic
from handlers.login_handler import LoginHandler
from handlers.registration_handler import RegistrationHandler

urls = [
    (r"/login", LoginHandler),
    (r"/choose_music", ChooseMusic),
    (r"/registration", RegistrationHandler),
]
