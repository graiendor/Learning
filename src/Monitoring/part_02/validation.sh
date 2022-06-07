#!/bin/bash

function validate() {
    validation=0
    if [ $# -ne 4 ]
    then
        validation=1
        size=`expr length "$folders_symbols_list"`
        if [ "$size" -lt "7" ] && [ "$size" -gt "0" ]
        then
            validation=2
            size=`expr length "$file_name"`
            if [ "$size" -lt "7" ] && [ "$size" -gt "0" ]
            then
                validation=3
                size=`expr length "$file_extension"`
                if [ "$size" -lt "3" ] && [ "$size" -gt "0" ]
                then
                    validation=4
                    size=`expr length "$files_size"`
                    if [ "$size" -lt "6" ] && [ "$size" -gt "0" ]
                    then
                        validation=5
                        size=$(( size - 2 ))
                        shopt -s nocasematch
                        if [ "${files_size: $size}" == "mb" ] 
                        shopt -u nocasematch
                        then
                            validation=6
                            files_size=${files_size:0:size}
                            if [ "$files_size" -le "100" ] && [ "$files_size" -ge "0" ]
                            then
                                validation=7
                                files_size+="M"
                            fi
                        fi
                    fi
                fi
            fi
        fi
    fi
}