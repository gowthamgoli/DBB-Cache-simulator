#!/bin/bash
# run_simulator.sh filename cachesize blocksize associativity replacement_policy 
python2 ./DBB/vm.py "$1" 
python2 ./Cache_Simulator/cachesim_dbb.py $1.bb $1.trace $2 $3 $4 $5