#!/usr/bin/env python3

import sys

# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print("Here is your flag:")
print("".join(bytes.fromhex(ords).decode()))
