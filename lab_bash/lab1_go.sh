#!/bin/bash
# File: lab_bash
# Date: 17:14 9/12/2015
# Description: Running compress95.ss file, changing alu, mult, palu values.

# Deal each para_name and para_value.
deal () {
	para_name=$1
	para_value=$2
	out_file_name="go.$para_name.$para_value"
	#output file
	>/home/yuedeji/simplescalar/benchmark/$out_file_name
	#../simplesim-3.0/sim-outorder -res:$para_name $para_value -redir:sim /home/yuedeji/simplescalar/benchmark/$out_file_name ../benchmark/go.ss 9 9 ../benchmark/go.in
	../simplesim-3.0/sim-outorder -res:$para_name $para_value -redir:sim /home/yuedeji/simplescalar/benchmark/$out_file_name ../benchmark/go.ss 9 9 ../benchmark/go.in
}

# The funtion units name 
argu[1]="ialu"
argu[2]="imult"
argu[3]="memport"
argu[4]="fpalu"
argu[5]="fpmult"
# The different values
value[1]=1
value[2]=2
value[3]=4
value[4]=8
value[5]=16
# Iterate different combinations
for index in 1 2 3 4 5
do
	for v in 1 2 3 4 5
	do
		deal ${argu[$index]} ${value[$v]}
	done
done
