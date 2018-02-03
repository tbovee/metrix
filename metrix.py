#! /usr/bin/env python

# Version 0.0

# DTG 20180203.0700 Added TableMarket object
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
calendarfile = "calendar.csv"
earnscolfixes = []

# Zacks object constants
zacksfile = "zacks.csv"
zackscolfixes = []

# Market object constants
marketfile = "market.csv"
marketcolfixes = []

# Weeklys object constants
weeklysfile  = "weeklys.csv"
weeklyscolfixes = []

# Syms object constants :: IS THIS REALLY NEEDED??
 symsfile = "syms.csv"
 symscolfixes = []
 
def pausehere()
  # Code that pauses while Market externality is created.

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
    
def main():

  TableEarns = DataBox(earnsfile,earnscolfixes)
  TableZacks = DataBox(zacksfile,zackscolfixes)
  pausehere()
  TableMarket = DataBox(marketfile,[])
  TableWeeklys = Databox(weeklysfile,[])
  TableSyms = Databox(symsfile,[])
	

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--
