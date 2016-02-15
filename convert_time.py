import re

from datetime import datetime


'''
Use this script to convert time obtained from NASA data dump to python
supported formats. This makes working with time easy in django.

Example: 01/01/1880 12:00:00 AM  =>  1880-01-01 00:00:00
'''
date_time_validation = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} [A-Z]{2}'

def is_valid_date_time(date_time):
    reg = re.match(date_time_validation, date_time)
    if reg:
        return True
    return False

def replace_time(line):
    words = line.split(',')
    date_time = words[6]

    # validate if words[6] is datetime
    if is_valid_date_time(date_time):
        words[6] = str(datetime.strptime(date_time, '%m/%d/%Y %I:%M:%S %p'))

    return ','.join(words)



# open files to read and write.
with open('Meteorite.csv', 'r') as fr:
    with open('Meteorite_sanitized.csv', 'w') as fw:
        for line in fr:
            newline = replace_time(line)
            fw.write(newline)
