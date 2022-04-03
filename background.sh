#!/bin/bash

if (($# != 2)); then
    echo "Tool to change the wallpaper
Usage:
    $0 [desktop] [n/p/s]
    (next/previous/stay)
    Example to cycle the wallpaper of the first desktop to the next one:
    $0 1 n
"
    exit
fi

#apod

WALLPAPERDIR=~/nextcloud/wallpapers

if ! [ -f /tmp/backgrounds ]; then
    #fdupes -rdI $WALLPAPERDIR
    (ls $WALLPAPERDIR | grep -v apod) > /tmp/backgrounds
#    (ls $WALLPAPERDIR/apod | sed 's/^/apod\//') >> /tmp/backgrounds
    sort -R /tmp/backgrounds > /tmp/backgrounds2
    cat /tmp/backgrounds2 > /tmp/backgrounds
    rm /tmp/backgrounds2
fi

num=$(wc -l /tmp/backgrounds | awk '{print $1}')

if ! [ -f /tmp/.currentwallpaper ]; then
    fn=$(( ( RANDOM % num )  + 1 ))
    sn=$(( ( RANDOM % num )  + 1 ))
    echo "$fn
$sn" > /tmp/.currentwallpaper
fi

bgn1=$(sed "1q;d" /tmp/.currentwallpaper)
bgn2=$(sed "2q;d" /tmp/.currentwallpaper)

if [ "$2" != "s" ]; then
    if [ "$1" = "1" ]; then
	if [ "$2" = "n" ]; then
	    bgn1=$(((bgn1 + 1) % num))
	else
	    bgn1=$(((bgn1 - 1) % num))
	    if [ $bgn1 -lt 1 ]; then
		bgn1=$num
	    fi
	fi
    else
	if [ "$2" = "n" ]; then
	    bgn2=$(((bgn2 + 1) % num))
	else
	    bgn2=$(((bgn2 - 1) % num))
	    if [ $bgn2 -lt 1 ]; then
		bgn2=$num
	    fi
	fi
    fi
fi

echo "$bgn1
$bgn2" > /tmp/.currentwallpaper

bg1=$(sed "$bgn1""q;d" /tmp/backgrounds)
bg2=$(sed "$bgn2""q;d" /tmp/backgrounds)

cd ~/nextcloud/wallpapers/ || exit

feh --bg-fill "$bg1" "$bg2" #&& sleep 5 && feh --bg-fill /tmp/wallpaper.jpg /tmp/wallpaper2.jpg

xrdb -merge ~/.Xresources
