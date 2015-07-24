#!/bin/bash
./tugboat_template.sh >> ~/.tugboat
test_running=$(tugboat droplets | grep test)
if [[ "$test_running" != "" ]] 
	then
	tugboat destroy test
	sleep 180
fi