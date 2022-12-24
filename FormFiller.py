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
    form_name = get_form_url()

    # open the form in chrome
    browser = webdriver.Chrome()
    browser.get(form_name)
    browser.maximize_window()
    time.sleep(1)

    # test input
    # form_name = 'https://forms.gle/xrcrwKP7k9jEq3os7'
    # input_csv = 'test.csv'

    # read in csv
    with open(input_csv, mode='r') as file:
        csv_file = csv.reader(file)

        # skips header
        next(csv_file)

        # parses each entry
        for line in csv_file:
            date = line[0]
            provider = line[1]
            course_name = line[2]
            role = line[3]
            credit = line[4]
            cpe_hours = line[5]
            comment = line[6]

            # completion date - date
            date_input = browser.find_element('xpath',
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div['
                                              '2]/div[1]/div/div[1]/input')
            date_input.send_keys(date)

            # provider - fill in the blank
            provider_input = browser.find_element('xpath',
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
            provider_input.send_keys(provider)

            # course title - fill in the blank
            course_title = browser.find_element('xpath',
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
            course_title.send_keys(course_name)

            # role - drop down menu
            role_dropdown = browser.find_element('xpath',
                                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div['
                                                 '1]/div[1]/div[1]')
            role_dropdown.click()
            time.sleep(1)

            role_index = get_role_index(role)

            for i in range(role_index):
                pyautogui.keyDown('down')
                pyautogui.keyUp('down')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            # credit type - drop down menu
            credit_dropdown = browser.find_element('xpath',
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div['
                                                   '2]/div/div[1]/div[1]/div[1]')
            credit_dropdown.click()
            time.sleep(1)

            credit_index = get_credit_index(credit)
            for _ in range(credit_index):
                pyautogui.keyDown('down')
                pyautogui.keyUp('down')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            # number of hours - fill in the blank
            num_hours_input = browser.find_element('xpath',
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div['
                                                   '2]/div/div[1]/div/div[1]/input')
            num_hours_input.send_keys(cpe_hours)

            # comments - fill in the blank
            comment_input = browser.find_element('xpath',
                                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div['
                                                 '1]/div[2]/textarea')
            comment_input.send_keys(comment)

            # submit button
            submit = browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()

            # submit another response
            another_response = browser.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()

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


def get_role_index(role):
    """Determines index for role dropdown menu"""

    if role == "Student":
        return 1
    elif role == "Instructor/Developer":
        return 2
    elif role == "Published Authorship":
        return 3
    elif role == "ACB Board Service":
        return 4
    else:
        return -1


def get_credit_index(credit):
    """Determines index for credit hours dropdown menu"""

    if credit == "Technical":
        return 1
    elif credit == "Non-Technical":
        return 2
    else:
        return 0
