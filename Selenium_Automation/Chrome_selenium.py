from operator import index
from select import select
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select

path = 'D:\chromedriver_win32\chromedriver.exe'
#path = 'D:\Firefix_driver\geckodriver.exe'
url = 'https://www.thetestingworld.com/testings/'

d = Chrome(executable_path=path)
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

#Work on 
e = Select(d.find_element_by_name("sex"))
e.select_by_index(2)
#e.select_by_value("2")
#e.select_by_visible_text("Male")

e1 = Select(d.find_element_by_name("country"))
e1.select_by_visible_text("India")

d.implicitly_wait(5)

e2 = Select(d.find_element_by_name("state"))
e2.select_by_visible_text("Tamil Nadu")

d.implicitly_wait(5)

e3 = Select(d.find_element_by_name("city"))
e3.select_by_visible_text("Chennai")

d.implicitly_wait(5)

#d.find_element_by_xpath("//input[@type = 'text']").send_keys('600005')
d.find_element_by_name("zip").send_keys('600005')

#Working on Checkbox
d.find_element_by_xpath("//input[@name = 'terms']").click()

# Working on button
d.find_element_by_xpath("//input[@type ='submit']").click()

#Working on links
d.find_element_by_link_text("Read Detail").click()

d.implicitly_wait(15)

#Close the browser
d.close()

