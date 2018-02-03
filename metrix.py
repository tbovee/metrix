#! /usr/bin/env python

# Version 0.0

# DTG 20180203.1215 
#	Removed Syms object as not needed.
#	Added AnalyzeBox class, structure of the Analyze object
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

# Analyze object constants
scorecols = []
filestub = "Earns "
 
def pausehere()
  # Code that pauses while Market externality is created.

class DataBox(datafile, colrename, coldelete):
  # Holds DataFrame and associated attributes and tools.
   
  def ___init___():
    self.Datafile = datafile
    self.Datafile = datapath + self.Datafile
    self.Colfixes = colfixes
    self.Acquire()
    self.Colrename()
  
  def Acquire():
  	# Check for the existence of the file, abort if not found
  	self.Datatable = pd.read_csv(self.Datafile,header=1)
  	
  def Colrename():
  	if colfixes.empty == True:
  	  pass
  	else:
      self.Datatable.columns = self.Colfixes
    	
  def Coldelete():
    if colrename.empty == True:
      pass
    else:
      # Do the deletions
      pass  
    	

class AnalyzeBox()
  # Joins table into a single datastructure, \analyzes
  # the data, and makes a judgment of each symbol: analyze-dopt and pass-dopt for
  #   directional optons, analyze-nopt and pass-nopt, for direction neutral optons, 
  #   and analyze-shr and pass-shr for shares, all of which are long plays.
  
  def ___init___:
    pass
    
  def joindata():
    pass
    
  def annotations():
    pass
    
  def insertcols(): # if needed for new columns; do in join if possible
    pass
    
  def percentile(col, inverse)
  	pass
  	
  def calcscores()
    # Sums (or averages) the score columns TBD
    # For each scorecol:
    #  percentile(col, inverse) range 0.00 to 1.00
    #  write percentile to appropriate score column
    pass
    
  def gateclosed(gate):
    if gate == 1:
      return 1
    else:
      return 0  
      
  def options():
     return [weeklys] #column	  
	
  def decision():
    if gateclosed(gate):
    	dec = "pass_"options() == 1:
    	pass
         
def main():

  TableEarns = DataBox(earnsfile,earnscolfixes,earnscoldeletes)
  TableZacks = DataBox(zacksfile,zackscolfixes,zackscoldeletes)
  pausehere()
  TableMarket = DataBox(marketfile,[1,"syms"],marketcoldeletes)
  TableWeeklys = Databox(weeklysfile,[],[])
  Analyze = AnalyzeBox()

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--
