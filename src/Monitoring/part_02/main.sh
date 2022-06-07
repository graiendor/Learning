source validation.sh
source creation.sh

START="$(date +%s%N)"

folders_symbols_list=$1
files_symbols_list=$2
files_size=$3

ok="false"

space_edge=1000000

file_name=`echo $files_symbols_list | awk -F. '{print $1}'`
file_extension=`echo $files_symbols_list | awk -F. '{print $2}'`

echo "-- Validating input --"

validate

if [ $validation -eq 7 ]
then
    path=`ls --hide=bin --hide=sbin -d /*/ | sort --random-sort | head -1`

    echo "-- The randomly-selected folder is: $path --";
    space_left=`df -k / | awk 'NR == 2 {print $4}'`
    while [ "$space_left" -ge "$space_edge" ]
    do
        create
    done
    echo "-- There is no space left --"
else
    case $validation in
        0) echo 'Invalid number of arguments';;
        1) echo 'Invalid length of symbols in folder symbols';;
        2) echo 'Invalid length of symbols in file name symbols';;
        3) echo 'Invalid length of symbols in file extension symbols';;
        4) echo 'Invalid size of files';;
        5) echo 'Incorrect type of size';;
        6) echo 'Incorrect size';;
    esac
fi

