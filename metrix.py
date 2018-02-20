#! /usr/bin/env python

# Version 0.0

# DTG 20180220.1440
# DTG 20180218.1812 Debugging handling of comma-quote delimited source files
# DTG 20180217.1705 Debugging obj DataBox.delcols
#   The column names in the drop() command aren't recognized, although they
#   visually match between the variable and the .csv file. I am commenting 
#    the function out for now and shall pick it up later. Likewise the namecols()
#    function.
# DTG 20180217.1338 Fixing .csv data files
# DTG 20180217.1253 Debugging objects and instantiations
# DTG 20180217.0722 Debugging 
# DTG 20180215.1845 Splits data saving into proc filetable(); comments out Analysis
#	for tetng purposes
# DTG 20180213.1620 Finished def Gateclosed; sketched def Calcscores
# DTG 20180209.1918 Began work on Analyzebox.perentile()
# DTG 20180209.1852 Completed Joindata() in Analyzebox
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
import pandas as pd
import numpy as np

# File constants
fsep = "/"
datapath = "." + fsep + "data" + fsep

# Calendar object contants
calendarfile = "c.csv"
calendarcolnames = '"Symbol" : "Sym"'
calendarcoldel = "Company","Market Cap(M)","Estimate","Reported","ESP","PriceChange"

# Zacks object constants
zacksfile = "z.csv"
zackscolnames = {"Ticker" : "Sym", "Next EPS Rerpot Date" : "Date", "# of Analysts in Q0 Consensus" : "Analysts","Estimate Q0" : "EstQ0","Earnings ESP" : "ESP", "Zacks Rank" : "Rank"}
zackscoldel = "Avg Volume","Market Cap","Optionable","Compare"

# Market object constants
marketfile = "m.csv"
marketcolname = {"Market Cap" : "Market Cap", "Impl Vol" : "IV","IV_Percentile" : "IVR","FisherTransform" : "FT"}
marketcoldel = []

# Weeklys object constants :: Needs column label "Sym", added manually
weeklysfile  = "weeklys.csv"
weeklyscolname = []
weeklycoldel = []

# Create a single table, constants
Finaltable = pd.DataFrame()

# Analyze object constants
colscore = []
gateclosed = 1
gateopen = 0


# Filetable procedure constants
filestub = "Earns"
 
def pausehere():
  # Code that pauses while Market externality is created.
  pass

class DataBox():
# Holds DataFrame and associated attributes and tools.
   
  def __init__(self, datafile, colname, coldel):
    self.Datafile = datafile
    self.Datafile = datapath + self.Datafile
    self.Acquire()
    self.Delcols(colname,coldel)
    self.Namecols(colname)
  
  def Acquire(self):
    # Check for the existence of the file, abort if not found
    self.Datatable = pd.read_csv(self.Datafile, header=1)
    Filetable()
    sys.exit()

  def Namecols(self,colname):
    if colname == {}:
  	  pass
    else:
      self.Datatable.rename(index=str, columns={ colname })
     
  def Delcols(self,colname,coldel):
    if colname == ():
      pass
    else:
      self.Datatable.drop(coldel, axis='columns')
    	
# Create a single table


def Joindata(c,z):
  Interimtable = pd.merge(c.Datatable, z.Datatable, how='inner', on='Syms')
  Finaltable = pd.merge(self.Interimtable, Weeklys.Datatable, how='outer', on='Syms')
        
def Filetable():
  Finaltable.to_csv(datapath + "out.csv")
	
def CombineBox():
  Joindata(c, z)
  Filetable()

      	
'''
class AnalyzeBox()
  # Joins table into a single datastructure, \analyzes
  # the data, and makes a judgment of each symbol: analyze-dopt and pass-dopt for
  #   directional optons, analyze-nopt and pass-nopt, for direction neutral optons, 
  #   and analyze-shr and pass-shr for shares, all of which are long plays.
  
  def Calcscores(dframe)
    # Calculates a quintile for each scorable column
    # Scorable columns: esp, rank, iv, ivp, fishertrans, beta, analysts
    quantiles = 5
    return dframe(q=0.5, axis=0)
    # What sort of return? ]
    # How do I pass to drame? 
    # How do I put an item's quantile in a column in the same table?
    
    pass
    
  def Gateclosed(gate):
  	# gates: weeklys, FTtrend, FTesp
    if gate == 1:
      return gateclosed
    else:
      return gateopen  
      
  def Options():
     return [weeklys] #column	  
	
  def Decision():
    if self.Gateclosed(gate):
    	dec = "pass_"options() == 1:
    	pass
'''

def main():

  Calendar = DataBox(calendarfile, calendarcolnames, calendarcoldel)
  Zacks = DataBox(zacksfile,zackscolnames,zackscoldel)
  #pausehere
  Market = DataBox(marketfile,[1,"syms"],marketcoldel)
  Weeklys = DataBox(weeklysfile,[],[])
  CombineBox(Calendar, Zacks)
# Analyze = AnalyzeBox()

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--














