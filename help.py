#!/usr/bin/env python3

##
## EPITECH PROJECT, 2019
## 107TRANSFER_2019
## File description:
## 107transfer
##

from __future__ import print_function
from fractions import Fraction
from sys import argv, exit
from math import pow, exp, factorial, sqrt, ceil, pi
from time import time

lishelp = "USAGE\n\
    /206neutrinos n a h sd\n\n\
DESCRIPTION\n\
    n\tnumber of values\n\
    a\tarithmetic mean\n\
    h\tharmonic mean\n\
    sd\tstandard deviation"

if len(argv) == 1:
    exit(84)

if len(argv) == 2 and argv[1] == "-h":
    print(lishelp)
    exit(0)

if len(argv) < 5 and len(argv) > 5:
    exit(84)

try:
    int(argv[1])
    int(argv[2])
    int(argv[3])
    int(argv[4])
except(ValueError):
    exit(84)

if int(argv[1]) < 0:
    exit(84)