source log_delete.sh
source date_time_input.sh
source date_validation.sh

echo "Delete files:"
select choice in "- By log file" "- By date and time" "- By name mask" "- Exit"
do
    case $choice in
        "- By log file") 

        echo "You've selected delete by logging" 
        log_delete
        ;;
        "- By date and time") 
        echo "You've selected delete by date and time"
        date_time_input
        find / -type f -exec bash date_delete.sh $date_from $time_from $date_to $time_to {} \; 
        ;;
        "- By name mask") 
        echo "You've selected delete by name mask"
        echo "Please, enter the search mask:"
        read mask
        sudo find / -type f -name $mask -delete
        ;;
        "- Exit") exit 0;;
        *) echo 'Try again, I believe in you'
    esac
done

