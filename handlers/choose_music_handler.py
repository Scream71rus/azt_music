from models.main_model import MainModel
from tornado.web import RequestHandler

import os


class ChooseMusic(RequestHandler, MainModel):

    @property
    def directory(self):
       return "C:/Users/User/Desktop/Флешка/SPL"

    def get_music_list(self):
        music = os.listdir(self.directory)
        return music

    async def get(self):
        cookie = self.get_cookie('azt_customer')
        customer = self.get_customer(cookie)

        if customer:
            music = self.get_music_list()
            self.render('../templates/music_list.html', music=music)
        else:
            self.redirect('/login')

    def post(self):
        track = self.get_argument('track')

        file = open(self.directory + '/' + track, 'r')
        file_data = file.read()
        file.close()

        self.render('../templates/index.html')
