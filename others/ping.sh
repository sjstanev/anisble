#!/bin/bash

# List of devices
HOST=( "10.81.0.61" "10.81.0.62" "10.81.0.63" "10.81.0.64" )
WAITFOR=1
TIMES=1

# connection check functions
pingtest(){

	ping $myhost -c $TIMES -i $WAITFOR &> /dev/null
	pingReturn=$?
}

# for every device start ping
for myhost in "${HOST[@]}"
	do
		pingtest $myhost
		
			if [ $pingReturn -eq 0 ]; then
				#It works
				echo "Ping to "$myhost "Successed !!!"
				#exit 0
			else
				# No access
				echo "Fail"
				# exit 1
			fi
	done
	