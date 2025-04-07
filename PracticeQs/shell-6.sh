#backing up files

#!/bin/bash

file="example.txt"
backup="${file}.bak_$(date +%Y-%m-%d)"
cp "$file" "$backup"
echo "Backed up $file to $backup"

