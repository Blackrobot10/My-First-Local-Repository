from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver import Firefox

#path = 'D:\chromedriver_win32\chromedriver.exe'
path = 'D:\Firefix_driver\geckodriver.exe'
url = 'https://www.thetestingworld.com/testings/'

d = Firefox(executable_path=path)
d.get(url)
d.maximize_window()

#Working on text fill

d.find_element_by_name("fld_username").send_keys('blackbox')
d.find_element_by_xpath("//input[@name = 'fld_email']").send_keys("blackbox@gmail.com")
d.find_element_by_name("fld_password").send_keys('blackbox')
d.find_element_by_name("fld_cpassword").send_keys('blackbox')
d.find_element_by_name("fld_password").send_keys('blackbox')
d.find_element_by_name("fld_username").clear()
d.find_element_by_name("fld_username").send_keys('blackbox123')

#Working on radio button
d.find_element_by_xpath("//input[@value = 'home']").click()
d.find_element_by_xpath("//input[@value ='office']").click()

# Working on Checkbox
d.find_element_by_xpath("//input[@name = 'terms']").click()

# Working on button
d.find_element_by_xpath("//input[@type ='submit']").click()

#Working on links
d.find_element_by_link_text("Read Detail").click()

#Close the browser
d.close()

