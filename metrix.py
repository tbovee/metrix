#! /usr/bin/env python

# Version 0.0

# DTG 20180203.1605 Completed field lists except for Analyze object
# DTG 20180203.1215 
#	Removed Syms object as not needed.
#	Added AnalyzeBox class, structure of the Analyze object
# DTG 20180203.0700 Added TableMarket object
# DTG 20180202.1225 Added the data file class and defined the input file objects
#   for the 1st run; next step is to define the output file objects.Q: How do I override
#   a method defined in the class?
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

# Calendar object contants
calendarfile = "c.csv"
earnscolnames = "Symbol" : "Sym"
earnscoldel = "Company","Market Cap(M)","Estimate","Reported","ESP","PriceChange"

# Zacks object constants
zacksfile = "z.csv"
zackscolnames = "Ticker" : "Sym", "Next EPS Rerpot Date" : "Date", "# of Analysts in Q0 Consensus" : "Analysts","Estimate Q0" : "EstQ0","Earnings ESP" : "ESP", "Zacks Rank" : "Rank"
zackscoldel = "Avg Volume","Market Cap","Optionable","Compare"

# Market object constants
marketfile = "m.csv"
marketcolname = "Market Cap" : "Market Cap", "Impl Vol" : "IV","IV_Percentile" : "IVR","FisherTransform" : "FT"
marketcoldel = []

# Weeklys object constants :: Needs column label "Sym", added manually
weeklysfile  = "weeklys.csv"
weeklyscolname = []
weeklycoldel = []

# Analyze object constants
colscore = []
filestub = "Earns "
 
def pausehere()
  # Code that pauses while Market externality is created.

class DataBox(datafile, colname, coldel):
  # Holds DataFrame and associated attributes and tools.
   
  def ___init___():
    self.Datafile = datafile
    self.Datafile = datapath + self.Datafile
    self.Acquire()
    self.Delcols()
    self.Namecols()
  
  def Acquire():
  	# Check for the existence of the file, abort if not found
  	self.Datatable = pd.read_csv(self.Datafile,header=1)
  	
  def Namecols():
  	if colname.empty == True:
  	  pass
  	else:
      self.Datatable.rename(index=str, columns={ colname } )
    	
  def Delcols():
    if colname.empty == True:
      pass
    else:
      self.Datatable.drop(columns=[coldel])
      pass  
    	

class AnalyzeBox()
  # Joins table into a single datastructure, \analyzes
  # the data, and makes a judgment of each symbol: analyze-dopt and pass-dopt for
  #   directional optons, analyze-nopt and pass-nopt, for direction neutral optons, 
  #   and analyze-shr and pass-shr for shares, all of which are long plays.
  
  def ___init___:
    pass
    
  def Joindata():
    pass
    
  def Annotations():
    pass
    
  def Insertcols(): # if needed for new columns; do in join if possible
    pass
    
  def Percentile(colscore, inverse)
  	pass
  	
  def Calcscores()
    # Sums (or averages) the colscore columns TBD
    # For each scorecol:
    #  percentile(col, inverse) range 0.00 to 1.00
    #  write percentile to appropriate score column
    pass
    
  def Gateclosed(gate):
    if gate == 1:
      return 1
    else:
      return 0  
      
  def Options():
     return [weeklys] #column	  
	
  def Decision():
    if self.Gateclosed(gate):
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
