#!/bin/bash

date_from=$1
time_from=$2
date_to=$3
time_to=$4
file=$5

date_of_file=`stat -c "%w %n" $file | awk '{print $1}'`
time_of_file=`stat -c "%w %n" $file | awk '{print $2}' | awk -F. '{print $1}'`
if [[ "$date_of_file" > "$date_from" ]] && [[ "$date_of_file" < "$date_to" ]]
then
    echo $date_of_file $time_of_file $file
    rm -rf $file
elif [[ "$date_of_file" == "$date_from" ]] && [[ "$time_of_file" > "$time_from" ]]
then
    echo $date_of_file $time_of_file $file
    rm -rf $file
elif [[ "$date_of_file" == "$date_to" ]] && [[ "$time_of_file" < "$time_to" ]]
then
    echo $date_of_file $time_of_file $file
    rm -rf $file
fi

