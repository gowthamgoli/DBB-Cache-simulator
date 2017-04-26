#!/bin/bash
python cachesim.py big.txt 1024 32 4 F > output/out1.txt
python cachesim.py big.txt 2048 32 4 F > output/out2.txt
python cachesim.py big.txt 4096 32 4 F > output/out3.txt
python cachesim.py big.txt 8192 32 4 F > output/out4.txt
python cachesim.py big.txt 16384 32 4 F > output/out5.txt
python cachesim.py big.txt 32768 32 4 F > output/out6.txt
python cachesim.py big.txt 65536 32 4 F > output/out7.txt

#python cachesim.py big.txt 8192 1 4 F > output/out8.txt
python cachesim.py big.txt 8192 2 4 F > output/out9.txt
python cachesim.py big.txt 8192 4 4 F > output/out10.txt
python cachesim.py big.txt 8192 8 4 F > output/out11.txt
python cachesim.py big.txt 8192 16 4 F > output/out12.txt
python cachesim.py big.txt 8192 32 4 F > output/out13.txt
python cachesim.py big.txt 8192 64 4 F > output/out14.txt

python cachesim.py big.txt 8192 32 1 F> output/out15.txt
python cachesim.py big.txt 8192 32 2 F > output/out16.txt
python cachesim.py big.txt 8192 32 4 F > output/out17.txt
python cachesim.py big.txt 8192 32 8 F > output/out18.txt
python cachesim.py big.txt 8192 32 16 F > output/out19.txt
python cachesim.py big.txt 8192 32 32 F > output/out20.txt
python cachesim.py big.txt 8192 32 64 F > output/out21.txt
python cachesim.py big.txt 8192 32 128 F > output/out22.txt
python cachesim.py big.txt 8192 32 256 F > output/out23.txt
