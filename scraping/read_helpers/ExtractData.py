from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def get_tender_data(driver: webdriver):
    tender_results = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((
            By.XPATH, '//*[@id="mainComponent"]/div/app-search-page/div/app-michrazim-result/div/div[4]')))
    tender_list = WebDriverWait(tender_results, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.list-rows')))
    last_tender = tender_list[0]
    while tender_list[-1] != last_tender:
        last_tender = tender_list[-1]
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)
        tender_list = WebDriverWait(tender_results, 10).until(
            ec.presence_of_all_elements_located((By.TAG_NAME, 'app-michraz-details')))
    tender_list = WebDriverWait(tender_results, 10).until(
        ec.presence_of_all_elements_located((By.TAG_NAME, 'app-michraz-details')))
    data_list = []
    for tender in tender_list:
        text = tender.text.split('\n')
        amount_apartment, area, book_published, category, city, last_date, neighborhood, number, open_date, publish_date, target = extract_data_from_text(
            text)
        link = create_link(number)
        # data_list.append(
        #     TenderData(link, number, area, city, neighborhood, amount_apartment, category, target, bool(book_published),
        #                publish_date, open_date, last_date))
        data_list.append([link, number, area, city, neighborhood,
                          amount_apartment, category, target, book_published,
                          publish_date, open_date, last_date])
    return data_list


def create_link(number: str):
    try:
        serial_number, year = number.split("/")
        if len(serial_number) > 4:
            raise IndexError
        serial_number = "0" * (4 - len(serial_number)) + serial_number
        if len(year + serial_number) != 8:
            raise IndexError
        else:
            return "https://apps.land.gov.il/MichrazimSite/#/michraz/" + year + serial_number
    except:
        raise IndexError


def extract_data_from_text(text):
    amount_apartment, category, number = extract_line_0(text)
    area, book_published = extract_line_1(text)
    city, neighborhood = extract_line_2(book_published, text)
    target = extract_line_3(book_published, text)
    last_date, open_date, publish_date = extract_dates(book_published, text)
    return amount_apartment, area, book_published, category, city, last_date, neighborhood, number, open_date, publish_date, target


def extract_line_3(book_published, text):
    target = " ".join(text[3 + book_published].split(" ")[1::1])
    return target


def extract_dates(book_published, text):
    publish_date = text[4 + book_published].split(" ")[-1]
    open_date = text[5 + book_published].split(" ")[-1]
    last_date = " ".join(text[6 + book_published].split(" ")[-2::1])
    return last_date, open_date, publish_date


def extract_line_2(book_published, text):
    city = text[2 + book_published].split(" ")[1].strip(", ")
    neighborhood = " ".join(text[2 + book_published].split(" ")[2::1])
    return city, neighborhood


def extract_line_1(text):
    book_published = 0
    if text[1] == 'פורסמה חוברת המכרז':
        book_published = 1
    area = " ".join(text[1 + book_published].split(" ")[2::])
    return area, book_published


def extract_line_0(text):
    number = text[0].split(" ")[0]
    if text[0].split(" ")[-2].isdigit():
        amount_apartment = int(text[0].split(" ")[-2])
        category = " ".join(text[0].split(" ")[1: -2: 1])
    else:
        amount_apartment = 0
        category = " ".join(text[0].split(" ")[1:: 1])
    return amount_apartment, category, number
