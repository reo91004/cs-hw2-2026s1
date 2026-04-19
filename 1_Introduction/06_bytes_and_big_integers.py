#!/usr/bin/env python3

import sys
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

print("Here is your flag:")
print(long_to_bytes(n).decode())
