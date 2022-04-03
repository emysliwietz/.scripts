#!/bin/bash

if [[ -z $2 ]]; then
	echo level full-speed | sudo tee /proc/acpi/ibm/fan
else
	echo "level $2" | sudo tee /proc/acpi/ibm/fan
fi

for (( i=0; i<$1; i++ ))
do
	echo $i
	sleep 1
done
echo level auto | sudo tee /proc/acpi/ibm/fan
