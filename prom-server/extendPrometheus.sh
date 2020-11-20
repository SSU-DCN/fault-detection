#!/bin/bash
  
# turn on bash's job control
set -m
  
# Start the primary process and put it in the background
python3 server.py  --filesd /etc/prometheus/targets.json --alertfile /etc/prometheus/alert-rule.yml &
  
# Start the helper process
prometheus $1

