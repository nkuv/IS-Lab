#counting words and lines

#!/bin/bash

wc -l example.txt                       # Count lines

wc -w example.txt                       # Count words

wc -c example.txt                       # Count characters

grep -c "st" example.txt                # Count pattern matches