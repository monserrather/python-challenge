#Import libraries
import csv
import os
from collections import Counter

#Establish path of current script
file_dir = os.path.dirname(os.path.realpath(__file__))

#Establish path of resource file
with open(os.path.join(file_dir, 'Resources/election_data.csv'),'r') as bd_file:
    
    #Skip headers
    heading = next(bd_file)

    #Read file
    csvreader=csv.reader(bd_file)

    #Initialize variables
    row_count=0
    candidate_list=[]
    candidate_distinct_list=set()
    winner=0

    #Final arrays
    candidate_count=[]
    candidate_name=[]
    candidate_percentage=[]
    name_winner=""

    #Loop through file, extract total number of votes and populate array of candidates
    for row in csvreader:
        row_count=row_count+1
        candidate_list.append(row[2])

    counter=Counter(candidate_list)
    for s in candidate_list:
        if s not in candidate_distinct_list:
            candidate_distinct_list.add(s)
            candidate_count.append(counter[s])
            candidate_name.append(s)
            candidate_percentage.append(round(counter[s]*100/row_count,3))

    #Print results to console
    print("\nElection Results")
    print("---------------------------------")
    print(f"Total Votes: {row_count}")
    print("---------------------------------")
    for recs in range(len(candidate_count)):
        print(f"{candidate_name[recs]}: {candidate_percentage[recs]}% ({candidate_count[recs]})")
        if candidate_count[recs]>winner:
            winner=candidate_count[recs]
            name_winner=candidate_name[recs]
    print("---------------------------------")
    print(f"Winner: {name_winner}")
    print("---------------------------------")

    #Write results to text file
    with open(os.path.join(file_dir, 'analysis/election_data_results.txt'), 'w') as new_file:
        new_file.write("\nElection Results\n")
        new_file.write("---------------------------------")
        for recs in range(len(candidate_count)):
            new_file.write("\n"+str(candidate_name[recs])+" "+str(candidate_percentage[recs])+"% ("+str(candidate_count[recs])+")")
        new_file.write("\n---------------------------------")
        new_file.write("\nWinner: "+str(name_winner))
        new_file.write("\n---------------------------------")
        