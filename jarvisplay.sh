#!/usr/bin/env sh

CMD='ssh sermak.xyz -tt ssh jarvis -tt DISPLAY=:0.0 '

$CMD xdotool search \"Mozilla\ Firefox\" | dmenu
#$CMD xdotool search -name "Mozilla Firefox" | dmenu
#xdotool windowactivate $(xdotool search "Mozilla Firefox" | head -1)
#xdotool key space

$CMD firefoxwindows | dmenu

