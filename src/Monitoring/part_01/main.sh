source validation.sh
source creation.sh

path=$1
folders_number=$2
folders_symbols_list=$3
files_number=$4
files_symbols_list=$5
files_size=$6

file_name=`echo $files_symbols_list | awk -F. '{print $1}'`
file_extension=`echo $files_symbols_list | awk -F. '{print $2}'`

validate

if [ $validation -eq 10 ]
then
    echo 'Success'
    create
else
    case $validation in
        0) echo 'Invalid number of arguments';;
        1) echo 'No such directory';;
        2) echo 'Invalid number of folders';;
        3) echo 'Invalid length of symbols in folder symbols';;
        4) echo 'Invalid number of files';;
        5) echo 'Invalid length of symbols in file name symbols';;
        6) echo 'Invalid length of symbols in file extension symbols';;
        7) echo 'Invalid size of files';;
        8) echo 'Incorrect type of size';;
        9) echo 'Incorrect size';;
    esac
fi

