#Import libraries
import csv
import os

#Establish path of current script
file_dir = os.path.dirname(os.path.realpath(__file__))

#Establish path of resource file
with open(os.path.join(file_dir, 'Resources/budget_data.csv'),'r') as bd_file:
    
    #Skip headers
    heading = next(bd_file)
    #Read file
    csvreader=csv.reader(bd_file)
    
    #Initialize variables
    total=0
    row_count=0
    chngs_array=[]
    chngs_array_drvd=[]
    chngs_array_dts=[]
    chngs_array_dts_drvd=[]
    chngs_total=0
    gretaest_increase=0
    greatest_decrease=0
    
    #Loop through file, extract totals, count of rows and populate auxiliary arrays
    for row in csvreader:
        total=total+float(row[1])
        row_count=row_count+1
        chngs_array.append(float(row[1]))
        chngs_array_dts.append(row[0])
    
    #Loop through one auxiliary array to calculate changes
    for rs in range(len(chngs_array)):
        if rs<len(chngs_array)-1:
            chngs_total=chngs_total+(chngs_array[rs]-chngs_array[rs+1])
            chngs_array_drvd.append(-1*(chngs_array[rs]-chngs_array[rs+1]))
            chngs_array_dts_drvd.append(chngs_array_dts[rs+1])

    #Loop through another auxiliary array to get max and min values
    for rsd in range(len(chngs_array_drvd)):
        if chngs_array_drvd[rsd]>gretaest_increase:
            gretaest_increase=chngs_array_drvd[rsd]
            greatest_increase_date=chngs_array_dts_drvd[rsd]
        if chngs_array_drvd[rsd]<greatest_decrease:
            greatest_decrease=chngs_array_drvd[rsd]
            greatest_decrease_date=chngs_array_dts_drvd[rsd]

    #Print results to console
    print("\nFinancial Analysis\n")
    print("---------------------------------\n")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total}")
    print(f"Average change: ${round(chngs_total/(row_count-1),2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${gretaest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

    #Write results to text file
    with open(os.path.join(file_dir, 'Resources/budget_data_results.txt'), 'w') as new_file:
        new_file.write("\nFinancial Analysis\n")
        new_file.write("---------------------------------")
        new_file.write("\nTotal Months: "+str(row_count))
        new_file.write("\nTotal: $"+str(total))
        new_file.write("\nAverage change: $"+str(round(chngs_total/(row_count-1),2)))
        new_file.write("\nGreatest Increase in Profits: "+str(greatest_increase_date)+" $"+str(gretaest_increase))
        new_file.write("\nGreatest Increase in Profits: "+str(greatest_decrease_date)+" $"+str(greatest_decrease))
