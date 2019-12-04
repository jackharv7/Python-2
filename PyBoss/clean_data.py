import csv
import os
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join("..", "PyBoss", "employee_data.csv")
#open the file
state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open("employee_data.csv") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)
    new_rows = []
    print(csv_header)
    new_rows.append(csv_header)
    for row in csvreader:
        # mutate row
        if row[4] in state_abbrev:
            row[4] = state_abbrev[row[4]]
        split_name = row[1].split(' ')
        #row[1] = first name
        row[1] = split_name[1]
        #insert first name before last name (row[2] = last name)
        row.insert(1, split_name[0])       
        #change date from YYYY-MM-DD to MM/DD/YYY
        date = datetime.strptime(row[3], "%Y-%m-%d")
        del row[3]
        row.insert(3,datetime.strftime(date, "%m/%d/%Y"))
        #Asterisks for SSN
        asterisk = [numbers for numbers in row[4]]
        for number in range(6):
            if number == 3:
                continue
            asterisk[number] = '*'
        #Combine digits in SSN
        asterisk = ''.join(asterisk)
        del row[4]
        #^Delete old SSN
        #add SSN back to row
        row.insert(4,asterisk)
        #join list in list together      
        row = (','.join(map(str,row)))
        new_rows.append(row)
        print(row)

with open('summary.txt', 'w') as outfile:
    outfile.write('\n'.join(new_rows))
