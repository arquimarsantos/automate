from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from flask import Flask
from imap_tools import MailBox
from urlextract import URLExtract
import time
import pickle
import random
from datetime import datetime

app = Flask(__name__)
email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMISTADES Y OTROS', 'ENTRA', 'ENTREN GUAPOS', 'ENTRA TE ESPERO :)', 'VIRTUALITOS', 'AMISTADES SUDAMERICA', 'ENTRA AMOR', 'ENTRA AQUI :)', 'ENTREN ENTREN', 'VIRTUALITOS 2024']
group_link = "https://chat.whatsapp.com/KbrxPxeqIDCHUUdYUoPJMG"

def automate():
    try:
        options = webdriver.ChromeOptions()
        mobile_emulation = { "deviceName": "iPhone X" }
        #user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        #options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--user-data-dir=selenium")
        options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        dtime = datetime.now()
        dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
        names = random.choice(group_names)
        driver.get('https://api.ipify.org/')
        ip_address = driver.find_element(By.TAG_NAME, "body").text
        print(ip_address)
    except Exception as e:
        print(e)
        

@app.route('/')
def index():
    automate()
    return 'Automação ativada!'


if __name__ == '__main__':
    app.run()

