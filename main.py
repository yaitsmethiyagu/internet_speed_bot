from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = "https://fast.com/"
driver.get(url)

time.sleep(20)
show_more = driver.find_element(By.LINK_TEXT, "Show more info")
show_more.click()
time.sleep(15)
download_speed = driver.find_element(By.ID, "down-mb-value").text
upload_speed = driver.find_element(By.ID, "up-mb-value").text

print(download_speed)
print(upload_speed)
driver.switch_to.new_window("tab")
driver.get("https://twitter.com/thiyagshankar")