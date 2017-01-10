#! /usr/bin/env python
from sys import argv
import sys

year = int(sys.argv[1])
print(year)
re1 = year % 400
re2 = (year % 4)
re3 = (year % 100)
if re1 == 0 or re2 == 0 and re3 != 0:
	print(str(year) + "is leap year")
else:
	print(str(year) + "is not leap year")

