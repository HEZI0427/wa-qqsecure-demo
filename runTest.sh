#!/bin/bash
env

which python38
r="$?"
which python3.8
rp="$?"
c="python3"
if [[ "$r" == '0' ]]; then
    c="python38"
elif [[ "$rp" == '0' ]]; then
    c="python3.8"
fi
$c main.py --mode=3