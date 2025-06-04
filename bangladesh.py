#!/bin/python3

import sys

ascii_letter_start = 65
ascii_letter_end = 90 + 1 # Add 1 because range is exclusive on the high end.

start_letter = None
if len(sys.argv) == 2:
    stop_letter = sys.argv[1].upper()
elif len(sys.argv) == 3:
    start_letter = sys.argv[1].upper()
    stop_letter = sys.argv[2].upper()

for i in range(ascii_letter_start, ascii_letter_end):
    if start_letter:
        if chr(i) < start_letter:
            continue
    if chr(i) == stop_letter:
        break
    print(chr(i))
