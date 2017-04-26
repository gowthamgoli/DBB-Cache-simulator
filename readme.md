# readme for code cache simulator #

The code cache simulator can be run by the following command on a given .vm program

./run_simulator.sh [filename] [cacheSize] [blockSize] [associativity] [replacementPolicy]

## filename ##
This is the pseudo-x86 program on which runs and based on which the code cache is tested
### Valid options: ### 
primes_sieve.vm
primes.vm
compute.vm
fact.vm
fib.vm
jsr_other.vm
loop.vm
nop.vm
stack_bench.vm

## cacheSize ##
Size of the cache in bytes
### Valid options: ###
2
4
8
16
32
64
128
256
512

Note: cache size must always be smaller than the size of the program for legitimate results. Each instruction in the program is considered to be 4 bytes

## blockSize ##
Size of each block in bytes
### Valid options: ###
2
4
8
16
32
64
128
256
512

Note: block size must always be smaller than cache size

## associativity ##
The n-way set associativity of the cache
### Valid options: ###
greater than 1, but less than or equal to blockSize, and a power of two

## replacementPolicy ##
The replacement policy used by the cache simulator
### Valid options: ###
F - Flush When Full
L - Least Recently Used
R - Random
C - Custom policy based on DBB CFG edge profiling (Look Ahead and Insert)

## output ##
Initially, the output to the terminal is whatever the program being run does. This is followed by the results of our code cache simulation, which are shown as follows:

total number of distinct blocks = __  
total number of blocks executed = __  
replacement policy = __  
number of times code cache accessed = __  
code cache miss rate = __  
code cache hit rate = __  
total number of blocks evacuated from cache = __ 
------------------------------------------------------------------------------------------------------
To experiment with a larger address space, use the following command:
./run_big.sh cachesize blocksize associativity replacement_policy

## Valid values ##

## Cache size ##
1024-65536 bytes (powers of 2)

## Block size ##
2-64 bytes (powers of 2)

## Associativity ##
1-256 (powers of 2)
