#!/usr/bin/env bash
OC_SCRIPT=/mining/oc.sh
ZM_DIR=/mining/zm

#Overclocking
. $OC_SCRIPT

#Start mining
cd $ZM_DIR
python3 start.py --reboot
