#!/bin/bash
./cleanup/tugboat_template.sh >> ~/.tugboat
test_running=$(tugboat droplets | grep staging)
if [[ "$test_running" != "" ]] 
	then
	tugboat destroy staging -c
	#sleep 180
fi