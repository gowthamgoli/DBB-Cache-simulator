from random import randint
class CacheMangerOld:
	hits = 0
	misses = 0
	#replacement = 0

	def start(self, cache, request):
		if self.isPresentInCache(cache, request):
			self.hits += 1
			#print "Cache hit"
		else:
			self.misses += 1
			#print "Cache miss"
			self.insertIntoCache(cache, request)

	def isPresentInCache(self, cache, request):
		#print len(cache)
		for i in range(0, len(cache[0])):
			if cache[request.index][i].valid and cache[request.index][i].tag == request.tag:
				print "Cache hit occured at set index " + str(request.index) + " and block " + str(i) + " = tag "+ str(request.tag)
				return True
		print "Cache Miss occured for set index " + str(request.index) + " for tag "+ str(request.tag)
		return False

	def insertIntoCache(self, cache, request):
		associativity = len(cache[0])
		for i in range(0, associativity):
			if not cache[request.index][i].valid:
				print "Inserted into Cache at set index " + str(request.index) + " and block " + str(i) + " = tag "+ str(request.tag)
				cache[request.index][i].valid = True
				cache[request.index][i].tag = request.tag
				return
		print "No place found ---- replace"
		replaceInd = randint(0,associativity-1)
		print "Replaced set Index " + str(request.index) + " block " + str(replaceInd)
		cache[request.index][replaceInd].tag = request.tag
