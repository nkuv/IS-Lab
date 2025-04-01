#!/bin/bash

HASH_FILE="hashes.txt"

create_hash() {
    echo "Generating hashes..."
    find . -type f -not -name "$HASH_FILE" -exec sha256sum {} \; > "$HASH_FILE"
    echo "Hashes saved to $HASH_FILE."
}

check_integrity() {
    echo "Checking integrity..."
    if [ ! -f "$HASH_FILE" ]; then
        echo "Error: Hash file not found. Run the script in create mode first."
        exit 1
    fi

    sha256sum -c "$HASH_FILE" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "All files are unchanged."
    else
        echo "WARNING: Some files have been modified!"
    fi
}

case "$1" in
    create) create_hash ;;
    check) check_integrity ;;
    *) echo "Usage: $0 [create|check]"; exit 1 ;;
esac

