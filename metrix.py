#! /usr/bin/env python

# Version 0.0
# DTG 20180129.1950

# Import modules
import sys

# Optional modules
import pandas

'''
metrix performs these jobs:

	1) imports a specific set of csv tables into pandas dataframes. The tables are
		downloaded before metrix is invoked. The tables are z.csv and e.csv.
		a) First, an inner join
			i) z.csv :: Daily analysis data from Zacks, updated daily in the morning
				approximately 7,000 records
			ii) e.csv :: Earnings schedule data from Zacks, updated once weekly 
				Up to approximately 2,000 records
			Result: earns01.csv
		b) Second join, a left outer join:
			i) zearns.csv (the left, all records retained)
			ii) w.csv :: A list of symbols having weekly options, updated as needed
				to capture changes
			iii) binary.csv  :: A list of brokerage-recognizable symbols corresponding to 
				binary options on Nadex
			iv) The combined table is reconstructed with flag fields marking symbols 
				having weekly options and symbols used to analyze binary options.
			Result: earns_interim.csv
		c) A manual stage to allow for download of the brokerage data.
			i) metrix Writes the full list of symbols in zearns_interim to file syms.csv
			ii) metrix pauses for manual creation of the market-data table m.csv
			iii) metrix resumed when notified by the operator.		
		c) Third join, a left outer join:
			i) earns_interim.csv (the left, all records retained as an error check)			
			ii) m.csv :: Current market information :: updated as needed, from 
				brokerage ThinkOrSwim
			Result: Earns mmdd-mmdd, where mmdd are the start and end dates of the
				period covered, derived programmatically from the minimum and maximum
				earnings announcements dates in the set. For example, the file for the
				week of Jan. 29 through Feb. 2, 2018 would be styled "Earns 0129-0202".
	2) Analyzes the combined data, restructuring the Earns... table, scoring the
		metrics used for analysis and restructuring the Earns... table to accommodate
		the analytical results, all in csv format. (Details to come.)
	3) Program terminates, and operator uploads it to Google Sheet as input into
		the trading routine.

'''

def main() :
	print "In main()"


# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--
