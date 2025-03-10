#!/bin/bash

# Demonstrate fork, exec, getpid, exit, wait, close, stat, opendir, readdir

# 1. fork + exec: Run a command in a child process
echo "Parent PID: $$"
( echo "Child PID: $BASHPID"; exec ls / ) &  # Child forks, then execs 'ls /'
child_pid=$!
echo "Child process started with PID: $child_pid"

# 2. wait: Wait for child process to finish
wait $child_pid
echo "Child process $child_pid exited."

# 3. getpid: Show current PID
echo "Current PID: $$"

# 4. stat: Get file status
echo "Stat of /etc/passwd:"
stat /etc/passwd

# 5. opendir + readdir: List directory contents
echo "Files in /tmp:"
for file in /tmp/*; do
    echo "$file"
done

# 6. close: Open and close a file descriptor
exec 3>test.txt        # Open FD 3
echo "Hello World" >&3  # Write to FD 3
exec 3>&-              # Close FD 3
echo "Closed FD 3."

# 7. exit
exit 0
