import socket
import pickle
from _thread import *
from game import Game

server = "86.132.63.32"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('',port))
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection...")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096*4096*4))
            if gameId in games:
                game = games[gameId]
                if not data:
                    print("e3")
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                print("e0")
                break
        except socket.error as e:
            print("e1",e)
            break
    try:
        del games[gameId]
        print("Closing game",gameId)
        print((p + 1),"left")
    except:
        print("e2")
        pass
    idCount -=1
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:",addr)
    idCount += 1
    p = 0
    gameId = (idCount - 1)//4
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("new game")
    elif idCount % 3 == 1:
        games[gameId].ready = True
        p = 3
    elif idCount % 2 == 1:
        p = 2
    else:
        p = 1
    
    start_new_thread(threaded_client, (conn, p, gameId))
