from DistributedCache import DistributedCache 

serv1 = DistributedCache(3, 2, '127.0.0.1')
serv1.start_server()

serv1.read_data_from_server()
