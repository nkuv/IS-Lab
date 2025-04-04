#Write a Bash script to rename all .py and .txt files in the current directory by appending the 
#current date (YYYY-MM-DD) to their filenames while preserving extensions.

#!/bin/bash

current_date=$(date +"%Y-%m-%d")

for file in *.py *.txt; do
    if [ -e "$file" ]; then
        base="${file%.*}"
        ext="${file##*.}"
        
        new_name="${base}_${current_date}.${ext}"
        
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
    fi
done