import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string

def random_nrn():
    s = ""
    for x in range(5):
        n = random.randint(0, 9)
        s += str(n)
    return s

def random_name():
    s = ""
    c = list("äöüßàâæçéèêëïîôœÿüûùéëïóöü")
    for x in c:
        n = random.choice(c)
        s += str(n)
    return s

def random_phone():
    s = ""
    for x in range(7):
        n = random.randint(0, 9)
        s += str(n)
    return s

def random_passport():
    a = ""
    b = ""
    s = ""
    for x in range(5):
        n = random.randint(0, 9)
        a += str(n)
    for x in range(5):
        n = random.choice(string.ascii_letters)
        b += str(n)
    for x in range(random.randint(4, 6)):
        s += random.choice(a)
        s += random.choice(b)
    return s

print("Type office if using office ip")
ipused = input()

print("If you don't want bypass cookie, type no")
bypass = input()


print("Enter email wanted")
emailwanted = input()

print("Type BE or NONBE")
nrnstatus = input()

if nrnstatus in ("BE", "be", "Be"):
 print("Generated last 5 NRN numbers for BE")
 nrnwanted = random_nrn()

elif nrnstatus in ("NONBE", "nonbe", "non-be", "Nonbe"):
 idwanted = random_passport()
 print("Generated random passport/id between 7 and 12 characters")

print("Enter desired DOB: Day/Month/Year")
dobwanted = input()

print("Enter promo code")
promocode = input()

print("Type yes if you want validate in RMS/CMP")
rmsvalidate = input()

phonewanted = random_phone()
print(phonewanted)

name = random_name()
print(name)

stagelist = ('https://beta-dev.casino777.be/', 'https://beta-dev.casino777.be/en/', 'https://beta-dev.casino777.be/nl/', 'https://beta-dev.casino777.be/de/')
preprodlist = ('https://beta-pre-prod.casino777.be/', 'https://beta-pre-prod.casino777.be/nl/', 'https://beta-pre-prod.casino777.be/en/', 'https://beta-pre-prod.casino777.be/de/')
prodlist = ('https://www.casino777.be/', 'https://www.casino777.be/nl/', 'https://www.casino777.be/de/', 'https://www.casino777.be/en/')

print('''Enter one of the following and press enter: stage, prod, preprod''')
env = input()

if env in ('stage', 'Stage', 'STAGE', 'STage', 'STAGE'):
  website = random.choice(stagelist)
elif env in ('prod', 'Prod', 'PROD', 'PRod', 'PROD'):
  website = random.choice(prodlist)
elif env in ('preprod', 'pre-prod', 'Preprod', 'PRE-PROD', 'PRE-prod'):
  website = random.choice(preprodlist)



print("Select browser: Chrome, Firefox, Edge")
desiredbrowser = input()


if desiredbrowser == "Chrome" :
 driver = webdriver.Chrome()
elif desiredbrowser == "Firefox" :
 driver = webdriver.Firefox()
elif desiredbrowser == "Edge" :
 driver = webdriver.Edge()




driver.implicitly_wait(30)

'''Get initial access to Beta
 if ipused == "office":
 if website in stagelist:
  driver.get('https://beta-dev.casino777.be')
  UsernameAccess = driver.find_element(By.ID, "username")
  UsernameAccess.send_keys('test_loyalty22')
  CodeAccess = driver.find_element(By.ID, "code")
  CodeAccess.send_keys('HC1YC2')
  ActivateButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/button")
  ActivateButton.click()
  time.sleep(5)
 
 elif website in prodlist:
  driver.get('https://beta.casino777.be')
  UsernameAccess = driver.find_element(By.ID, "username")
  UsernameAccess.send_keys('test_games')
  CodeAccess = driver.find_element(By.ID, "code")
  CodeAccess.send_keys('4Z5PG5')
  ActivateButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/button")
  ActivateButton.click()
  time.sleep(5)'''
 

