from selenium import webdriver
import time
import pyautogui
import csv

# open the form in chrome
browser = webdriver.Chrome()
browser.get('https://forms.gle/xrcrwKP7k9jEq3os7')
browser.maximize_window()
time.sleep(5)

# read in csv

index_number = 5
role = "Student"
credit = 'Technical'
date = '09/09/2022'
provider_name = 'WSCPA'
course_name = 'Tax'
cpe_hours = '1'
na_comment = ' '

# completion date - date

# provider - fill in the blank
provider = browser.find_element('xpath',
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
provider.send_keys(provider_name)

# course title - fill in the blank
course_title = browser.find_element('xpath',
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
course_title.send_keys(course_name)

# role - drop down menu
role_dropdown = browser.find_element('xpath',
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
role_dropdown.click()
time.sleep(3)

if role == "Student":
    role_index = 1

elif role == "Instructor/Developer":
    role_index = 2

elif role == "Published Authorship":
    role_index = 3

elif role == "ACB Board Service":
    role_index = 4

else:
    role_index = 0

for _ in range(role_index):
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

# credit type - drop down menu
credit_dropdown = browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]')
credit_dropdown.click()
time.sleep(3)

if credit == "Technical":
    credit_index = 1
elif credit == "Non-Technical":
    credit_index = 2
else:
    credit_index = 0

for _ in range (credit_index):
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

# number of hours - fill in the blank
num_hours = browser.find_element('xpath',
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
num_hours.send_keys(cpe_hours)

# comments - fill in the blank
comment = browser.find_element('xpath',
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')
comment.send_keys(na_comment)

# submit button
submit = browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()

# close chromedriver
# browser.close()
# browser.quit()
