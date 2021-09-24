import csv

with open("Resources/election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
 
    #skip first row because it contains column names
    columnnames = next(csvreader)
    
    for row in csvreader:
        pass

with open("Analysis/election_analysis.txt","w") as election_analysis:
    summary_report = f"""
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
    """
    print(summary_report)
    election_analysis.write(summary_report)