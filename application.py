
import psycopg2.extras
import momoko
import tornado.web

from tornado.ioloop import IOLoop

from config import host, port, database, user, password


class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._db = momoko.Pool(
            dsn="host={} port={} database={} user={} password={}".format(host, port, database, user, password),
            size=2,
            ioloop=IOLoop.current(),
            cursor_factory=psycopg2.extras.DictCursor
        )

        self._db.connect()

    @property
    def db(self):
        return self._db
