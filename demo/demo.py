#!/usr/bin/env python3

import fileinput
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import ppp_spell_checker


if __name__ == "__main__":
    corrector = ppp_spell_checker.StringCorrector('en')
    while(True):
        print(corrector.correctString(input("")))
