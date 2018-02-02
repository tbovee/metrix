#! /usr/bin/env python

# Version 0.0
# DTG 20180202.1225 Added the data file class and defined the input file objects
  for the 1st run; next step is to define the output file objects.Q: How do I override
  a method defined in the class?
# DTG 20180129.1950 template created
# See Documentation.txt for an explanation of metrix.py

# Import modules
import sys

# Optional modules
import pandas as pd
import numpy as np

# File constants
fsep = "/"
datapath = "." + fsep + "data" + fsep

# Earns object contants
earnsfile = "e.csv"
earnscolfixes = []

# Zacks object constants
zacksfile = "z.csv"
zackscolfixes = []

# Weeklys object constants
weeklysfile  = "weeklys.csv"
weeklyscolfixes = []

# Syms object constants
 symsfile = "syms.csv"
 symscolfixes = []
 
class DataBox(datafile, colfixes):
  # Holds DataFrame and associated attributes and tools.
   
  def ___init___():
    self.Datafile = datafile
    self.Datafile = datapath + self.Datafile
    self.Colfixes = colfixes
    self.Acquire()
    self.Fixcols()
  
  def Acquire():
  	# Check for the existence of the file, abort if not found
  	self.Datatable = pd.read_csv(self.Datafile,header=1)
  	
  def Fixcols():
  	if colfixes.empty == True:
  		pass
  	else:
    	self.Datatable.columns = self.Colfixes
    
TableEarns = DataBox(earnsfile,earnscolfixes)
TableZacks = DataBox(zacksfile,zackscolfixes)
TableWeeklys = Databox(weeklysfile,[])
Tablesyms = Databox(symsfile,[])





def main() :
  print "In main()"
	

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--
