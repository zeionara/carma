#!/bin/bash

ROOT="$1"
SUFFIX="$2"

if [ -z "$ROOT" ]; then
    echo 'root directory must be defined'
    exit 1
fi

if [ -z "$SUFFIX" ]; then
    echo 'suffix must be defined'
    exit 1
fi

for file in "$ROOT"/*; do
    extension=$(echo $file | rev | cut -d . -f 1 | rev)
    no_extension=$(echo $file | rev | cut -d . -f2- | rev)

    mv "$file" "$no_extension.$SUFFIX.$extension"
done
