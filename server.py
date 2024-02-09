import socket
import threading
import sys

import pickle









ip='192.168.18.2'
# server='10.5.1.191'  #clz
port=5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(ip,port)
try:
    server.bind((ip, port))
except socket.error as e:
    print(str(e))

server.listen(5)
print("Waiting for a connection, Server Started")

# pos=[[(350.00,0.00),0],[(-350.00,0.00),0]]
pos=[(350.00,0.00),(-350.00,0.00)]
player=0

def threaded_client(conn,player):
    # global player
    conn.send(pickle.dumps(pos[player]))
    while True:
        try:
            data =pickle.loads(conn.recv(2048))
            pos[player]=data

            if not data:
                print('Disconnected')
                break
            else:
                if player==1:
                    reply=[pos[0],player]
                else:
                    reply=[pos[1],player]
                
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print('Lost connection')
    # player-=1
    conn.close()





player=0
while True:
    conn, addr = server.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))
    threading.Thread(target=threaded_client, args=(conn,player)).start()
    player+=1
    # print("playerid:",player_id)