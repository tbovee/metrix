#! /usr/bin/env python

# Import modules
import sys
import pandas as pd
import numpy as np

# Zacks object constants
zacksfile = "z.csv"
# zackscolnames = "Ticker" : "Sym", "Next EPS Rerpot Date" : "Date", "# of Analysts in Q0 Consensus" : "Analysts","Estimate Q0" : "EstQ0","Earnings ESP" : "ESP", "Zacks Rank" : "Rank"
# zackscoldel = "Avg Volume","Market Cap","Optionable","Compare"

class DataBox(datafile, colname, coldel):
  # Holds DataFrame and associated attributes and tools.
   
  def ___init___():
    self.Datafile = datafile
    Acquire()
  
  def Acquire():
  	# Check for the existence of the file, abort if not found
  	self.Datatable = pd.read_csv(self.Datafile,header=1)
  	

def Calcscores():
    quantiles = 5
    return Zacks.Datafiles(q=0.5, axis=0)


def main():

  Zacks = DataBox(zacksfile,zackscolfixes,zackscoldeletes)
  
  print Calscores()

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--
