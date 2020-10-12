# Election_Analysis
## Project Overview
Elections analysis using python.  Using election results contained in a .CSV file we used a Python program to determine the number and percentage of votes for each candidate, the winning candidate and the county vote totals.  Results are displayed on screen and printed to a file.

## Resources
Data source election_results.csv
Software, Python 3.7 64 bit

## Summary of Results
With a total of 3sults69,711 votes cast, the results of the election are verified to be as follows.  Diana DeGette was the winner of the election with 73.8% of the vote.  The county with the highest turnout was Denver, with 306,055 votes.

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest county: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------


## Election Audit Summary
The included election audit program can be used to provide similar analysis to other elections.  For elections tracked at the county level no changes are needed, provided that the .CSV file is provided in the same format.  If the format is different, then the column markers would need to be changed in the program to corresond to the format of the file.  

For Elections at the state or precint level, the county designators in the program would need to be changed to correspond to the particular election parameters.  The program is not limited to a specific number of candidates or geographic designators.
