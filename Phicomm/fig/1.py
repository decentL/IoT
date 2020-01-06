from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import sys
import time

chrome_options = Options()
chrome_options.add_experimental_option('w3c',False)
driver = webdriver.Chrome(chrome_options=chrome_options)
homeURL = sys.argv[1]

def submit_empty_form(URL):
  driver.get(URL)
  time.sleep(20)
  #sleeping 20 seconds to login！
  e = driver.find_element_by_id('save_pwd')
  e.submit()
  driver.close()

submit_empty_form(sys.argv[1])
