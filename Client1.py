from DistributedCache import DistributedCache 
import os

cli1 = DistributedCache(3, 2, '127.0.0.1')
cli1.start_client()


while True:
	print('\n---- Menu ----')
	print('[1] Send message to server')
	print('[2] Check ')
	print('[3] Sair')

	opt = int(input('-> '))

	if opt == 1:
		print("\nType 'exit' to return to options")
		message = input("->")
		while message != 'exit':
			cli1.send_data_to_server(message)
			message = input("->")
	elif opt == 2:
		print("\n---- CACHE INFO ----")
		print(cli1.getCache(1))
		print(cli1.getCache(2))
		print(cli1.getCache(3))
		print(cli1.getCache(4))
	elif opt == 3:
		cli1.send_data_to_server("quit")
		break
		



