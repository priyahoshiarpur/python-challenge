import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')


# define variables 
total_votes = 0
#created an empty dictionary
candidates = {}

# Read the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Count the votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Add candidate to the dictionary if it is not present in candidates
        if candidate not in candidates:
            candidates[candidate] = 0

        candidates[candidate] += 1

# percentage of votes can be calulated by doing following
#intialize max votes as 0
max_votes = 0
#result empty list
results = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Sorting the results by the number of votes in descending order
results.sort(key=lambda x: x[1], reverse=True)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
