import time
from read_helpers.TenderCategory import TenderCategory
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def enter_search_mode(driver: webdriver):
    url = 'https://apps.land.gov.il/MichrazimSite/#/homePage'
    driver.get(url)
    active_tenders_button = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH,
                                        '//*[@id="mainComponent"]/div/app-home-page/div/div/div[1]/div[2]/button')))
    active_tenders_button.click()


def search_by_number(driver: webdriver, number: str = None):
    if number:
        search_number = driver.find_element(by=By.XPATH, value='//*[@id="mismichraz_id"]')
        search_number.send_keys(number)


def search_by_city(driver: webdriver, city_name: str = None):
    if city_name:
        search_city = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="Yishuv_id"]/span/input')))
        time.sleep(2)
        search_city.send_keys(city_name)
        time.sleep(2)
        search_city.send_keys(Keys.ARROW_DOWN)
        search_city.send_keys(Keys.RETURN)


def run_search(driver: webdriver):
    search_button = driver.find_element(By.XPATH, '//*[@id="search-wrapper"]/div[2]/div[3]/span')
    search_button.send_keys(Keys.RETURN)


def search_by_category(driver: webdriver, category_list: [TenderCategory] = None):
    if category_list is None:
        category_list = []
    category_selector = driver.find_element(By.XPATH, '//*[@id="SugMichraz_id"]/div/div[2]/div')
    category_selector.click()
    categories_listbox = driver.find_element(By.XPATH, '//*[@id="SugMichraz_id"]/div/div[4]/div[2]/ul')
    categories = categories_listbox.find_elements(By.TAG_NAME, 'p-multiselectitem')
    for tender_category in category_list:
        categories[tender_category.value].click()
