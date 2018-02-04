#!/usr/bin/env python

# Version 0.0

# DTG 20180204.0000 Initial coding

# Import modules
import sys
import os

# Globals
indir = "./cal"
outfile = "./c.csv"
splitstr = '"Symbol'

def combinefiles(dir,out) :
  files = os.listdir(dir)
  f = 0
  k = 0
  for file in files:
    Fin = open(file,"r")
    Fout = open(file,"w")
    for s = Fin:
      if f == 0:
        if k == 0:
          linea = s.split(splitstr)
          Fout.write(splitstr + linea[1])
          k = k + 1
          f = f + 1
        else:
          if f > 0:
            k > 0;
              Fout.print s
  
  
def main() :
  combinefiles(indir,outfile)


# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--

