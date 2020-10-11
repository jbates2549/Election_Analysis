# 1. data we need to retrieve
# 2. total number of votes cast
# 3. list of candidates who received votes
# 4. percentage of votes each candidate won
# 5. total number of votes each candidate won
# 6. winner of election based on popular vote

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
#with open(file_to_load) as election_data:

     # To do: perform analysis.
 #    print(election_data)
# Open the election results and read the file.
#file_to_load = 'Resources/election_results.csv'


import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")

file_to_load = 'c:/Users/jbate/OneDrive/Desktop/Analysis_Projects/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("c:/users/jbate/OneDrive/Desktop/Analysis_Projects/Election_Analysis/analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)



