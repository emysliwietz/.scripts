#!/usr/bin/env bash

LANG=$1
case "$LANG" in
    "de")
        BIBLE="menge"
        ;;
    "en")
        BIBLE="kjv"
        ;;
    "la")
        BIBLE="vul"
        ;;
    "gr")
        BIBLE="grb"
        ;;
    *)
        BIBLE="kjv"
        ;;
esac

R=$(((RANDOM + 1) % 150))

echo "Psalm $R:"
eval "PAGER='cat' $BIBLE -W Psa $R" |
    awk '{ $1=""; print}' |
    sed '1d;s/^[[:space:]]*//;s/$//;s/<em>/(/g;s/<\/em>/)/g' |
    fold -s -w 80
