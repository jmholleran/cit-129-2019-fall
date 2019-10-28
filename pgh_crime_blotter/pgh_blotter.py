# -*- coding: utf-8 -*-
"""
Joe Holleran
PGH Crime Blotter Analysis
10/27/2019
"""
# Python script to move prior 7 days crime blotter data into one excel file

import pandas as pd

def main():
    
    # Create list of days of the week for loop in order to create link in read_csv    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
    
    # Empty list of dataframes
    pgh_blotter_list = []    
    
    # Loop through days of week and create URL for each day: Monday, Tuesday, etc.
    for day in days_of_week:
        
        # Create dataframe and read csv file in url by day of week
        pgh = pd.read_csv("http://apps.pittsburghpa.gov/police/arrest_blotter/arrest_blotter_" + (str(day)) + ".csv")
        
        # Append pgh dataframe to list
        pgh_blotter_list.append(pgh)
        
    # Combine the lists of dataframes into one dataframe
    pgh_blotter_df = pd.concat(pgh_blotter_list)
    
    with pd.ExcelWriter('pgh_crime_blotter.xlsx') as writer:
        # Create a spreadsheet of the prior 7 days PGH crime blotter data
        pgh_blotter_df.to_excel(writer, index = False)
    
if __name__=='__main__':
    main()