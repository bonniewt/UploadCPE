import csv
import random
from faker import Faker

fake_data = Faker()

# uncomment this if you want to generate the same dataset, else this will produce different set each run
# Faker.seed(0)

# get user input for file name and check if it is csv
file_name = input("Enter file name (end with .csv): ")
filename_check = file_name.endswith("csv")
while not filename_check:
    print("Error: Invalid file name. Please end filename with \'.csv\' ")
    file_name = input("Enter file name (end with .csv): ")
    filename_check = file_name.endswith("csv")

# get user input for number of entries and check if it is valid
entries = input("Enter number of CPE certificate entries (integer): ")
int_entries = entries.isnumeric()
while not int_entries:
    print("Error: Invalid value entered. Please enter an integer.")
    entries = input("Enter number of CPE certificate entries (integer): ")
    int_entries = entries.isnumeric()
num_entries = int(entries)

#TODO add check for numbers between 0 and 100

# options
provider = ("AICPA", "WSCPA", "IIA", "ISACA", "Becker", "EY", "PwC", "KPMG", "Deloitte")
role = ("Student", "Instructor/Developer", "Published Authorship", "ACB Board Service")
credit_type = ("Technical", "Non-Technical")

# create a csv file with column headings
with open(file_name, 'w', newline='') as csvFile:
    fieldnames = ["Completion Date",
                  "Provider",
                  "Course Title",
                  "Role",
                  "Credit Type",
                  "Number of Hours",
                  "Comments"]
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    # selects random value for each of the attributes
    for _ in range(num_entries):
        writer.writerow({"Completion Date": fake_data.date_this_year(),
                         "Provider": random.choice(provider),
                         "Course Title": fake_data.sentence(nb_words=5),
                         "Role": random.choice(role),
                         "Credit Type": random.choice(credit_type),
                         "Number of Hours": random.randint(1, 40),
                         "Comments": fake_data.sentence(nb_words=15)})

csv_fake_data = csv.writer(csvFile)
