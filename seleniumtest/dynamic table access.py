# from selenium.webdriver.common.by import By
# import time
# from selenium import webdriver

# driver = webdriver.Edge()
#
# driver.implicitly_wait(10)
# driver.get("https://dynamictable.com/demos/")
# driver.maximize_window()
#
#
# rows=len(driver.find_elements(By.XPATH,"//table[@id='dynamicTable']//tr"))
# columns=len(driver.find_elements(By.XPATH,"//table[@id='dynamicTable']//tr[1]//td"))
#
# print(rows)
# print(columns)
# print(f"Rows: {rows}, Columns: {columns}")
# #data=driver.find_element(By.XPATH, "//table[@id='dynamicTable']/tbody/tr[1]/td[3]").text
# # print(data)
# count =0
# for r in range(1,rows):
#      for c in range(1,columns):
#         data=driver.find_element(By.XPATH,"//table[@id='dynamicTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         #Anchor=driver.find_element(By.XPATH,"//table[@id='dynamicTable']/tbody/tr["+str(r)+"]/td[3]").text
#         #Anchor=driver.find_element(By.XPATH,"//table[@id='dynamicTable']/tr["+str(r)+"]/td[3]/a[contains(.,'2000')]").text
#         anchor=data.__contains__("2000")
#         if anchor==True:
#             print(r,c)
#             print(driver.find_element(By.XPATH,"//table[@id='dynamicTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text)
#             count +=1
#
#
#
#         # print(anchor)
#
#
#
# print(count)
# time.sleep(15)
# driver.quit()

from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

# Set up the browser and open the URL
driver.implicitly_wait(10)
driver.get("https://dynamictable.com/demos/")
driver.maximize_window()

# Get the number of rows and columns
rows = len(driver.find_elements(By.XPATH, "//table[@id='dynamicTable']//tr"))
cols = len(driver.find_elements(By.XPATH, "//table[@id='dynamicTable']//tr[1]//td"))

print(f"Rows: {rows}, Columns: {cols}")

# Initialize the counter
count = 0

# Iterate through the table and count cells containing "2000"
for r in range(1, rows):
    for c in range(1, cols + 1):
        cell_xpath = f"//table[@id='dynamicTable']/tbody/tr[{r}]/td[{c}]"
        cell_text = driver.find_element(By.XPATH, cell_xpath).text
        print(f"{cell_text}", end="     ")
        # if "2000" in cell_text:
        #     print(f"Found '2000' at row {r}, column {c} : {cell_text}")
        count += 1
    print()

print(f"Total count: {count}")

# Clean up and close the browser
time.sleep(5)
driver.quit()
