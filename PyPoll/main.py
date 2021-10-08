import csv
vote_count = {}

with open("Resources/election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)

    
    #skip first row because it contains column names
    columnnames = next(csvreader)


    for row in csvreader:
        if row[2] not in vote_count.keys():
            vote_count[row[2]] = 1
        else:
            vote_count[row[2]] += 1



        
candidate_names = list(vote_count.keys())
candidate_votes = list(vote_count.values())
total_votes = sum(list(vote_count.values()))
largest_vote_count = max(candidate_votes)
winning_index = candidate_votes.index(largest_vote_count)
winner = candidate_names[winning_index]

with open("Analysis/election_analysis.txt","w") as election_analysis:
    summary_report = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate_names[0]}: {round(candidate_votes[0]/total_votes*100,2)}% ({candidate_votes[0]})
{candidate_names[1]}: {round(candidate_votes[1]/total_votes*100,2)}% ({candidate_votes[1]})
{candidate_names[2]}: {round(candidate_votes[2]/total_votes*100,2)}% ({candidate_votes[2]})
{candidate_names[3]}: {round(candidate_votes[3]/total_votes*100,2)}% ({candidate_votes[3]})
-------------------------
Winner: {winner}
-------------------------
    """
    print(summary_report)
    election_analysis.write(summary_report)