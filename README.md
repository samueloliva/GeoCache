# GeoCache
Geo Distributed LRU cache


# Usage:
```python

serv1 = DistributedCache(3, 2, '127.0.0.1')
serv1.start_server()

cli1 = DistributedCache(3, 2, '127.0.0.1')
cli1.start_client()

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

```
