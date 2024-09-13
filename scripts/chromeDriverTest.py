from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

# ...

driver.get('https://www.nintendo.com/')

print(driver.page_source)


driver.quit()
