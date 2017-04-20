from collections import OrderedDict

class Address:
	def __init__(self):
		self.tag = 0
		self.index = 0
		self.offset = 0

	def __str__(self):
		return "tag = " + str(self.tag) + " | index = " + str(self.index) + " | offset = " + str(self.offset)

class CacheParameters:	
	def __init__(self):
		self.tagSize = 0
		self.indexSize = 0
		self.offsetSize = 0
		self.cacheSize = 0
		self.blockSize = 0
		self.numBlocks = 0
		self.associativity = 0
		self.numSets = 0
		self.replacement = ''

	def __str__(self):
		return "cacheSize = " + str(self.cacheSize) + " | blockSize = " + str(self.blockSize) + " | numBlocks = " + str(self.numBlocks) + \
		" | associativity = " + str(self.associativity) + " | numSets = " + str(self.numSets)

class CacheTable:
	def __init__(self):
		self.valid = False
		self.tag = 0

class Sets:
	def __init__(self):
		self.blocks = OrderedDict()
