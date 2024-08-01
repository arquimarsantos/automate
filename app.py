from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
import os
import time
import random
from datetime import datetime

app = Flask(__name__)

def automate():
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.set_capability("loggingPrefs", {'performance': 'ALL'})
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--headless")
            service = ChromeService(executable_path'/usr/local/bin/chromedriver')
            driver = webdriver.Chrome(service=service, options=options)
            dtime = datetime.now()
            dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
            groupNames = ['AMISTADES & STICKERS ENTREN', 'ENTRA BB', 'ENTREN GUAPOS', 'ENTRA AMOR TE ESPERO', 'VIRTUALITOS']
            names = random.choice(groupNames)
            groupLink = "https://chat.whatsapp.com/HcggDDBEURG6jhillSbv7L"
            driver.get("https://www.google.com")
            time.sleep(10)
            driver.find_element("xpath", '//*[@id="gb"]/div/div[2]/a').click()
            driver.find_element("xpath", '//*[@id="identifierId"]').send_keys("arquimarsx@gmail.com")            
            driver.find_element("xpath", '//*[@id="identifierNext"]/div/button/span').click()
            time.sleep(10)
            driver.find_element("xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("13421822$$")
            driver.find_element("xpath", '//*[@id="passwordNext"]/div/button/span').click()
            time.sleep(10)
            driver.get("https://www.gruposwats.com")
            driver.find_element("xpath", '//*[@id="btnpublica"]').click()
            driver.find_element("xpath", '//*[@id="myDiv3"]/span[6]').click()
            driver.find_element("xpath", '/html/body/div[2]/div/div[1]/button').click()
            driver.find_element("xpath", '//*[@id="mailgrupo"]').click()
            driver.find_element("xpath", '//*[@id="mailgrupo"]').send_keys("arquimarsx@gmail.com")
            driver.find_element("xpath", '//*[@id="FRMgest"]/button').click()
            time.sleep(5) 
            driver.get("https://www.google.com")
            time.sleep(300)
            driver.get("https://mail.google.com/mail/u/0/#inbox")
            time.sleep(10)
            driver.find_element("xpath", '//*[@id=":2a"]').click()
            time.sleep(10)
            txt = driver.find_element("link text", 'Clic para gestionar tus anuncios')
            url = txt.get_attribute("href")
            driver.get(url)
            time.sleep(10)
            try:
                driver.switch_to.alert
                print("Alerta detectado, aceitando... - ", dt_string)
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
            except NoAlertPresentException:
                print("Sem presença de alerta, continuando... - ", dt_string)
                
            time.sleep(10)
            driver.find_element("xpath", '//*[starts-with(@id,"btn")]/input').click()
            time.sleep(10)
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            driver.find_element("xpath", '//*[@id="btnpublica"]').click()
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[2]/input').send_keys(names)
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[3]/input').send_keys(groupLink)
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[5]/div/input[2]').click()
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[6]/div/input[1]').send_keys("arquimarsx@gmail.com")
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[6]/div/input[2]').send_keys("arquimarsx@gmail.com")
            driver.find_element("xpath", '//*[@id="descripcion"]').send_keys("Grupo para hacer amistades, parejas, stickers, y más... entra y desfruta!")
            driver.find_element("xpath", '//*[@id="keys"]').send_keys("amistad, amigos, humor, memes, ciudad, argentina, colombia, peru, perú, mexico, méxico")
            driver.find_element("xpath", '//*[@id="cat1"]').click()
            driver.find_element("xpath", '//*[@id="cat1"]/option[2]').click()
            driver.find_element("xpath", '//*[@id="cat2"]').click()
            driver.find_element("xpath", '//*[@id="cat2"]/option[3]').click()
            driver.find_element("xpath", '//*[@id="cat3"]').click()
            driver.find_element("xpath", '//*[@id="cat3"]/option[4]').click()
            driver.find_element("xpath", '//*[@id="privacidad"]').click()
            driver.find_element("xpath", '//*[@id="frmALTA1"]/div[11]/div/a').click()
            time.sleep(10)
            driver.find_element("xpath", '//*[@id="frmALTA2"]/button[1]').click()
            time.sleep(10)
            driver.get("https://mail.google.com/mail/u/0/#inbox")
            time.sleep(10)
            driver.find_element("xpath", '//*[@id=":2c"]').click()
            time.sleep(5)
            driver.find_element("xpath", '//*[@id=":4"]/div/div[1]/div[1]/div/div/div[2]/div[3]').click()
            time.sleep(5)
            driver.find_element("xpath", '//*[@id=":ld"]').click()
            driver.find_element("xpath", '//*[@id=":lu"]/div').click()
            time.sleep(10)
            driver.find_element("xpath", '//*[@id=":mz"]/div[1]/span').click()
            driver.find_element("xpath", '//*[@id=":4"]/div[2]/div[2]/div[1]/div/div/div[2]/div/div').click()
            driver.quit()
            print("Automação concluída com sucesso! - ", dt_string)
            time.sleep(3300)
        except Exception as e: 
            print (e)
            automate()


@app.route('/home', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return automate()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
