#!/usr/bin/env bash

#Overclocking
. /mining/oc.sh

#Start mining
python3 /mining/zm/start.py --launch-command '/mining/zm/zm --cfg-file=/mining/zm/zm.cfg --log=/mining/zm/zm.log' --log '/mining/zm/zm_wrapper.log'
