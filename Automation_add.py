from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from oauth2client.service_account import ServiceAccountCredentials
import gspread, time
import constants as c
###
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(c.driverPath,chrome_options=chrome_options)
###
driver = webdriver.Chrome(c.driverPath)
driver.get('http://www.google.com/xhtml');
driver.get(c.gLink)
driver.find_element_by_name(c.identifierElement).send_keys(c.gmailId)
driver.find_element_by_xpath(c.xpathNext).click()
driver.implicitly_wait(10)
driver.find_element_by_name(c.passElement).send_keys(c.gmailPass)
driver.find_element_by_xpath(c.xpathLogin).click()
driver.get(c.ssUrl)
time.sleep(4)
driver.implicitly_wait(15)
creds = ServiceAccountCredentials.from_json_keyfile_name(c.json, c.ssApi)
client = gspread.authorize(creds)
sheet = client.open(c.ssName).worksheet(c.sName)
sheet.insert_row(c.data2Insert, c.insertIndex)
time.sleep(5)
driver.get(c.ssUrl)
time.sleep(15)
driver.find_element_by_xpath(c.xpathSsTools).click()  
driver.implicitly_wait(20)
driver.find_element_by_xpath(c.xpathSsToolsScriptEditor).click()
time.sleep(15)
driver.switch_to.window(driver.window_handles[-1])  
driver.find_element_by_xpath(c.xpathGsPublish).click() 
driver.find_element_by_xpath(c.xpathGsDeploy).click() 
driver.find_element_by_xpath(c.xpathGsWebNew).click()
time.sleep(10)
driver.find_element_by_xpath(c.xpathGsUpdate).click() 
driver.implicitly_wait(20)
time.sleep(10)
driver.find_element_by_xpath(c.xpathGsLatestC).click()
time.sleep(20)
driver.quit()
