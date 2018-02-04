#! /usr/bin/env python

# Version 1.01 

# DTG 20180204.1405 v1.01 Fixed an error that zeroed outfile for each infile
# DTG 20180204.1315 v1.00 Working standalone version
#  Next step: Make it work as an importable module
# DTG 20180204.xxxx v0.00 Initial commit

# Import modules
import sys
import os

# Globals
DEBUG = 0

indir = "./cal/"
outfile = "./c.csv"
splitstr = '"Symbol'


def combinefiles(dir,out) :
  files = os.listdir(dir)
  f = 0
  k = 0
  Fout = open(outfile,"w")
  for file in files:
    Fin = open(indir + file,"r")
    for s in Fin:
      if f == 0:
        if k == 0:
          linea = s.split(splitstr)
          Fout.write(str(f) + ": " + str(k) + ": " + file + " :: " + splitstr + linea[1])
      k = k + 1

      if k > 0:
        Fout.write(s)
    Fin.close()
    f = f + 1
    k = 0
  Fout.close()
  
def main() :
  combinefiles(indir,outfile)


# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--

