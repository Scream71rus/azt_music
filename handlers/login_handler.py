from models.main_model import MainModel
from pbkdf2 import PBKDF2
from tornado.web import RequestHandler

import os


class LoginHandler(RequestHandler, MainModel):

    async def check_password(self, password, customer_data):
        if PBKDF2(password, customer_data.get('salt')).hexread(16) == customer_data.get('password'):
            session_key = os.urandom(24).hex()

            self.set_cookie("azt_customer", session_key)
            self.set_db_cookie(session_key, customer_data.get('id'))

            return True
        else:
            return False

    def get(self):
        self.render('../templates/login.html')

    async def post(self):
        login = self.get_argument('login').strip()
        password = self.get_argument('password').strip()

        if login and password:
            customer_data = await self.get_password(login)
            check_password = await self.check_password(password, customer_data)

            if check_password:
                self.render('..templates/music_room.html')
            else:
                self.redirect('/login')
        else:
            self.redirect('/login')
