#!/bin/bash

hash_file="hash.txt"

sha256sum * > "$hash_file"
cat "$hash_file"

while true; do
    sha256sum -c "$hash_file"
    for i in {1..30}; do
        echo  -ne "next check in $((30-i))\r"
        sleep 1
    done
done

