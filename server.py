import sys
import socket
import select

SOCKETS = []
HOST = ''
RECV_BUFFER = 4096
PORT = 9000
