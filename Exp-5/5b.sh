#!/bin/bash

read -p "Enter username to monitor: " username
while true; do
    if who | grep -qw "^$username"; then
        echo "User $username has logged in."
        exit 0
    else
        echo "Waiting for $username to log in..."
        sleep 30
    fi
done

