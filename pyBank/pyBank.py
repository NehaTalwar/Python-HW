#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv

budget_csv_path = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_csv_path , newline="")as csvfile:
    
    # Read the header row first skip this part if there is no header 
    budgetreader = csv.reader(csvfile , delimiter=",")
 
    
    csv_header = next(csvfile)
    print(f"header: {csv_header}")
    
    for row in budgetreader:
        print(row)
      
    


# In[13]:


import os
import csv

budget_csv_path = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_csv_path , newline="")as csvfile:
    
# Read the header row first skip this part if there is no header 
    budgetreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvfile)
    
    
    revenue = []
    date = []
    rev_change =[]
    
    total_months = 0 
    total = 0
    
    for row in budgetreader:
        total_months = total_months + 1
        revenue.append(float(row[1]))
        date.append(row[0])
        
        result = (f"\n\nFinancial Analysis\n"
           f"\n-----------------------------------\n"
           f"\nTotal Months: {len(date)}\n"
           f"\nTotal Revenue: ${sum(revenue)}\n")
    print(result)
        

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

    max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
    
    avg_round = round(avg_rev_change)
    avg_change = f"Avereage Change:${avg_round}\n"
    print(avg_change)
    #txt_file.write(avg_change)
    profit_inc = f"Greatest Increase in Profits: {max_rev_change_date}, (${max_rev_change})\n"
    print(profit_inc)
    #txt_file.write(profit_inc)
    profit_dec = f"Greatest Decrease in Profits: {min_rev_change_date}, (${min_rev_change})\n"
    print(profit_dec)
    #txt_file.write(profit_dec)


            



# In[ ]:





# In[ ]:




