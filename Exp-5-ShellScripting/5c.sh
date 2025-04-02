#!/bin/bash

read -p "Enter filename to deny execution: " filename
if [ -f "$filename" ]; then
    chmod a-x "$filename"
    echo "Execute permission removed for $filename"
fi
