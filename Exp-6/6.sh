#!/bin/bash

echo "Parent PID: $$"
( echo "Child PID: $BASHPID"; exec ls / ) & child_pid=$!
echo "Child started: $child_pid"

wait $child_pid && echo "Child $child_pid exited."
stat /etc/passwd

echo -e "\nFiles in /tmp:"; ls /tmp

exec 3>test.txt && echo "Hello World" >&3 && exec 3>&-
echo "Closed FD 3."
exit 0