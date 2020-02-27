import os
import csv 

#reading file
with open('budget_data.csv') as budget:
    csv_reader = csv.reader(budget)
    


    csv_header= next(csv_reader)

    total_months = 0
    PL_total = 0

    # find total number of months
    for row in csv_reader:
        total_months = total_months+1
    
    # find total sum of profit and losses   
        PL_total = PL_total + int(row[1])
        
    



    print('Total Months:' + str(total_months))
    print('Total: $' + str(PL_total))
    # print(average_change)



    

    
    # with open('budget_data.csv','w') as csv_budget_two:
    #     csv_dictreader = csv.DictReader(csv_budget_two)
        
        
    #     fieldnames=['Date','Profit/Losses']

    #     csv_writer = csv.DictWriter(csv_budget_two,fieldnames = fieldnames, delimeters = ',t')
                
    #     csv_writer.writeheader()

    
    
