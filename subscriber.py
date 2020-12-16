import sys
import zmq

context = zmq.Context()

print("Connecting to server…")

socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:2000")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    message = socket.recv()
    print(message)