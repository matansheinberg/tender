import os
#fdfs
from read_helpers.Search import *
from read_helpers.ExtractData import get_tender_data
from read_helpers.TenderCategory import TenderCategory
import pandas as pd


def write_data_to_excel(data):
    df = pd.DataFrame(data,
                      columns=['link', 'number', 'area', 'city', 'neighborhood', 'amount apartments',
                               'category', 'target', 'book published', 'publish date',
                               'open date', 'last date'])
    df.to_excel('tender_data.xlsx', index=False)


def update_excel_file(data):
    existing_data = pd.read_excel('tender_data.xlsx')
    new_data = pd.DataFrame(data,
                            columns=['link', 'number', 'area', 'city', 'neighborhood', 'amount apartments',
                                     'category', 'target', 'book published', 'publish date',
                                     'open date', 'last date'])
    combined_data = pd.concat([existing_data, new_data])
    combined_data = combined_data.drop_duplicates(subset='link', keep='first')
    combined_data.to_excel('tender_data.xlsx', index=False)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        enter_search_mode(driver)
        search_by_number(driver)
        search_by_category(driver, [TenderCategory.REGISTRATION_LOTTERY, TenderCategory.UNSPECIFIED_LOT])
        search_by_city(driver)
        run_search(driver)
        data_list = get_tender_data(driver)
        if os.path.exists('tender_data.xlsx'):
            update_excel_file(data_list)
        else:
            write_data_to_excel(data_list)
    finally:
        driver.quit()
