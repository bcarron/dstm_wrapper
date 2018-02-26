#!/usr/bin/env python3

import subprocess
import sys

def restart_miner(proc):
    print('Restarting miner...')
    proc.kill()

def process_line(proc, line):
    if 'cudaMemcpy 1 failed' in line:
        restart_miner(proc)
    else:
        print(line, end='')

if __name__ == '__main__':
    while True:
        proc = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            process_line(proc, line.decode())
