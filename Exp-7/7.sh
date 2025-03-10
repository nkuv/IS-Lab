#!/bin/bash
exec 3< input.txt
exec 4> output.txt             
while IFS= read -r line <&3; 
  do echo "$line" >&4; 
done
exec 3<&- 4>&-             
