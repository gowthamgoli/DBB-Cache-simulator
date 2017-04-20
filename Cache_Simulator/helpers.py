import math
#from classes import *

def createMask(a, b):
	r = 0
	for i in range(a,b+1):
		r |= 1 << i;
	return r;

def getParamsOfAddress(currAddress, request, params):
	'''print bin(currAddress)[2:]
	mask = ((1 << params.offsetSize) - 1) << 0
	print bin(mask)
	request.offset = mask & currAddress
	mask = ((1 << params.indexSize) - 1) << params.offsetSize
	print bin(mask)
	request.index = mask & currAddress
	mask = ((1 << params.tagSize) - 1) << (params.offsetSize+params.indexSize)
	print bin(mask)
	request.tag = mask & currAddress'''
	x = bin(currAddress)[2:]
	#print str(currAddress) + ' : '+ x
	#print x[-params.offsetSize:]
	request.offset = int(x[-params.offsetSize:],2)
	#print x[-(params.offsetSize+params.indexSize):-params.offsetSize]
	if params.indexSize > 0:
		request.index = int(x[-(params.offsetSize+params.indexSize):-params.offsetSize],2)
	#print x[-(params.offsetSize+params.indexSize+params.tagSize):-(params.offsetSize+params.indexSize)]
	if params.tagSize > 0:
		request.tag = int(x[-(params.offsetSize+params.indexSize+params.tagSize):-(params.offsetSize+params.indexSize)],2)
	#print request
	#print request.offset

def getParamSizes(params):
	#print params.numSets
	params.indexSize = int(math.log(params.numSets,2))
	params.offsetSize = int(math.log(params.blockSize,2))
	params.tagSize = 32 - (params.indexSize + params.offsetSize)
