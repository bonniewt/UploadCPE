from selenium import webdriver
import time
import csv

# open the form in chrome
browser = webdriver.Chrome()
browser.get('https://forms.gle/xrcrwKP7k9jEq3os7')
browser.maximize_window()
time.sleep(5)

# read in csv

provider_name = 'WSCPA'
course_name = 'Tax'
cpe_hours = '1'
na_comment = ' '

# def fillForm(date, course, role, credit, hours, comments)


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

# credit type - drop down menu

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
browser.close()
browser.quit()
