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
file_to_save = os.path.join("Analysis", "election_results.txt")


# Initalize a total vote counter.
total_votes = 0

# Retreive candidate names/option.
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read the header row.
    headers = next(file_reader)


    # Print each row in the CSV file.
    for row in file_reader:
        # Add to total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's count.
        candidate_votes[candidate_name] += 1

# print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# print(winning_candidate_summary)
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Retrieve the votes for each candidate and get the percentages of votes.
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Challenge Formate : vote_percentage = "{:.2f}".format(vote_percentage)
        # Tabulate each candidate's name, vote count, and percentage of # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # Determine winning vote count and candidate.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and percentage to terminal. 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)      
        

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# Print the total votes and candidate name.
# print("Total Votes =", total_votes)
# print("Candidate Names:", candidate_options)
# Print the candidate vote dictionary.
# print("Candidate Total Votes :", candidate_votes)




