# List out all users
cat /etc/passwd | cut -d: -f1

# Add a user
sudo useradd mec1

# Assign password to user
sudo passwd mec1

# Access user configuration file
cat /etc/passwd

# Change user login name of a user
sudo usermod -l mec2 mec1

# Delete a user name
sudo userdel mec2
