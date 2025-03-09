#!/bin/bash

dir="."
count=1

echo "Serial | Filename           |     Creation Date"
echo "-----------------------------------------------"

for file in "$dir"/*; do
    filename=$(basename "$file")
    creation_date=$(stat -c "%w" "$file" 2>/dev/null || stat -c "%y" "$file")
    creation_date=$(echo "$creation_date" | cut -d '.' -f1)
    printf "%-6s | %-16s | %s\n" "$count" "$filename" "$creation_date"
    count=$((count+1))
done
