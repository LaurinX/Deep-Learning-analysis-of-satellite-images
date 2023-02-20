from selenium import webdriver         #für das Scraping
from selenium.webdriver.common.by import By
from time import sleep      

driver = webdriver.Chrome(r'C:\Users\Anwender\Documents\ChromeDriver\chromedriver.exe')         #Pfad des Webdrivers
driver.maximize_window()
driver.get('https://www.google.de/maps/@52.5264131,13.4153769,40460m/data=!3m1!1e3!5m1!1e4')

def decline_cookies():
    cookies = driver.find_element(By.CLASS_NAME, "lssxud")
    cookies.click()

decline_cookies()

def search_place():
    place = driver.find_element(By.CLASS_NAME, "tactile-searchbox-input")
    place.send_keys('Marzahner Chaussee')
    submit = driver.find_element(By.CLASS_NAME, "mL3xi")
    submit.click()

search_place()

sleep(3)

def close_search():
    close = driver.find_element(By.CLASS_NAME, "gsst_a")
    close.click()

close_search()

driver.save_screenshot("image.png")

#bis hier funktioniert alles einwandfrei, das andere muss ich noch verbessern

def hide_labels():
    layers = driver.find_element(By.CLASS_NAME, "yHc72 qk5Wte")
    layers.click()
    more = driver.find_element(By.CLASS_NAME, "hYkU8c")
    more.click()
    hide = driver.find_element(By.CLASS_NAME, "xXq44b iBueH")
    hide.click()

hide_labels()