#Set BE GEO ip cookie if using office ip
if ipused == "office":
 if website in stagelist:
  driver.get('https://beta-dev.casino777.be/qasecrettool')
  driver.add_cookie({"name" : "dev_testIP", "value" : "5.23.255.255"})
  driver.get('https://rms-stage.casino777.be/')
  driver.add_cookie({"name" : "RMS_BYPASS_MAINTENANCE", "value" : "true"})
  driver.add_cookie({"name" : "RMS_LIVE_DEBUG", "value" : "true"})
  print("cookies were added")
 
 elif website in preprodlist:
  driver.get('https://beta-pre-prod.casino777.be/')
  driver.add_cookie({"name" : "dev_testIP", "value" : "5.23.255.255"})
  driver.get('https://bo.casino777.be')
  driver.add_cookie({"name" : "RMS_BYPASS_MAINTENANCE", "value" : "true"})
  driver.add_cookie({"name" : "RMS_LIVE_DEBUG", "value" : "true"})
  print("cookies were added")
 
 elif website in prodlist:
  driver.get('https://www.casino777.be/qasecrettool')
  driver.add_cookie({"name" : "dev_testIP", "value" : "5.23.255.255"})
  driver.get('https://bo.casino777.be')
  driver.add_cookie({"name" : "RMS_BYPASS_MAINTENANCE", "value" : "true"})
  driver.add_cookie({"name" : "RMS_LIVE_DEBUG", "value" : "true"})
  print("cookies were added")

else:
  if website in prodlist:
    driver.get('https://www.casino777.be')
    driver.add_cookie({"name" : "dev_testIP", "value" : "5.23.255.255"})
    driver.add_cookie({"name" : "bypassEGames", "value" : "true"})
    driver.get('https://bo.casino777.be')
    driver.add_cookie({"name" : "RMS_BYPASS_MAINTENANCE", "value" : "true"})
    driver.add_cookie({"name" : "RMS_LIVE_DEBUG", "value" : "true"})
    print("cookies were added")
    
  elif website in stagelist:
    driver.get('https://beta-dev.casino777.be')
    driver.add_cookie({"name" : "dev_testIP", "value" : "5.23.255.255"})
    driver.add_cookie({"name" : "bypassEGames", "value" : "true"})
    driver.get('https://rms-stage.casino777.be/')
    driver.add_cookie({"name" : "RMS_BYPASS_MAINTENANCE", "value" : "true"})
    driver.add_cookie({"name" : "RMS_LIVE_DEBUG", "value" : "true"})
    print("cookies were added")

#Set bypass cookie for BE user
if nrnstatus in ("BE", "be", "Be") and ipused == "office":
 if website in stagelist:
  driver.get('https://beta-dev.casino777.be/qasecrettool')
  driver.add_cookie({"name" : "bypassEGames", "value" : "true"})
 
 elif website in preprodlist:
  driver.get('https://beta-pre-prod.casino777.be/qasecrettool')
  driver.add_cookie({"name" : "bypassEGames", "value" : "true"})
 
 elif website in prodlist:
  driver.get('https://www.casino777.be/qasecrettool')
  driver.add_cookie({"name" : "bypassEGames", "value" : "true"})


#Puts the bypass recaptcha cookie
if website in stagelist and bypass != "no" :
      driver.get("https://beta-dev.casino777.be/qa_test")
      GenerateCookieButton = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/button[1]")
      GenerateCookieButton.click()
      time.sleep(5)
      
elif website in preprodlist and bypass != "no":
      driver.get("https://beta-pre-prod.casino777.be/qa_test")
      GenerateCookieButton = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/button[1]")
      GenerateCookieButton.click()
      time.sleep(5)
      
elif website in prodlist and bypass != "no":
      driver.get("https://www.casino777.be/qa_test")
      GenerateCookieButton = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/button[1]")
      GenerateCookieButton.click()
      time.sleep(5)
    

#Goes to the website and refreshes
driver.get(website)
driver.maximize_window()
driver.refresh()

#Dismiss Didomi cookie popup
driver.find_element(By.ID, "didomi-notice-agree-button").click()

#Triggers register

registerbutton = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/header/div[1]/div[2]/button[3]");
registerbutton.click()
time.sleep(5)
 
#SelectsManualRegistration
ManualRegistration = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/button[2]")
ManualRegistration.click()

#Step 1 registration
time.sleep(10)
entermail = driver.find_element(By.ID, 'email')
entermail.send_keys("1" +emailwanted + "@yopmail.com")
enterpassword = driver.find_element(By.ID, 'password')
enterpassword.send_keys("sJgimo777")
checkpreferences = driver.find_element(By.ID, 'consent_marketing')
checkpreferences.click()


