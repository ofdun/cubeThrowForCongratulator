import telebot
from telebot import types
import requests as req
import os
from time import sleep
from threading import Thread
from random import choice


TOKEN = '5979625092:AAFWdT1jp-RDOm-19TZvQRf96liaMoPjKxc'
bot = telebot.TeleBot(token=TOKEN)


class Photo():
    def __init__(self, path, name):
        self.path = path
        self.name = name


@bot.message_handler(commands=['start'])
def starter(message):
    bot.send_message(message.from_user.id, 'Hey! I am a tester bot for ofdun!')


@bot.message_handler(content_types=['text'])
def throwCube(message):
    if message.text == 'Брось кубик':
        pathToPhoto = 'other/cubePictures/' + choice(os.listdir(PATH_TO_CUBE))
        nameOfPhoto = pathToPhoto[pathToPhoto.rfind(
            '/')+1:pathToPhoto.rfind('.')]
        photo = Photo(pathToPhoto, nameOfPhoto)
        with open(photo.path, 'rb') as photoBytes:
            bot.send_message(message.from_user.id,
                             text=f'Тебе выпало {photo.name}!')
            return bot.send_photo(message.from_user.id, photo=photoBytes)


def checkIfNew():
    path1 = 'other'
    path2 = 'cubePictures'
    global PATH_TO_CUBE
    PATH_TO_CUBE = path1 + '/' + path2
    if not os.path.exists(path1):
        os.makedirs(path1)
    if not os.path.exists(PATH_TO_CUBE):
        os.makedirs(PATH_TO_CUBE)
    if len(os.listdir(PATH_TO_CUBE)) < 6:
        raise Exception('YOU ARE DUMB AF, PUT PICTURES OF CUBE DUMBASS')


def polling():
    try:
        bot.infinity_polling()
    except:
        sleep(1)
    finally:
        print('RequestsError: reconecting...')


if __name__ == '__main__':
    Thread(target=polling).start()
    Thread(target=checkIfNew).start()
