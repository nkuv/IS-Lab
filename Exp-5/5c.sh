#!/bin/bash

read -p "Enter the path of the file to block execution: " filepath

if [ -f "$filepath" ]; then
    chmod a-x "$filepath"
    echo "Execute permission removed for $filepath."
else
    echo "Error: File not found."
fi
