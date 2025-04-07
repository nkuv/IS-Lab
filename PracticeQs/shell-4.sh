#manipulating contents

#!/bin/bash

cut -d' ' -f1 example.txt             # Extract the first word from each line (space as delimiter)

tr 'a-z' 'A-Z' < example.txt          # Convert all lowercase letters to uppercase

sed 's/e/w/g' example.txt             # Replace all 'e' with 'w'

sort example.txt | uniq               # Sort lines and remove duplicates

head -n 2 example.txt                 # Display the first 2 lines of the file