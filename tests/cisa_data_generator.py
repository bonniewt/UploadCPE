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

# options
provider = ("AICPA",
            "WSCPA",
            "IIA",
            "ISACA",
            "Becker",
            "EY",
            "PwC",
            "KPMG",
            "Deloitte")
activity = ("Contributions to the profession",
            "Exam question development and review",
            "ISACA professional education activities",
            "ISACA professional education skills-based activities (Must Contain Lab Exercises)",
            "Mentoring",
            "Non-ISACA professional education activities",
            "Non-ISACA porfessional education skills-based activities (Must Contain Lab Exercises",
            "Passing related professional examinations",
            "Passing related skills-based professional examinations (Must Contain Lab Exercises)",
            "Publication of articles, monographs and books",
            "Self-study courses",
            "Summary CPE (Qualifying Activity not specified)",
            "Teaching/lecturing/presenting",
            "Teaching/lecturing/presenting skills-based exercises and training (Must Contain Lab Exercises)",
            "Vendor sales/marketing presentations",
            "Working as a Cybersecurity Practitioner (CSX-P certification required)",
            "Working on ISACA Boards/Committees/Chapters")
delivery_method = ("By Mail",
                   "In Person",
                   "Online")

# create a csv file with column headings
with open(file_name, 'w', newline='') as csvFile:
    fieldnames = ["Title/Description",
                  "Sponsoring Organization",
                  "Start Date",
                  "End Date",
                  "Qualifying Activity",
                  "Method of Delivery",
                  "CPE hours"]
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    # selects random value for each of the attributes
    for _ in range(num_entries):
        rand_activity = random.choice(activity)
        if rand_activity == "Contributions to the profession" \
                or rand_activity == "Exam question development and review" \
                or rand_activity == "Mentoring" \
                or rand_activity == "Passing related professional examinations" \
                or rand_activity == "Passing related skills-based professional examinations (Must Contain Lab " \
                                    "Exercises)" \
                or rand_activity == "Publication of articles, monographs and books" \
                or rand_activity == "Self-study courses" \
                or rand_activity == "Summary CPE (Qualifying Activity not specified)" \
                or rand_activity == "Teaching/lecturing/presenting" \
                or rand_activity == "Teaching/lecturing/presenting skills-based exercises and training (Must Contain " \
                                    "Lab Exercises)" \
                or rand_activity == "Vendor sales/marketing presentations" \
                or rand_activity == "Working on ISACA Boards/Committees/Chapters":
            delivery = "NA"
        elif rand_activity == "ISACA professional education activities" \
                or rand_activity == "ISACA professional education skills-based activities (Must Contain Lab Exercises)" \
                or rand_activity == "Non-ISACA professional education activities" \
                or rand_activity == "Non-ISACA porfessional education skills-based activities (Must Contain Lab " \
                                    "Exercises":
            delivery = random.choice(delivery_method)
        elif rand_activity == "Working as a Cybersecurity Practitioner (CSX-P certification required)":
            delivery = "In Person"
        else:
            delivery = " "

        writer.writerow({"Title/Description": fake_data.sentence(nb_words=5),
                         "Sponsoring Organization": random.choice(provider),
                         "Start Date": fake_data.date_this_year(),
                         "End Date": fake_data.date_this_year(),
                         "Qualifying Activity": rand_activity,
                         "Method of Delivery": delivery,
                         "CPE hours": random.randint(1, 8)})

csv_fake_data = csv.writer(csvFile)
