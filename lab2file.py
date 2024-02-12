#!/usr/bin/env python3
import sys

def print_script_and_variables():
    print("Script name:", sys.argv[0])
    if len(sys.argv) > 1:
        print("Variables:", sys.argv[1:])
        print("Script and Variables:", ' '.join(sys.argv))

if __name__ == "__main__":
    print_script_and_variables()

