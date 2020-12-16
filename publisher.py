import time
import zmq
import os

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:2000")

folder_name = input('Please enter a folder name: ')
path = folder_name
files = os.listdir(path)

while True:
    for file in files:
        message = 'Folder {path} has {file}'.format(path=path, file=file)
        socket.send_string(message)
    break