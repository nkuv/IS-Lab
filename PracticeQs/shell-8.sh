#!/bin/bash

while read line; do
    sudo useradd "$user"
    echo "User added : $user"
done < new.txt