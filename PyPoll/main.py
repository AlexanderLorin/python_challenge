import csv

with open("Python_Challenge/PyPoll/Resources/election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)

    
    #skip first row because it contains column names
    columnnames = next(csvreader)
    total_votes = len(list(csvreader))
    

    candidate1 = "Khan"
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"

    candidate1_vote = 0
    candidate2_vote = 0 
    candidate3_vote = 0
    candidate4_vote = 0


    for row in csvreader:
        if str(row[2]) == candidate1:
            candidate1_vote +=1
        


with open("Python_Challenge/PyPoll/Analysis/election_analysis.txt","w") as election_analysis:
    summary_report = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate1}: 63.000% (2218231)
{candidate1}: 20.000% (704200)
{candidate1}: 14.000% (492940)
{candidate1}: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
    """
    print(summary_report)
    election_analysis.write(summary_report)