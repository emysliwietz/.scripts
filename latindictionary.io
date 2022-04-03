#!/usr/bin/env sh

PYCMD=$(cat <<EOF
import latindictionary_io
import json

dictionary = latindictionary_io.Client()

a = json.load(dictionary.analyze_word('canis'))

print(a["mean"])
EOF
)

/usr/bin/env python3 -c "$PYCMD"
