#!/bin/sh

pgrep -x dmenu && exit

choice=$(echo "pound->kg kg->pound MB/s->Mbps Mbps->MB/s inch->cm cm->inch foot->cm cm->foot mile->km km->mile" | tr ' ' '\n' | sort | dmenu -i -p "Convert") || exit 1

if [ "$choice" = "pound->kg"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a/2.205)")
    res=$(echo "$b" | dmenu_color.sh)
elif [ "$choice" = "kg->pound"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a*2.205)")
    res=$(echo "$b" | dmenu_color.sh)
    
elif [ "$choice" = "MB/s->Mbps"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a*8)")
    res=$(echo "$b" | dmenu_color.sh)
elif [ "$choice" = "Mbps->MB/s"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a/8)")
    res=$(echo "$b" | dmenu_color.sh)
    
elif [ "$choice" = "inch->cm"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a*2.54)")
    res=$(echo "$b" | dmenu_color.sh)
elif [ "$choice" = "cm->inch"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a/2.54)")
    res=$(echo "$b" | dmenu_color.sh)

elif [ "$choice" = "foot->cm"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a*30.48)")
    res=$(echo "$b" | dmenu_color.sh)
elif [ "$choice" = "cm->foot"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a/30.48)")
    res=$(echo "$b" | dmenu_color.sh)

elif [ "$choice" = "mile->km"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a*1.609)")
    res=$(echo "$b" | dmenu_color.sh)
elif [ "$choice" = "km->mile"  ]; then
    a=$(echo "" | dmenu_color.sh)
    b=$(python -c "print($a/1.609)")
    res=$(echo "$b" | dmenu_color.sh)

fi

    
echo $res | xclip -selection clipboard
echo $res | xclip
