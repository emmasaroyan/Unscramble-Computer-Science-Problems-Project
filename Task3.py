"""
Read file into texts and calls.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re
from functools import reduce

#Part A
dict = {} #keep codes and counts

numbers_bangalore = list(filter(lambda x: x[0][0:5] == '(080)', calls))

for record in numbers_bangalore:
    if record[1][0] == '(':
        if re.match("\(([0-9]+)\)", record[1]).group(0)[1:-1] in dict:
            dict[re.match(r"\(([0-9]+)\)", record[1]).group(0)[1:-1]] += 1
        else:
            dict[re.match("\(([0-9]+)\)", record[1]).group(0)[1:-1]] = 1
    elif record[1][0:3] == '140':
        if '140' in dict:
            dict['140'] += 1
        else:
            dict['140'] = 1
    else:
        if record[1][0:4] in dict:
            dict[record[1][0:4]] += 1
        else:
            dict[record[1][0:4]] = 1

print("The numbers called by people in Bangalore have codes:")
for key in sorted(dict):
    print(key)

#Part B
sum_of_all_values = reduce(lambda x, value: x + value, dict.values(), 0)
print(str(round((dict['080'] * 100) / sum_of_all_values, 2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
