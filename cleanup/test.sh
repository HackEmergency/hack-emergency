#!/bin/bash
./cleanup/tugboat_template.sh >> ~/.tugboat
test_running=$(tugboat droplets | grep test)
if [[ "$test_running" != "" ]] 
	then
	tugboat destroy test -c
	#sleep 180
fi