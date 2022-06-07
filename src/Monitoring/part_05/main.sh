mode=$1

if [ "$mode" -eq "1" ]
then
    cat ../part_04/*.log | sort -k 2
fi

if [ "$mode" -eq "2" ]
then
    cat ../part_04/*.log | sort -u -n

fi

if [ "$mode" -eq "3" ]
then
    awk '$2 ~ /^(4|5)[0-9]{2}$/' ../part_04/*.log | sort -k 2
fi

if [ "$mode" -eq "4" ]
then
        awk '$2 ~ /^(4|5)[0-9]{2}$/' ../part_04/*.log | sort -k 2 | sort -u -k 1 -n
fi
