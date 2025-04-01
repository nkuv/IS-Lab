#!/bin/bash

hash_db="hashes.txt" 

create_hashes() {
    sha256sum * > "$hash_db"
}

check_files() {
    sha256sum -c "$hash_db" 
}

case $1 in
    create) create_hashes ;;
    check)  check_files ;;
esac


# ./5d.sh create     # Generate hashes
# ./5d.sh check      # Verify file integrity
# hashes.txt is output file
