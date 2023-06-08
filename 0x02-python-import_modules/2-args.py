#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
        for i in range(1, len(sys.argv)-1):
            print(f"{i}: {sys.argv[i]}")
