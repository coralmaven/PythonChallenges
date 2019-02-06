import os
import csv
import string
import pdb

with open('Resources/election_data.csv', newline='') as electionData:
    csvreader = csv.reader(electionData, delimiter=',')
    csv_header = next(csvreader) # Skip the header
    
    votingData = []
    totalVotes = 0
    
    for row in csvreader:
        votingData.append(row[2])
        totalVotes += 1
            
    candidates = []  # names 
    votes = []       # votes
    
    for c in votingData:
        if c in candidates:
            idx = candidates.index(c)
            votes[idx] += 1
        else:
            candidates.append(c)
            votes.append(1)
            
# The percentage of votes each candidate won
percentVotes = [round(vote*100/totalVotes,3) for vote in votes] 
            
print(" Election Results")
print(" -------------------------")
print(" Total Votes: %d" % totalVotes)
print(" -------------------------")
for candidate, vote, percentVote in zip(candidates, votes, percentVotes):
    print(f' {candidate}: {percentVote:0.3f}% ({vote})')
    
print(" -------------------------")
# The winner of the election based on popular vote.
winner = candidates[votes.index(max(votes))]
print(f' Winner: {winner.title()}')
print(" -------------------------")

