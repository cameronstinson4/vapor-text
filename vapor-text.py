#!/usr/bin/env python

import sys

result = ''

for word in sys.argv[1:]:
    result += " "
    for c in word:
        result += c.upper() + " "

print(result)