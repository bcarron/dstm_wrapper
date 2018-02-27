#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os
import logging

def restart_miner(proc):
    logging.info('Restarting miner...')
    proc.kill()

def process_line(args, proc, line):
    if 'cudaMemcpy 1 failed' in line:
        restart_miner(proc)
    if args.reboot and 'cudaGetDeviceCount failed' in line:
        logging.info('Restarting system...')
        os.system('reboot')
    else:
        logging.info(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Restart dstm's miner when an overclocking error is detected")
    parser.add_argument('-c', '--launch-command', default='./zm --cfg-file zm.cfg', help="the command used to launch dstm's miner")
    parser.add_argument('-l', '--logfile', default='zm_wrapper.log', help="the path to the log file") 
    parser.add_argument('-r', '--reboot', action='store_true', help="restart the machine if a 'cudaGetDeviceCount failed' error is encountered (requires root privileges)")
    args = parser.parse_args()

    logging.basicConfig(filename=args.logfile, level=logging.INFO, format='%(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())
   
    while True:
        proc = subprocess.Popen(args.launch_command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            process_line(args, proc, line.decode().strip('\n'))
