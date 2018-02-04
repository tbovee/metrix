#! /usr/bin/env python

# Version 1.0 

# DTG 20180204.1315 v. 1.0 Working standalone version
#  Next step: Make it work as an importable module
# DTG 20180204.xxxx v. 0.0 Initial commit

# Import modules
import sys
import os

# Globals
DEBUG = 1

indir = "./cal/"
outfile = "./c.csv"
splitstr = '"Symbol'


def combinefiles(dir,out) :
  files = os.listdir(dir)
  f = 0
  k = 0
  for file in files:
    if DEBUG == 1:
      print "Processing " + file
    Fin = open(indir + file,"r")
    Fout = open(outfile,"w")
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

