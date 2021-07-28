from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import glob
import os.path
import time
import datetime


def extractdat():
    value = datetime.datetime.now()+datetime.timedelta(days=1)
    value = value.strftime("%d-%m-%Y")
    PATH = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://newwbes.nerldc.in/Report/DeclarationRldc")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located(
        (By.XPATH, "//div[@class='blockUI blockOverlay']")))

    #driver.execute_script("arguments[0].style.visibility='hidden'", element)
    date = driver.find_element_by_id("datepicker")
    date.click()
    date.clear()
    date.send_keys(value)
    date.send_keys(Keys.ENTER)
    time.sleep(5)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "btnShow"))).click()
    showdata = driver.find_element_by_id("btnShow")
    showdata.click()
    time.sleep(2)
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
    if os.path.exists(folder_path+'dec1.xlsx'):
        os.remove(folder_path+'dec1.xlsx')
    os.rename(max_file, folder_path+'dec1.xlsx')
    driver.get("https://newwbes.nerldc.in/ReportNetSchedule/GetNetScheduleIndex")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "scheduleDate"))).click()
    date = driver.find_element_by_id("scheduleDate")
    date.click()
    date.clear()
    date.send_keys(value)
    date.send_keys(Keys.ENTER)
    time.sleep(2)
    dropdown = driver.find_element_by_xpath(
        ".//a/i[@class='icon-download-alt white']")
    dropdown.click()
    time.sleep(2)
    download = driver.find_element_by_id("XlsExport")
    download.click()
    time.sleep(3)
    folder_path = r'C:\Users\yagar\Downloads\\'
    file_type = '\*xlsx'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    if os.path.exists(folder_path+'sec1.xlsx'):
        os.remove(folder_path+'sec1.xlsx')
    os.rename(max_file, folder_path+'sec1.xlsx')
    driver.quit()
