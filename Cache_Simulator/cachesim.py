import sys
from classes import *
from helpers import *
from CacheManager import *
from CacheManagerOld import *

def main():
	
	params = CacheParameters()
	request = Address()
	cacheManager = CacheMangerOld()
	#cacheManagerOld = CacheMangerOld()

	inputFile = sys.argv[1]
	params.cacheSize = int(sys.argv[2])
	params.blockSize = int(sys.argv[3])
	params.associativity = int(sys.argv[4])
	params.replacement = sys.argv[5]
	params.numBlocks = params.cacheSize/params.blockSize
	params.numSets = params.numBlocks/params.associativity

	#print inputFile, params.cacheSize, params.blockSize, params.associativity, params.numBlocks, params.numSets

	cache = [[CacheTable() for j in range(params.associativity)] for i in range(params.numSets)]
	
	sets = [Sets() for i in range(params.numSets)]
	#cacheManager.replacement = params.replacement

	getParamSizes(params)
	print params
	print ''
	print params.tagSize, params.indexSize, params.offsetSize

	#currAddress = 123879438
	#getParamsOfAddress(currAddress, request, params)
	#print request.offset, request.index, request.tag



	prevAdress = 0
	with open(inputFile) as f:
		for line in f:
			#print line
			currAddress = prevAdress + int(line.strip())
			getParamsOfAddress(currAddress, request, params)
			cacheManager.start(sets, request, params)
			#cacheManagerOld.start(cache, request)
			#print bin(currAddress)[2:]
			#print request.offset, request.index, request.tag
			#print ''
			prevAdress = currAddress
			#for x in sets:
			#	print x.blocks
			#print ''

	print cacheManager.hits, cacheManager.misses, 1.0*cacheManager.hits/(cacheManager.hits+cacheManager.misses)
	#print cacheManagerOld.hits, cacheManagerOld.misses

if __name__ == '__main__':
	main()