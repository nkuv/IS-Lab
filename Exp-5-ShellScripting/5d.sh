#!/bin/bash

echo "Creating hashes..."
sha256sum * > hashes.txt

cat hashes.txt
sleep 2

echo "Verifying files...."
sha256sum -c hashes.txt

