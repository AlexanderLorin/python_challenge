import csv

with open("Python_Challenge/PyBank/Resources/budget_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
    number_of_months = 0
    total_dollars = 0 
    max_change_value = 0
    min_change_value = 0
    #skip first row because it contains column names
    columnnames = next(csvreader)
   
    
    for row in csvreader:

        #count number of months
        number_of_months +=1
        #sum profit/losses
        total_dollars += int(row[1])
        #find average of profit/loss
        average_change = total_dollars/number_of_months
        #find max change value and the month
        if max_change_value < int(row[1]):
            max_change_value = int(row[1])
            max_change_month = (row[0])
        #find min change value and the month
        if min_change_value > int(row[1]):
            min_change_value = int(row[1])
            min_change_month = (row[0])            


            
with open("Python_Challenge/PyBank/Analysis/budget_analysis.txt","w") as budget_analysis:
    summary_report = f"""
Financial Analysis
----------------------------
Total Months: {number_of_months}
Total: ${total_dollars}
Average  Change: ${average_change}
Greatest Increase in Profits: {max_change_month} {max_change_value}
Greatest Decrease in Profits: {min_change_month} {min_change_value}
    """
    print(summary_report)
    budget_analysis.write(summary_report)
