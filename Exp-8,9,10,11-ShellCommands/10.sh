# Retrieve and display ACL(Access Control List) entries.
getfacl sample.py

# Modify ACL
setfacl -m u:mec:rwx sample.py
setfacl -m g:mecgroup:r-- sample.py
setfacl -x u:mec sample.py
setfacl -b sample.py