#Clicks Next to reach step 2
nextbutton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/button")
nextbutton.click()


#Step 2 registration
firstname = driver.find_element(By.ID, "first_name")
firstname.send_keys(name)

name = random_name()
print(name)

secondname = driver.find_element(By.ID, "last_name")
secondname.send_keys(name)


                 
dob = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[4]/div[1]/div[1]/div/input")
dob.send_keys("0" + dobwanted)

nrn = driver.find_element(By.ID, "nrn_passport_field")

if nrnstatus in ("BE", "be", "Be"):
 nrn.send_keys(nrnwanted)
 
else:
  NationalityField = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div[1]/div")
  NationalityField.click()
  SearchNationality = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div[2]/div/input")
  SearchNationality.send_keys("Liechtenstein")
  SelectNationality = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div[2]/div/div/h6")
  SelectNationality.click()
  nrn.send_keys(idwanted)
  
 
  

nextbutton.click()


#Step 3 registration

address = driver.find_element(By.ID, 'address')
address.send_keys('Street 12')

postcode = driver.find_element(By.ID, 'postcode')
postcode.send_keys('1356')

town = driver.find_element(By.ID, 'town')
town.send_keys('Liege')

phone = driver.find_element(By.ID, "mobile_phone")
phone.send_keys(phonewanted)

 
nextbutton.click()

#Step 4 registration

username = driver.find_element(By.ID, "username")
time.sleep(5)
username.send_keys(Keys.CONTROL + 'a')
username.send_keys(Keys.DELETE)
username.send_keys(emailwanted)
promocodefield = driver.find_element(By.ID, "promo_code")
promocodefield.click()
promocodefield.send_keys(promocode)

tos = driver.find_element(By.ID, "tos")
tos.click()

#Confirms register
confirmbutton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/button[1]")
confirmbutton.click()
time.sleep(10)


#Logs in to RMS and validates user:


if website in stagelist and rmsvalidate in ("Yes", "yes"):
    driver.get("https://rms-stage.casino777.be/")
    driver.implicitly_wait(30)
    Username = driver.find_element(By.ID, "user")
    Username.send_keys("mihai_andronie")
    Password = driver.find_element(By.ID, "pass")
    Password.send_keys("173467321476Charlie")
    LoginButton = driver.find_element(By.NAME, "auth_feature")
    LoginButton.click()
    driver.get("https://rms-stage.casino777.be/index.php?op=31")
    LoginSearch = driver.find_element(By.NAME, "Account")
    SearchButton = driver.find_element(By.NAME, "action")
    LoginSearch.send_keys(emailwanted)
    SearchButton.click()
    UserID = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]").text
    print(UserID)
    driver.get(f"https://rms-stage.casino777.be/index.php?op=31&action=information&id={UserID}")
    SelectNationality = Select(driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[3]/form/table[1]/tbody/tr[31]/td[2]/select"))
    SelectNationality.select_by_value('1')
    PressOK = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[3]/form/table[1]/tbody/tr[31]/td[2]/input")
    PressOK.click()
    driver.switch_to.alert.accept()
    
elif website in (prodlist + preprodlist) and rmsvalidate in ("Yes", "yes"):
    driver.get("https://bo.casino777.be/")
    driver.implicitly_wait(30)
    Username = driver.find_element(By.ID, "user")
    Username.send_keys("mihai_andronie")
    Password = driver.find_element(By.ID, "pass")
    Password.send_keys("173467321476Charlie")
    LoginButton = driver.find_element(By.NAME, "auth_feature")
    LoginButton.click()
    driver.get("https://bo.casino777.be/index.php?op=31")
    LoginSearch = driver.find_element(By.NAME, "Account")
    SearchButton = driver.find_element(By.NAME, "action")
    LoginSearch.send_keys(emailwanted)
    SearchButton.click()
    UserID = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]").text
    print(UserID)
    driver.get(f"https://bo.casino777.be/index.php?op=31&action=information&id={UserID}")
    SelectNationality = Select(driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[3]/form/table[1]/tbody/tr[31]/td[2]/select"))
    SelectNationality.select_by_value('1')
    PressOK = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div[3]/form/table[1]/tbody/tr[31]/td[2]/input")
    PressOK.click()
    driver.switch_to.alert.accept()  

    
 


