#!/usr/bin/env sh

while true
do
    curl mysliwietz.de 2>/dev/null | grep 301 1>/dev/null || continue
    #ping mysliwietz.de 2> /dev/null || continue
    sshfs -f -o ConnectTimeout=3,ConnectionAttempts=1,ServerAliveInterval=5,ServerAliveCountMax=3 "$@"
    echo "disconnected from" "$@"
    sleep 3
    echo "retry" "$@" "..."
done
