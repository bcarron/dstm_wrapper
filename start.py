#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

def restart_miner(proc):
    print('Restarting miner...')
    proc.kill()

def process_line(args, proc, line):
    if 'cudaMemcpy 1 failed' in line:
        restart_miner(proc)
    if args.reboot and 'cudaGetDeviceCount failed' in line:
        print('Restarting system...')
        os.system('reboot')
    else:
        print(line, end='')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Restart dstm's miner when an overclocking error is detected")
    parser.add_argument('-l', '--launch_command', default='./zm --cfg-file zm.cfg', help="the command used to launch dstm's miner")
    parser.add_argument('-r', '--reboot', action='store_true', help="restart the machine if a 'cudaGetDeviceCount failed' error is encountered (requires root privileges)")
    args = parser.parse_args()
    
    while True:
        proc = subprocess.Popen(args.launch_command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            process_line(args, proc, line.decode())
