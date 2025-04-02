#!/bin/bash

# Get the current date in YYYY-MM-DD format
current_date=$(date +"%Y-%m-%d")

# Iterate through all .py and .txt files in the current directory
for file in *.py *.txt; do
    # Check if the file exists to avoid errors if no matching files are found
    if [ -e "$file" ]; then
        # Extract filename without extension and extension separately
        base="${file%.*}"
        ext="${file##*.}"
        
        # Create the new filename with the current date added
        new_name="${base}_${current_date}.${ext}"
        
        # Rename the file
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
    fi
done

echo "Renaming completed."