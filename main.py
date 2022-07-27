from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')

headers = driver.find_elements(By.CLASS_NAME,'data-table__header')
rows = driver.find_elements(By.CLASS_NAME,'data-table__row')

table_header = []
for header in headers:
    table_header.append(header.text)

table_rows = []
for row in rows:
    table_rows.append(row.text)

table_rows1 = []
for table_row in table_rows:
     row1 = table_row.split("\n")
     last_element = row1[-1].split(" ")
     del row1[-1]
     for element in last_element:
         row1.append(element)
     table_rows1.append(row1)



driver.quit()

df = pd.DataFrame(columns=table_header, data=table_rows1)
df.to_excel('data.xlsx')

