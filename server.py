import tornado.ioloop
import tornado.web
from handlers.choose_music_handler import ChooseMusic
from handlers.login_handler import LoginHandler
from handlers.registration_handler import RegistrationHandler


def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler),
        (r"/choose_music", ChooseMusic),
        (r"/registration", RegistrationHandler),

    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()