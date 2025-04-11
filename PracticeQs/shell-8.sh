#!/bin/bash

while read user; do
    if id "$user" &>/dev/null; then
        echo "$user already exists"
    else 
        sudo useradd "$user"
        echo "User added : $user"
    fi
done < new.txt