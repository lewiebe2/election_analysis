# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Assign a variable for total votes.
total_votes = 0

# Assign a new list for candidate options.
candidate_options = []

# Assign a new dictionary for candidate names and votes.
candidate_votes = {}

# Assign a variable for the winning candidate.
winning_candidate = ""

# Assign a variable for the winning vote count.
winning_count = 0

#Assign a variable for winning percentage.
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list if the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add name to list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    # Get candidate's name from candidate_votes dict.
    for candidate_name in candidate_votes:
        # Get vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #Calculate percentage of votes each candidate won
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print candidate's name with percentage of total votes. 
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
           #Set candidate's vote count equal to winning_count.
            winning_count = votes
            #Set candidate's percentage equal to winning_percentage.
            winning_percentage = vote_percentage
            #Set winning_candidate to candidate's name.
            winning_candidate = candidate_name
    
    #Print winning candidate summary.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

