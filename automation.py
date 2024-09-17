from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import details
browser = webdriver.Chrome() # open browser driver
# browser.get("https://google.com") # open specific site
browser.maximize_window()
browser.get("https://github.com/")
time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a').click()
# time.sleep(2)
wait_login = EC.presence_of_element_located((By.ID, 'login_field'))
WebDriverWait(browser, timeout=20).until(wait_login)
login = browser.find_element(By.ID, 'login_field') # find the field of login
login.click() # click on login field
login.send_keys(details.mail)
password = browser.find_element(By.ID, 'password')
password.send_keys(details.password)
browser.find_element(By.NAME, 'commit').click()
time.sleep(2)
# try:
#     check = browser.find_element(By.CLASS_NAME, 'js-flash-alert')
# except:
#     print("the test failed")
#
# if check:
#     print("The test passed")
# else:
#     print("the test failed")

check = browser.find_element(By.CLASS_NAME, 'AppHeader-context-item-label  ')
if check:
    print("The test passed")
else:
    print("the test failed")

browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a').click()
repository = browser.find_element(By.ID, ':r5:')
repository.click() # not mandatory in many cases
repository.send_keys('kiruhs1')
time.sleep(3)
try:
    if browser.find_element(By.ID, 'RepoNameInput-message'):# negative test
        repository.send_keys('1')
    # browser.find_element(By.ID, 'RepoNameInput-is-available') # positive
    print("The test of checking of existing repository has passed")
    browser.find_element(By.XPATH, '//*[@id=":ra:"]').click()
    body = browser.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)
    # ActionChains(browser).send_keys(Keys.PAGE_DOWN)  # not relevant to this test
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button/span').click()
    time.sleep(5)

except:
    print("The test of checking of existing repository has failed")
    print("No success in creating repository")
finally:
    time.sleep(10)

try:
    assert browser.find_element(By.LINK_TEXT, 'kiruhs11')
    print("the repository was created successfully")
except:
    print("repository was not created")
finally:
    time.sleep(5)
browser.close() # close browser driver