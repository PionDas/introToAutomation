#importing webdriver package from selenium
from selenium import webdriver

#creating a driver by chrome
driver = webdriver.Chrome()

#making a request
driver.get('https://www.youtube.com/')



#finding the search on the 'xpath' from the inspect
searchBox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

#writing text the search box
searchBox.send_keys('pion Das')

#using the search buttom
#searchButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')



#hitting the search button
searchButton.click()
