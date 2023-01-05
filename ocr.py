import os
import pytesseract
from pdf2image import convert_from_path
import csv

'''
PDF format input
'''

filePath = 'WSCPA.pdf'
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

# create dictionary to store values
Dict = {}

# method to parse for values after a given field name
def substring_after(string, delimiter):
    first_partitioned_str = string.partition(delimiter)
    second_partitioned_str = first_partitioned_str[2] # string after the provided field name (delimiter)
    third_partitioned_str = second_partitioned_str.partition('\\n')
    fourth_partitioned_str = third_partitioned_str[0] # string before the newline char
    return fourth_partitioned_str

# read in pdf to string
for page_data in doc:
    pre_txt = pytesseract.image_to_string(page_data).encode("utf-8")
    txt = str(pre_txt)

    # Completion Date
    completion_date = substring_after(txt, "Event Date: ")
    Dict['Completion Date'] = completion_date

    # Provider
    provider = substring_after(txt, "CPE Sponsor: ")
    Dict["Provider"] = provider

    # Course Title
    course = substring_after(txt, "Member Exclusive: ")
    Dict["Course Title"] = course

    # Role - will always be a student for CPE certificates
    Dict['Role'] = 'Student'

    # Credit Type - will always be technical for CPE certificates
    Dict['Credit Type'] = 'Technical'

    # Number of Hours
    hours = substring_after(txt, "Total Credit Earned: ")
    Dict['Number of Hours'] = hours

# print parsed contents to terminal
print(Dict)

# output parsed data to csv file
field_names = ['Completion Date', 'Provider', 'Course Title', 'Role', 'Credit Type', 'Number of Hours', 'Comments']

with open('test_file.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerow(Dict)