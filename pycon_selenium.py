from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q") #'q' because is the name that was given to the search bar in the html file of python.org
elem.clear() # to flush any previous text in the searchbar (e.g. 'search')
elem.send_keys("pycon") # Text we want to search for
elem.send_keys(Keys.RETURN) # Presss ENTER
assert "No results found." not in driver.page_source
#driver.close()"""