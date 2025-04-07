#searching words in a file

#!/bin/bash

grep "manage" example.txt                  # Basic search for the word "manage"

grep -i "calls" example.txt                # Case-insensitive search for the word "calls"

grep -n "file" example.txt                 # Show line numbers for matches with "file"

grep -c "em" example.txt                   # Count lines that contain "em"
