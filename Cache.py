# OrderedDict is the best data structure for LRU implementation
from collections import OrderedDict
import time

class Cache:
	""" 
		Local cache for storing data considering 
		the least recently used algorithm
	"""
	def __init__(self, size=3, time_expire=2):
		self.size = size
		self.time_expire = time_expire
		self.cache = OrderedDict()
		self.lru = None

	# put data inside the cache
	def putData(self, data):
		t = time.time()

		# check whether the data is new
		if data.id not in self.cache:
			self.cache[data.id] = (data, t)
		# if data is already in cache, return a message	
		else:
			print("Data ({},{}) is already in cache".format(data.id, data.value))

		if self.lru is None:
			self.lru = data.id
		# check whether the cache size was exceeded
		if len(self.cache) > self.size:
			# if yes remove the least recently used
			del self.cache[self.lru]
			self.lru = list(self.cache.keys())[0]
	# get the data from the cache by id
	def getData(self, id):
		if id in self.cache:
			data, t = self.cache[id]
			return data.value
		else:
			return 'id {} is not in cache'.format(id)
	# remove the expired data
	def expired(self):
		if len(self.cache) == 0:
			return
		lru_t = self.cache[self.lru][1]
		
		while time.time() - lru_t > self.time_expire:
			if len(self.cache) == 1:
				del self.cache[self.lru]
				self.lru = None
				return
			del self.cache[self.lru]
			self.lru = list(self.cache.keys())[1]
			lru_t = self.cache[self.lru][1]
