from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#https://googlechromelabs.github.io/chrome-for-testing/

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)  

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Unbwogable" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Unbwogable")
link.click()


time.sleep(10)
driver.quit()