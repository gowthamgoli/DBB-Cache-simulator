#!/bin/bash
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 16 8 2 L > output_primes/out1.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 32 8 2 L > output_primes/out2.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 2 L > output_primes/out3.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 128 8 2 L > output_primes/out4.txt

python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 4 2 L > output_primes/out5.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 2 L > output_primes/out6.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 16 2 L > output_primes/out7.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 32 2 L > output_primes/out8.txt

python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 1 L > output_primes/out9.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 2 L > output_primes/out10.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 4 L > output_primes/out11.txt
python cachesim_dbb.py primes_sieve.vm.bb primes_sieve.vm.trace 64 8 8 L > output_primes/out12.txt