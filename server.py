
import tornado.ioloop
import tornado.web

from urls import urls


def make_app():
    return tornado.web.Application(urls, debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
