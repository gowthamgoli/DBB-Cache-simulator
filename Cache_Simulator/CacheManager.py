from random import randint
class CacheManger:
	hits = 0
	misses = 0

	def start(self, sets, request, params):
		if self.isPresentInCache(sets, request):
			self.hits += 1
			if params.replacement == 'L':
				del sets[request.index].blocks[request.tag]
				sets[request.index].blocks[request.tag] = True
		else:
			self.misses += 1
			#print "Cache miss"
			self.insertIntoCache(sets, request, params)

	def isPresentInCache(self, sets, request):
		#print sets[request.index].blocks
		if request.tag in sets[request.index].blocks:
			#print "Cache hit occured at set index " + str(request.index) + " and tag = "+ str(request.tag)
			return True
		#print "Cache Miss occured for set index " + str(request.index) + " for tag "+ str(request.tag)
		return False

	def insertIntoCache(self, sets, request, params):
		#if len(sets[request.index].blocks) < params.associativity:
		#	print "Inserted into Cache at set index " + str(request.index) + " and tag = "+ str(request.tag)
		if len(sets[request.index].blocks) == params.associativity:
			#print "No place found ---- replace"
			self.replaceBlock(sets, request, params)
		#print ""
		sets[request.index].blocks[request.tag] = True

	def replaceBlock(self, sets, request, params):
		if params.replacement == 'R':
			replaceInd = randint(0, params.associativity-1)
			#print "Replaced set Index " + str(request.index) + " block " + str(replaceInd)
			del sets[request.index].blocks[sets[request.index].blocks.keys()[replaceInd]]
			#sets[request.index].blocks[request.tag] = True
		if params.replacement == 'L':
			#print "Replaced set Index " + str(request.index) + " block first"
			sets[request.index].blocks.popitem(last=False)




