import re
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from user.User import User

date_pattern = r'^\d{2}/\d{2}/\d{4}$'


# Function to check if a string matches the date pattern
def valid_date_format(date_str):
    return bool(re.match(date_pattern, date_str))


def login_to_account(driver: webdriver, user: User):
    id_bar = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="userId"]')))
    id_bar.send_keys(user.get_username())
    password = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="userPass"]')))
    password.send_keys(user.get_password())
    connect_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="loginSubmit"]/span[2]')))
    connect_button.click()
    second_pass = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="smsOtp"]')))
    second_pass.send_keys(input("enter code sent to sms: "))
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="loginOtpSubmit"]'))).click()
    time.sleep(5.5)


if __name__ == '__main__':
    data = pd.read_excel('tender_data.xlsx')
    for index, row in data.iterrows():
        link = row['link']
        open_date = row['open date']
        if valid_date_format(open_date):
            date_format = '%d/%m/%Y'
            date_obj = datetime.strptime(open_date, date_format)
            current_datetime = datetime.now()
            if date_obj > current_datetime:
                print("The provided date is in the future. " + row['number'])
                # row['']
            else:
                print("The provided date is in the past. " + row['number'])
                driver = webdriver.Chrome()
                try:
                    driver.get(link)
                    sign_page = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((
                        By.XPATH,
                        '//*[@id="mainComponent"]/div/app-michraz-page/div/div[1]/div[1]/div[2]/div[1]/span[1]/a')))
                    url = sign_page.get_attribute('href')
                    driver.get(url)
                    time.sleep(3)
                    if driver.current_url.startswith("https://login"):
                        login_to_account(driver, User("318253549", "12345678aA!"))
                    mark = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                        (By.XPATH, '//*[@id="MagishHatzaa"]/aside/div/div[1]/input')))
                    # mark = driver.find_element(By.XPATH, '//*[@id="MagishHatzaa"]/aside/div/div[1]/input')
                    mark.click()
                    driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys("שינברג")
                    driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys("מתן")
                    driver.find_element(By.XPATH, '//*[@id="inputTaarichLeda"]').send_keys("01051997")
                    no_israel_id = True
                    if no_israel_id:
                        driver.find_element(By.XPATH, '//*[@id="isIsraeli0"]').click()
                        driver.find_element(By.XPATH, '//*[@id="MisZihuy"]').send_keys("12345")
                        driver.find_element(By.XPATH, '//*[@id="EretzHanpakatDarkon"]').send_keys("אירלנד")
                        # driver.find_element(By.XPATH, '//*[@id="jqxWidgetf7a795ac_BrowseButton"]').send_keys(
                        #     "C:\\Users\\matan\\PycharmProjects\\scraping\\id1.jpeg")
                    else:
                        driver.find_element(By.XPATH, '//*[@id="MisZihuy"]').send_keys("318253549")
                    driver.find_element(By.XPATH, '/html/body/div[3]/input').send_keys(
                        "C:\\Users\\matan\\PycharmProjects\\scraping\\id1.jpeg")
                    driver.find_element(By.XPATH, '//*[@id="MechaneChelekYachsiSutaf"]').send_keys("50")
                    driver.find_element(By.XPATH,
                                        '//*[@id="MagishBakasha"]/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/input').send_keys(
                        "50")


                finally:
                    driver.quit()
        else:
            print("invalid open date. " + row['number'])
