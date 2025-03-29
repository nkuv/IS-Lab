# List File/Directory permissions
ls -l

# Add user permissions
chmod u+rwx sample.py

# Remove user permissions
chmod u-rwx sample.py

# Add group permissions
chmod g+rw sample.py

# Remove group permissions
chmod g-rw sample.py
 
# Add "others" permissions
chmod o+x sample.py

# Remove "others" permissions
chmod o-x sample.py

# Give read, write, and execute to everyone
chmod a+rwx sample.py

# Give only read permission for everyone
chmod a=r sample.py

# Use numeric mode for modifying permissions
chmod 755 sample.py
chmod 644 sample.py
