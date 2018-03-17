#! /usr/bin/env python

# Version 1.1 

# DTG 20180317.1541 def procfile() to process a single file into a list, reworked combinefiles() 
#   to confirm. 
# DTG 20180308.1522 Added an option to def combinefiles that directs quote removal;
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

#indir = "./cal/"
#outfile = "./c.csv"

ALL = 1
STRINGS = 2
NONE = 0

quotes = NONE

def quotestocommas(s) : 
  s = s.replace('","','|')
  s = s.replace('"','')
  s = s.replace(',','')
  s = s.replace('|',',')
  return s

def trunc(f)
  f.open(outfile,"w")
  f.truncate()
  f.close()

def procfile(dir,file,quotes,filnum)
  k = 0
  output = []  
  Fin = open(dir + file,"r")
  for s in Fin:
    s = s.strip() + "\n"
    if f == 0:
      s = s[3:]
      if (quotes == ALL) : 
        s = quotestocommas(s)
      output.append(s)
    else:
      if (quotes == ALL) :
        s = quotestocommas(s)
        output.append(s)
      else:
        if k > 0:
          if (quotes == ALL) :
            s = quotestocommas(s)
            output.append(s)
    k = k + 1
  Fin.close()
  return output

def combinefiles(dir,out,quotes) :
  files = os.listdir(dir)
  f = 0
  Fout = open(outfile,"w")
  for file in files:
    Fout.write(procfile(out,ALL))
    f = f + 1
  Fout.close()
  
def main() :
  combinefiles(indir,outfile,ALL)


# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--

