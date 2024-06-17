#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#Import Modules
import os
import csv

# path to file
csvpath = os.path.join('Resources','election_data.csv')

# open the csv	
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)

	#variables
	total_votes = 0
	candidates = []
	vote_count = []
	vote_percent = []
	winner = ""
	winner_count = 0
	
	#main loop
	for row in csvreader:
		total_votes += 1
		if row[2] not in candidates:
			candidates.append(row[2])
			vote_count.append(1)
		else:
			vote_count[candidates.index(row[2])] += 1

	#calculate vote percentages
	for votes in vote_count:
		vote_percent.append(votes / total_votes * 100)

	#find the winner
	winner_count = max(vote_count)
	winner = candidates[vote_count.index(winner_count)]
	
	#Results
	print("Election Results")
	print("--------------------------")
	print(f"Total Votes: {total_votes}")
	print("--------------------------")
	for x in range(len(candidates)):
		print(f"{candidates[x]}: {vote_percent[x]:.3f}% ({vote_count[x]})")
	print("--------------------------")
	print(f"Winner: {winner}")
	print("--------------------------")

#Output to text file
os.makedirs('Analysis', exist_ok=True)
output_path = os.path.join('Analysis','election_results.txt')
with open(output_path, 'w') as file:
	file.write("Election Results\n")
	file.write("--------------------------\n")
	file.write(f"Total Votes: {total_votes}\n")
	file.write("--------------------------\n")
	for x in range(len(candidates)):
		file.write(f"{candidates[x]}: {vote_percent[x]:.3f}% ({vote_count[x]})\n")
	file.write("--------------------------\n")
	file.write(f"Winner: {winner}\n")
	file.write("--------------------------\n")

