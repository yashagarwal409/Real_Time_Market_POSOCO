from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
import os.path
import time


def extract():
    PATH = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://newwbes.nerldc.in/Report/DeclarationRldc")
    time.sleep(2)
    showdata = driver.find_element_by_id("btnShow")
    showdata.click()
    time.sleep(2)
    dropdown = driver.find_element_by_xpath(
        ".//a/i[@class='icon-download-alt white']")
    dropdown.click()
    download = driver.find_element_by_id("XlsExport")
    download.click()
    time.sleep(3)
    folder_path = r'C:\Users\yagar\Downloads\\'
    file_type = '\*xlsx'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    if os.path.exists(folder_path+'dec.xlsx'):
        os.remove(folder_path+'dec.xlsx')
    os.rename(max_file, folder_path+'dec.xlsx')
    driver.get("https://newwbes.nerldc.in/ReportNetSchedule/GetNetScheduleIndex")
    dropdown = driver.find_element_by_xpath(
        ".//a/i[@class='icon-download-alt white']")
    dropdown.click()
    time.sleep(1)
    download = driver.find_element_by_id("XlsExport")
    download.click()
    time.sleep(3)
    folder_path = r'C:\Users\yagar\Downloads\\'
    file_type = '\*xlsx'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    if os.path.exists(folder_path+'sec.xlsx'):
        os.remove(folder_path+'sec.xlsx')
    os.rename(max_file, folder_path+'sec.xlsx')
    driver.quit()
