from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from flask import Flask
from imap_tools import MailBox
from urlextract import URLExtract
import time
import random
from datetime import datetime

app = Flask(__name__)
email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMOR Y AMISTAD', 'ENTRA', 'ENTREN GUAPOS', 'ENTRA TE ESPERO :)', 'VIRTUALITOS', 'AMISTADES SUDAMERICA', 'ENTRA AMOR', 'ENTRA AQUI :)', 'ENTREN ENTREN', 'VIRTUALITOS 2024']
group_link = "https://chat.whatsapp.com/KbrxPxeqIDCHUUdYUoPJMG"
#proxy = "189.240.60.164:9090"

def automate():
    try:
        options = webdriver.ChromeOptions()
        #user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'
        mobile_emulation = { "deviceName": "Nexus 7" }
        #options.add_argument(f'user-agent={user_agent}')
        #options.add_argument(f"--proxy-server={proxy}")
        #options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        dtime = datetime.now()
        dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
        names = random.choice(group_names)
        print("Automação iniciada! - ", dt_string)
        driver.get("https://www.gruposwats.com")
        driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[2]/input').send_keys(names)
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[3]/input').send_keys(group_link)
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[5]/div/input[2]').click()
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[6]/div/input[1]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[6]/div/input[2]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="descripcion"]').send_keys("Grupo para hacer amistades, parejas, stickers, y más... entra y desfruta!")
        driver.find_element(By.XPATH, '//*[@id="keys"]').send_keys("amistad, amigos, humor, memes, ciudad, argentina, colombia, peru, perú, mexico, méxico")
        driver.find_element(By.XPATH, '//*[@id="cat1"]').click()
        driver.find_element(By.XPATH, '//*[@id="cat1"]/option[2]').click()
        driver.find_element(By.XPATH, '//*[@id="cat2"]').click()
        driver.find_element(By.XPATH, '//*[@id="cat2"]/option[3]').click()
        driver.find_element(By.XPATH, '//*[@id="cat3"]').click()
        driver.find_element(By.XPATH, '//*[@id="cat3"]/option[4]').click()
        driver.find_element(By.XPATH, '//*[@id="privacidad"]').click()
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[11]/div/a').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="frmALTA2"]/a[1]').click()
        time.sleep(5)
        driver.quit()
        print("Automação concluída com sucesso! - ", dt_string)
    except Exception as e:
        print(e)
        

@app.route('/')
def index():
    automate()
    return 'Automação ativada!'


if __name__ == '__main__':
    app.run()

