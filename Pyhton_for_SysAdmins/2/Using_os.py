#!/bin/python

from math import pi
import os


print os.getenv('DIGITS')
digits = os.getenv('DIGITS', 10)
print("%.*f" % (int(digits), pi))
