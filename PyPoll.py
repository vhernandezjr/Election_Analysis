#The data file needed.
#Get the total votes for each candidate.
#Names of all the candidates.
#Percentage of votes for each candidate.
#Total number of votes per candidate.
#Winner of the election based on popular vote.
# Import the datetime class from the datetime module.


import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)



    # Read and print the header row.
    headers = next(file_reader)
    print(headers)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")

