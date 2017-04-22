import sys
from classes import *
from helpers import *
from CacheManager_DBB import *
#from CacheManagerOld import *
from collections import OrderedDict

def main():
	
	params = CacheParameters()
	request = Address()
	cacheManager = CacheManger_DBB()
	dbb = Blocks()
	#cacheManagerOld = CacheMangerOld()

	blocksFile = sys.argv[1]
	traceFile = sys.argv[2]
	params.cacheSize = int(sys.argv[3])
	params.blockSize = int(sys.argv[4])
	params.associativity = int(sys.argv[5])
	params.replacement = sys.argv[6]
	params.numBlocks = params.cacheSize/params.blockSize
	params.numSets = params.numBlocks/params.associativity


	addressStream = []
	with open(blocksFile) as f:
		for line in f:
			tokens = line.strip().split()
			dbb.sizes[int(tokens[0])] = int(tokens[1])
	print dbb.sizes
	print ''
	
	with open(traceFile) as f:
		content = f.readlines()
	content = [int(x.strip('\n')) for x in content]

	for i in range(0, len(content)-1):
		currAddress = content[i]
		nextAddress = content[i+1]
		if currAddress not in dbb.cfg:
			dbb.cfg[currAddress] = {nextAddress:1}
		else:
			if nextAddress not in dbb.cfg[currAddress]:
				dbb.cfg[currAddress][nextAddress] = 1
			else:
				dbb.cfg[currAddress][nextAddress] += 1
	print dbb.cfg
	print ''

	for address in dbb.cfg:
		sumEdges = 0
		for neighbor in dbb.cfg[address]:
			sumEdges += dbb.cfg[address][neighbor]
		lastRange = 0
		for neighbor in dbb.cfg[address]:
			temp = 1.0*dbb.cfg[address][neighbor]/sumEdges
			dbb.cfg[address][neighbor] = (lastRange, lastRange + temp)
			lastRange = 1.0*temp

	print dbb.cfg
	print ''

	for i in range(0, len(content)):
		addressStream.append(content[i])
		for x in range(1, dbb.sizes[content[i]]/4):
			addressStream.append(content[i]+4*x)

	#for a in addressStream:
	#	print a


	#print inputFile, params.cacheSize, params.blockSize, params.associativity, params.numBlocks, params.numSets

	cache = [[CacheTable() for j in range(params.associativity)] for i in range(params.numSets)]
	
	sets = [Sets() for i in range(params.numSets)]
	#cacheManager.replacement = params.replacement

	getParamSizes(params)
	print params
	print ''
	#print params.tagSize, params.indexSize, params.offsetSize




	prevAdress = 0
	
	for address in addressStream:
		#print line
		currAddress = address
		getParamsOfAddress(currAddress, request, params)
		cacheManager.start(sets, currAddress, request, params, dbb)
		#cacheManagerOld.start(cache, request)
		#print bin(currAddress)[2:]
		#print request.offset, request.index, request.tag
		#print ''
		#prevAdress = currAddress
		#for x in sets:
		#	print x.blocks
		print ''

	print cacheManager.hits, cacheManager.misses 
	#print cacheManagerOld.hits, cacheManagerOld.misses

if __name__ == '__main__':
	main()