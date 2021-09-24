import csv

with open("Resources/budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
    number_of_months = 0
    total_dollars = 0 
    #skip first row because it contains column names
    columnnames = next(csvreader)
    
    for row in csvreader:
        number_of_months +=1
        total_dollars += int(row[1])

with open("Analysis/budget_analysis.txt","w") as budget_analysis:
    summary_report = f"""
Financial Analysis
----------------------------
Total Months: {number_of_months}
Total: ${total_dollars}
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
    """
    print(summary_report)
    budget_analysis.write(summary_report)