from models.main_model import MainModel
from pbkdf2 import PBKDF2
from tornado.web import RequestHandler

import os


class RegistrationHandler(RequestHandler, MainModel):

    def get(self):
        self.render('../templates/registration.html')

    async def post(self):
        login = self.get_argument('login').strip()
        password = self.get_argument('password').strip()
        replace_password = self.get_argument('replace_password').strip()

        if login and password:
            if replace_password == password:
                check_login = await self.check_login(login)
                if not check_login:
                    salt = os.urandom(16).hex()
                    hash_password = PBKDF2(password, salt).hexread(16)

                    customer_id = await self.create_customer(login, hash_password, salt)

                    if customer_id:
                        session_key = os.urandom(24).hex()

                        self.set_cookie("azt_customer", session_key)
                        self.set_db_cookie(session_key, customer_id)

                        self.render('..templates/music_room.html')

                    else:
                        self.redirect('/registration')
                else:
                    self.redirect('/registration')
            else:
                self.redirect('/registration')
        else:
            self.redirect('/registration')
