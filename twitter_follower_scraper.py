from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys

if len(sys.argv) == 1:
    print("Usage: python twitter_follower_scraper.py <user-url>")
    exit()
# I use MS edge web driver    
driver = webdriver.Edge(executable_path="msedgedriver.exe")
# load website
driver.get(sys.argv[1])
wait = WebDriverWait(driver, timeout=10)
action = ActionChains(driver)
# wait until web is loaded.
follower_link = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='follower']"))
    )
# mouse over a link of follower numbers
action.move_to_element(follower_link).perform()
# to appear number of followers tooltip
follower_tooltip = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='tooltip']"))
    )
print(follower_tooltip.text)

