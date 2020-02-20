from Cache import Cache
from Data import Data
import socket
from threading import Thread
import traceback


class DistributedCache():
	count = 0

	def __init__(self, max_size=3, time_expire=2, server_address=None):
			self.cache = Cache(max_size, time_expire)
			self.server_address = server_address
	
	def start_server(self) -> None:
		if self.server_address is not None:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			
			try:
				self.server.bind((self.server_address, 5000))
			except:
				print("Bind failed")

			print("Server started")
			self.listen_clients()
	
	def start_client(self) -> None:
		if self.server_address is not None:
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect((self.server_address, 5000))

	def send_data_to_clients(self, data) -> None:
		self.server.sendall(data.encode())
		pass

	def send_data_to_server(self, msg) -> None:
		self.count += 1
		self.data = Data(self.count, msg)
		self.cache.putData(self.data)
		self.client.sendall(msg.encode("utf8"))
	
	def listen_clients(self) -> None:
		self.server.listen(1)
		print("Server is listening for clients...\n\n")

	def client_thread(self, conn, cli) -> None:
		is_active = True
		while is_active:
			msg = conn.recv(5120).decode()
			if msg == 'quit':
				print("exiting...")
				conn.close()
				is_active = False
				
			print(" CLI_" + str(cli[1]) + " -> " + msg)
		

	def read_data_from_server(self) -> None:
		while True:
			conn, cli = self.server.accept()
			try:
				Thread(target=self.client_thread, args=(conn, cli)).start()
			except:
				print("Thread did not start")

	def getCache(self, id):
		return self.cache.getData(id)
	










		

