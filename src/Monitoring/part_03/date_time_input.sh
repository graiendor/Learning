#!/bin/bash

function date_time_input() {
        date_valid=0
        time_valid=0
        while [ "$date_valid" -ne "1" ] || [ "$time_valid" -ne "1" ]
        do
            date_valid=0
            time_valid=0
            echo "Enter the FROM date as YYYY-MM-DD:"
            read date_from
            echo "Enter the FROM time as HH:MM:SS"
            read time_from
            echo "Enter the TO date as YYYY-MM-DD:"
            read date_to
            echo "Enter the TO time as HH:MM:SS"
            read time_to
            validate_date
            echo $date_valid $time_valid
        done
}