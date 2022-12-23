import csv
import random
from faker import Faker

fake_data = Faker()

# uncomment this if you want to generate the same dataset, else this will produce different set each run
# Faker.seed(0)

provider = ("AICPA", "WSCPA", "IIA", "ISACA", "Becker", "EY", "PwC", "KPMG", "Deloitte")
role = ("Student", "Instructor/Developer", "Published Authorship", "ACB Board Service")
credit_type = ("Technical", "Non-Technical")

#create a csv file with column headings
with open('test_data_set.csv', 'w', newline='') as csvFile:
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
    # to adjust number of cpe entries change range(X) value in output
    for _ in range(100):
        writer.writerow({"Completion Date": fake_data.date_this_year(),
                         "Provider": random.choice(provider),
                         "Course Title": fake_data.sentence(nb_words=5),
                         "Role": random.choice(role),
                         "Credit Type": random.choice(credit_type),
                         "Number of Hours": random.randint(1, 40),
                         "Comments": fake_data.sentence(nb_words=15)})

    csv_fake_data = csv.writer(csvFile)