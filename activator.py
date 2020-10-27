from tkinter import *
from tkinter import messagebox
import os
from sys import exit
from uuid import getnode as getmac
import requests
import socket
import getpass
from os import remove
from sys import argv


userID = getpass.getuser()
machineID = socket.gethostname()
mac_address = getmac()
ip = socket.gethostbyname(machineID)


def telegram_bot_sendtext(bot_message):

    bot_token = '1236952296:AAE_2qBZqsELFpGNpubya6i7E9ChngWtMb0'
    bot_chatID = '902073466'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def enviar():
    telegram_bot_sendtext(
        "El codigo es : "+machineID+" \nEl usuario que ingresa es: "+userID+' \nLa direccion MAC es: '+str(mac_address) + ' \nLa direccion IP de la solicitud es: '+ip)
    messagebox.showinfo('Activacion exitosa',
                        'Se ha enviado el codigo de activacion al servidor')
    exit()


confirm = Tk()
confirm.title('Proceso de verificacion')
confirm.config()
confirmLabel = Label(confirm, text='Presione el boton para iniciar \nel proceso de activacion',
                     width=30, height=4)
confirmBtn = Button(confirm, text='Validar', command=enviar)
confirmLabel.grid(column=1, row=1)
confirmBtn.grid(column=1, row=2, padx=10, pady=10)
confirm.mainloop()
