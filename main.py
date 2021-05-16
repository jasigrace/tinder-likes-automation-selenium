import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import  webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

TINDER = 'https://tinder.com/'

driver.get(TINDER)
time.sleep(2)

login = driver.find_element_by_css_selector('.focus-button-style')
login.click()
time.sleep(5)

try:
    facebook = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[2]/button')
except NoSuchElementException:
    more = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/button')
    more.click()
    time.sleep(5)
facebook = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id("email")
email.send_keys("YOU_MAIL_ID_FACEBOOK")

password = driver.find_element_by_id("pass")
password.send_keys("YOUR_PASSWORD_FACEBOOK")
time.sleep(2)

login = driver.find_element_by_name("login")
login.click()
time.sleep(4)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(2)

location_permission = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[1]')
location_permission.click()
time.sleep(2)

notifications_permission = driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[2]')
notifications_permission.click()
time.sleep(2)

cookies_permission = driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[2]/div/div/div[1]/button')
cookies_permission.click()
time.sleep(2)

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(3)

    try:
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)