#PyPoll election_date | Alanis Perez Mod 3 Challenge
import os
import csv
csvpath = os.path.join("Resources","election_data.csv")

print("Election Results")
print("--------------------------------------------")

# The total number of votes cast per candidate including percentage & vote count
total_votes = 0
candidates = set() #NOT = [] because there would be many duplicates, this is a set not a listwith open(csvpath, 'r') as file:
candidate_votes = {} #dict to store votes per candidate
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  #skip header
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        candidates.add(candidate) #add NOT append because it's a set not a list
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
print(f"Total Votes: {total_votes}")

print("--------------------------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes) *100
    print(f"{candidate}: {percentage:.2f}%, ({votes} votes)")

print("--------------------------------------------")

# The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")

print("--------------------------------------------")

# Export results to a text file
output_file = os.path.join("analysis", "election_data_output.txt")
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("--------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------------------------\n")
    file.write(f"{candidate}: {percentage:.2f}%, ({votes} votes)\n")
    file.write("--------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------------------------------\n")