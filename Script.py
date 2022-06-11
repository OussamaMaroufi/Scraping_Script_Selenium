import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://www.adamchoi.co.uk"
driver_path = "/usr/bin/chromedriver"
s = Service(driver_path)
driver = webdriver.Chrome(service=s)

driver.get(website)
driver.maximize_window()
driver.implicitly_wait(5)

Over_element = driver.find_element(
    by=By.CSS_SELECTOR, value='a[data-ng-click="sc.check(6)"]')

Over_element.click()

detailed_element = driver.find_element(
    by=By.CSS_SELECTOR, value='a[ui-sref="site.oversdetailed"]')
detailed_element.click()

btn_all_matches_element = driver.find_element(by=By.CSS_SELECTOR,value='label[analytics-event="All matches"]')
btn_all_matches_element.click()

matches = driver.find_elements(by=By.TAG_NAME,value='tr')



date = []
home_team = []
score = []
away_team = []

print(matches[1])

for match in matches:
    date.append(match.find_element(by=By.XPATH,value="./td[1]").text)
    home  = match.find_element(by=By.XPATH,value="./td[2]").text
    home_team.append(home)
    print(home)
    score.append(match.find_element(by=By.XPATH,value="./td[3]").text)
    away_team.append(match.find_element(by=By.XPATH,value="./td[4]").text)

driver.quit()

df = pd.DataFrame({'date':date,'home':home_team,'score':score,'away_team':away_team})

df.to_csv('Football_csv.csv',index=False)
print(df)




