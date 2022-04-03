#!/bin/sh

# Import the colors
. "${HOME}/.cache/wal/colors.sh"

dmenu -i -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Source Code Sans Semibold-15" -p "$1"

