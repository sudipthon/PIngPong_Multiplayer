import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.18.2'
        # self.server='10.5.1.191'  #clz

        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
    

    def get_pos(self):
        return self.pos
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass 

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        # except socket.error as e:
        #     print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

# n=Network()
# n.send("hello")