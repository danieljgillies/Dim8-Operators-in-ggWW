#!/bin/bash
# Iterate over every file in the directory
for file in *; do
    # Check if it is a file (not a directory)
    if [ -f "$file" ]; then
        # Rename the file with 'mll' prepended to its name
        mv "$file" "mll_$file"
    fi
done