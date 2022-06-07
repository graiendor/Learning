#!/bin/bash

function validate() {
    validation=0
    if [ $# -ne 7 ]
    then
        validation=1
        if [ -d $path ];
        then
            validation=2
            if [ "$folders_number" -gt "0" ] && [[ $folders_number =~ ^[1-9][0-9]*$ ]]
            then
                validation=3
                size=`expr length "$folders_symbols_list"`
                if [ "$size" -lt "7" ] && [ "$size" -gt "0" ]
                then
                    validation=4
                    if [ "$files_number" -gt "0" ] && [[ $files_number =~ ^[1-9][0-9]*$ ]]
                    then
                        validation=5
                        size=`expr length "$file_name"`
                        if [ "$size" -lt "7" ] && [ "$size" -gt "0" ]
                        then 
                            validation=6
                            size=`expr length "$file_extension"`
                            if [ "$size" -lt "3" ] && [ "$size" -gt "0" ]
                            then
                                validation=7
                                size=`expr length "$files_size"`
                                if [ "$size" -lt "6" ] && [ "$size" -gt "0" ]
                                then
                                    validation=8
                                    size=$(( size - 2 ))
                                    if [ "${files_size: $size}" == "kb" ] 
                                    then
                                        validation=9
                                        files_size=${files_size:0:size}
                                        if [ "$files_size" -le "100" ] && [ "$files_size" -ge "0" ]
                                        then
                                            validation=10
                                            files_size+="K"
                                        fi
                                    fi
                                fi
                            fi
                        fi
                    fi
                fi
            fi
        fi
    fi
}