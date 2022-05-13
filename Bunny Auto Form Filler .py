import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

if __name__ == "__main__":

    #IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
    #sudo apt-get install chromium-chromedriver
    browser_driver = Service('C:/Users/schoo/Downloads/chromedriver_win32/chromedriver.exe')
    page_to_scrape = webdriver.Chrome(service=browser_driver)
    page_to_scrape.get("https://www.bluecloverrabbitry.com/store/p319/Bunny_Reservations.html#/")

    # page_to_scrape.find_element(By.LINK_TEXT, "Login").click()
    #click bunny name

    page_to_scrape.find_element(By.XPATH,'''//*[@id="wsite-com-product-options"]/div/div/label[3]''').click() #bunny 

    page_to_scrape.find_element(By.CLASS_NAME, "wsite-com-product-modifier-label").click() # i agree policy 
    page_to_scrape.find_element(By.XPATH, '''//*[@id="wsite-com-product-modifiers"]/div/div[2]/label[3]''').click() # i agree reading 

    page_to_scrape.find_element(By.XPATH,'''//*[@id="wsite-com-product-modifiers"]/div/div[3]/label[12]''').click() #airport


    page_to_scrape.find_element(By.XPATH,'''//*[@id="wsite-com-product-modifiers"]/div/div[4]/label[3]''').click()#personal delivery quote


    shipping = page_to_scrape.find_element(By.ID, "wsite-com-product-modifier-11ec593a7940a2d6a53682379b181de5")
    shipping.send_keys("ship")

    firstlastname = page_to_scrape.find_element(By.ID,"wsite-com-product-modifier-11ec593a794487029e4f82379b181de5")
    firstlastname.send_keys("Brittany Mar")

    address = page_to_scrape.find_element(By.ID,"wsite-com-product-modifier-11ec593a79434522a09182379b181de5") 
    address.send_keys('320 East Graves Monterey Park 91755')

    page_to_scrape.find_element(By.ID, "wsite-com-product-add-to-cart").click()

    # page_to_scrape.find_element(By.XPATH,'''//*[@id="wsite-com-minicart-checkout-button"]''').click()
    time.sleep(2)

    page_to_scrape.find_element(By.ID, "wsite-com-minicart-checkout-button").click() 

    time.sleep(1)

    page_to_scrape.find_element(By.CLASS_NAME,"wsite-button-inner").click()

    time.sleep(1) #pause to load final checkout page 

    email = page_to_scrape.find_element(By.NAME, '''email''')
    email.send_keys('breemar14@gmail.com')

    firstname = page_to_scrape.find_element(By.NAME, "name_first") 
    firstname.send_keys('Brittany')

    lastname = page_to_scrape.find_element(By.NAME, "name_last") 
    lastname.send_keys('Mar')

    addressline1 = page_to_scrape.find_element(By.NAME, '''street''')
    addressline1.send_keys('320 E Graves Ave')

    city = page_to_scrape.find_element(By.NAME, '''city''')
    city.send_keys('Monterey Park')


    city = page_to_scrape.find_element(By.NAME, '''phone''')
    city.send_keys('6266320067')

    zipcode = page_to_scrape.find_element(By.NAME, '''postal_code''')
    zipcode.send_keys('91755')

    select = Select(page_to_scrape.find_element(By.NAME,'region'))
    select.select_by_value('CA')

    # page_to_scrape.find_element(By.CLASS_NAME,"wsite-button-inner").click()

    page_to_scrape.find_element(By.XPATH, '''//*[@id="wsite-content"]/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[3]/fieldset/button''').click()

    time.sleep(1)
    page_to_scrape.find_element(By.XPATH, '''//*[@id="wsite-content"]/div/div[1]/div/div[3]/div[2]/div/div[2]/div/section/form/fieldset/section/button''').click()


# cardnumber = page_to_scrape.find_element(By.ID,"sq-input--cardNumber") 
# cardnumber.sendkeys('1231231231321')
# cardnumber = page_to_scrape.find_element(By.XPATH, '''//*[@id="sq-input--cardNumber"]''')
# cardnumber.send_keys('5524336577968708')

# expdate = page_to_scrape.find_element(By.ID, 'sq-input--expirationDate')
# expdate.send_keys('1024')

# cvv = page_to_scrape.find_element(By.ID, 'sq-input--cvv') 
# cvv.send_keys('467')

# zipcode2 = page_to_scrape.find_element(By.ID, 'sq-input--postalCode') 
# zipcode2.send_keys('91803')

# page_to_scrape.find_element(By.XPATH,'''//*[@id="wsite-content"]/div/div[1]/div/div[3]/div[2]/div/div[4]/div/section[4]/div/div[3]/button''').click() 