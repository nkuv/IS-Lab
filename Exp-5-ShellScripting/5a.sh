#!/bin/bash

i=1
for f in *; do
    [ -f "$f" ] && echo "$i. $f - $(date -r "$f" "+%Y-%m-%d")"
    ((i++))
done