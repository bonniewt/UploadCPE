from selenium import webdriver
import time
import pyautogui
import csv
import validators


def fill_form():
    """Opens a new Chrome browser and asks the user for input for the form URL and input csv file.
    Fills in the one form entry per entry in the input csv file
    """
    # get user input
    input_csv = get_input_csv()
    # form_name = get_form_url()

    # test input
    form_name = 'https://www.isaca.org/myisaca/managecpe'
    # input_csv = 'test.csv'

    # open the form in chrome
    browser = webdriver.Chrome()
    browser.get(form_name)
    browser.maximize_window()
    time.sleep(1)

    # click add new CPE records
    add_new_record = browser.find_element('xpath', '//*[@id="managecpeApp"]/manage-cpe/div[3]/form/div[1]/button')
    add_new_record.click()

    # read in csv
    with open(input_csv, mode='r') as file:
        csv_file = csv.reader(file)

        # skips header
        next(csv_file)

        # parses each entry
        for line in csv_file:
            course_name = line[0]
            provider = line[1]
            start_date = line[2]
            end_date = line[3]
            activity = line[4]
            delivery = line[5]
            cpe_hours = line[6]

            # title/description - fill-in-the-blank
            title_input = browser.find_element('id', 'cpe-title')
            title_input.send_keys(course_name)

            # sponsoring organization - fill-in-the-blank
            sponsor_input = browser.find_element('id', 'cpe-sponsoring')
            sponsor_input.send_keys(provider)

            # start date - date
            start_date_input = browser.find_element('id', 'cpe-start-date')
            start_date_input.send_keys(start_date)

            # end date - date
            end_date_input = browser.find_element('id', 'cpe-end-date')
            end_date_input.send_keys(end_date)

            # qualifying activity - dropdown
            activity_dropdown = browser.find_element('id', 'cpe-qualifying-activity')
            activity_dropdown.click()
            time.sleep(2)

            activity_index = get_activity_index(activity)

            for i in range(activity_index):
                pyautogui.keyDown('down')
                pyautogui.keyUp('down')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            # method of delivery - dropdown
            delivery_dropdown = browser.find_element('id', 'cpe-delivery')
            delivery_dropdown.click()
            time.sleep(2)

            delivery_index = get_delivery_index(delivery)

            for i in range(delivery_index):
                pyautogui.keyDown('down')
                pyautogui.keyUp('down')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            # CPE hours - fill-in-the-blank
            hours_input = browser.find_element('id', 'cpe-addapply-hours-CISA')
            hours_input.send_keys(cpe_hours)

            # save & add more button
            submit = browser.find_element('id', 'btnSaveAndAdd')
            submit.click()
            time.sleep(2)

    # close chromedriver
    time.sleep(2)
    browser.close()
    browser.quit()

    # close csv file
    file.close()


def get_form_url():
    """Prompts the user for the form URL"""

    form_name = input("Enter form URL: ")
    valid_url_check = validators.url(form_name)
    while not valid_url_check:
        print("Error: Invalid url provided.")
        form_name = input("Enter form URL: ")
        valid_url_check = validators.url(form_name)
    return form_name


def get_input_csv():
    """Prompts user for the input file in csv format"""

    input_csv = input("Enter input file name (csv format): ")
    filename_check = input_csv.endswith("csv")
    while not filename_check:
        print("Error: Invalid file name. Please end filename with \'.csv\' ")
        file_name = input("Enter input file name (end with .csv): ")
        filename_check = input_csv.endswith("csv")
    return input_csv


def get_activity_index(activity):
    """Determines index for qualifying activity dropdown menu"""

    if activity == "Contributions to the profession":
        return 1
    elif activity == "Exam question development and review":
        return 2
    elif activity == "ISACA professional education activities":
        return 3
    elif activity == "ISACA professional education skills-based activities (Must Contain Lab Exercises)":
        return 4
    elif activity == "Mentoring":
        return 5
    elif activity == "Non-ISACA professional education activities":
        return 6
    elif activity == "Non-ISACA professional education skills-based activities (Must Contain Lab Exercises)":
        return 7
    elif activity == "Passing related professional examinations":
        return 8
    elif activity == "Passing related skills-based professional examinations (Must Contain Lab Exercises)":
        return 9
    elif activity == "Publication of articles, monographs and books":
        return 10
    elif activity == "Self-study courses":
        return 11
    elif activity == "Summary CPE (Qualifying Activity not specified)":
        return 12
    elif activity == "Teaching/lecturing/presenting":
        return 13
    elif activity == "Teaching/lecturing/presenting skills-based exercises and training (Must Contain Lab Exercises)":
        return 14
    elif activity == "Vendor sales/marketing presentations":
        return 15
    elif activity == "Working as a Cybersecurity Practitioner (CSX-P certification required)":
        return 16
    elif activity == "Working on ISACA Boards/Committees/Chapters":
        return 17
    else:
        return -1


def get_delivery_index(delivery):
    """Determines index for delivery dropdown menu"""

    if delivery == "By Mail":
        return 1
    elif delivery == "In Person":
        return 2
    elif delivery == "NA":
        return 3
    elif delivery == "Online":
        return 4
    else:
        return -1
