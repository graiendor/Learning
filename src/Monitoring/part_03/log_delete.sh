#!/bin/bash

log_delete() {
    path=""
    while [ ! -f "$path" ]
    do 
        echo "Enter the path to your log, please:"
        read path
    done
    while read -r line
    do
        sudo rm -rf awk '{print $1}' $line
    done < $path
}
