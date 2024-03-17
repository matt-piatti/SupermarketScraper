from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import time
import re
import pandas as pd

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
options.set_capability("pageLoadStrategy", "none")

timestamps = []

data = pd.read_csv('companyname_timestamps_products1.csv', header=None)

for i in range(0, len(data)):
    timestamps.append(data.iloc[i][0])

driver = webdriver.Chrome(options=options)

timestamps_array = []
names_array = []
prices_array = []

while True:
    try:
        for timestamp in timestamps:

            
                
                    driver.get("http://web.archive.org/web/" + str(timestamp) + "/http://www.companyname.com.br:80/produtos/1")
                    time.sleep(30)
                    driver.execute_script("window.stop();")
                
                    product_names = driver.find_elements(By.CLASS_NAME, 'name')
                    for name in product_names:
                        
                        
                        
                        if "span" in name.get_attribute("innerHTML") or name.get_attribute("innerHTML").isupper() or "Hortifruti" in name.get_attribute("innerHTML"):
                            pass
                        else:
                            timestamps_array.append(timestamp)
                            names_array.append(name.get_attribute("innerHTML").strip())
                
                    product_prices = driver.find_elements(By.CLASS_NAME, 'number')
                    for price in product_prices:
                        if "span" in price.get_attribute("innerHTML"):
                         pass
                        else:
                            prices_array.append(price.get_attribute("innerHTML").strip())

                    print(timestamps_array)
                    print(names_array)
                    print(prices_array)

                    df = pd.DataFrame({'Timestamp': timestamps_array, 'Name': names_array, 'Price': prices_array})
                    df.to_csv('companyname_prices_products1.csv', index=False, encoding='utf-8')
        
    except TimeoutError as e:
        print(e)
        continue


# Adapted from Simon Willison's TILs https://til.simonwillison.net