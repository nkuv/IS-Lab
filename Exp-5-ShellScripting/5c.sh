#!/bin/bash

read -p "Enter filepath to deny execution: " filepath
if [ -f "$filepath" ]; then
    chmod a-x "$filepath"
    echo "Execute permission removed for $filepath"
fi
