#!/bin/bash



function validate_date {
    date_regular="^20[0-9]{2}-((0(1|3|5|7)|1(0|2))-((0|1)[0-9]|2[0-9]|3[0-1])|(0(4|6|9)|11)-((0|1)[0-9]|2[0-9]|30)|02-((0|1)[0-9]|2[0-8]))$"
    if [[ "$date_from" =~ $date_regular ]] && [[ "$date_to" =~ $date_regular ]]
    then
        date_valid=1
    fi
    time_regular="^((0|1)[0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9]$"
    if [[ "$time_from" =~ $time_regular ]] && [[ "$time_to" =~ $time_regular ]]
    then
        time_valid=1
    fi
}

validate_date