#! /usr/bin/env python

# Version 1.1 

# DTG 20180308.15.22 Added an option to def combinefiles that directs quote removal;
#  Added supporting globals ALL, STRINGS, None and var quotes
# DTG 20180218.1023 v1.1: Fixed errors that left extraneous characters
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

ALL = 1
STRINGS = 2
NONE = 0

quotes = NONE

def quotestobars(s) : 
  s = s.replace('","','|')
  s = s.replace('"','')
  s = s.replace(',','')
  s = s.replace('|',',')
  return s

def combinefiles(dir,out,quotes) :
  files = os.listdir(dir)
  f = 0
  k = 0
  Fout = open(outfile,"w")
  for file in files:
    Fin = open(indir + file,"r")
    for s in Fin:
      s = s.strip() + "\n"
      if f == 0:
        if k == 0:
          s = s[3:]
          if (quotes == ALL) : 
            s = quotestobars(s)
          Fout.write(s)
        else:
          if (quotes == ALL) :
            s = quotestobars(s)
          Fout.write(s)
      else:
        if k > 0:
          if (quotes == ALL) :
            s = quotestobars(s)
            Fout.write(s)
      k = k + 1
    Fin.close()
    f = f + 1
    k = 0
  #Fout.write("\n")
  Fout.close()
  
def main() :
  combinefiles(indir,outfile,ALL)


# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--

