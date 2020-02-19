from Cache import Cache
from Data import Data
import socket


class DistributedCache():
	count = 0

	def __init__(self, max_size=3, time_expire=2, server_address=None):
			self.cache = Cache(max_size, time_expire)
			self.server_address = server_address
	
	def start_server(self) -> None:
		if self.server_address is not None:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server.bind((self.server_address, 5000))
			print("Server started")
			self.listen_clients()
	
	def start_client(self) -> None:
		if self.server_address is not None:
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.client.connect((self.server_address, 5000))

	def send_data_to_clients(self, data) -> None:
		self.server.sendall(data.encode())
		pass

	def send_data_to_server(self, msg) -> None:
		self.count += 1
		self.data = Data(self.count, msg)
		self.cache.putData(self.data)
		msg = ("\n"+msg).encode()
		self.client.sendall(msg)
	
	def listen_clients(self) -> None:
		self.server.listen(1)
		print("Server is listening for clients...\n\n")

	def read_data_server(self) -> None:
		con, cli = self.server.accept()
		msg = con.recv(1024).decode()
		print("-- CLI_" + str(cli[1]) + " -- " + msg)

	def getCache(self, id):
		return self.cache.getData(id)
	

serv1 = DistributedCache(3, 2, '127.0.0.1')
serv1.start_server()

cli1 = DistributedCache(3, 2, '127.0.0.1')
cli1.start_client()

#cli2 = DistributedCache(3, 2, '127.0.0.1')
#cli2.start_client()

cli1.send_data_to_server('Hallo, Freund')
cli1.send_data_to_server('Wie geht es dir?')
cli1.send_data_to_server('Willkomen')
cli1.send_data_to_server('Ausgezeichnet')
serv1.read_data_server()

print("---- CACHE INFO ----")
print(cli1.getCache(1))
print(cli1.getCache(2))
print(cli1.getCache(3))
print(cli1.getCache(4))





		

