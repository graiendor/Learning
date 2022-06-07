#!/bin/bash

function create()
{
    echo "" > log.txt
    count=1
    dir_name=$folders_symbols_list
    size=`expr length "$dir_name"`
    while [ $size -lt "4" ]
    do
        dir_name+=$folders_symbols_list
        size+=$size
    done
    while [ "$count" -le "$folders_number" ]
    do
        dir_name+=${folders_symbols_list: -1}
        final_path=$path$dir_name
        mkdir -p $final_path
        __create_files__
        count=$(( count + 1 ))
    done
}

function __create_files__() {
    file_name=`echo $files_symbols_list | awk -F. '{print $1}'`
    files_count=1
    while [ "$files_count" -le "$files_number" ]
    do
        size=`expr length "$file_name"`
        if [ "$size" -gt "240" ]
        then 
            file_name=`echo $files_symbols_list | awk -F. '{print $1}'`
            file_name+=${file_name: 0}
        fi
        current_date=`date +"%d_%m_%y"`
        file_name+=${file_name: -1}
        fact_name=$file_name$current_date.$file_extension
        space_left=`df -k / | awk 'NR == 2 {print $4}'`
        if [ "$space_left" -lt "1000000" ]
        then
            break
        else
            sudo fallocate -l $files_size $final_path/$fact_name
            date_for_log=`date +"%d_%m_%y_%T"`
            echo "$final_path/$fact_name $date_for_log $files_size" >> log.txt
            files_count=$(( files_count + 1 ))
        fi
    done
}