#!/bin/bash

current_hour=$(date +%H)

if [ "$current_hour" -ge 6 ] && [ "$current_hour" -lt 12 ]; then
    sct 6000 
elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 16 ]; then
	sct 4000 

elif [ "$current_hour" -ge 17 ] && [ "$current_hour" -lt 18 ]; then
	sct 3000
else
	sct 2500 
fi

