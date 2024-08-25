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
host = "189.240.60.164"
port = "9090"
# 189.240.60.164:9090 mx
# 200.174.198.86:8888 br
# 177.23.176.58:8080 br
email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMISTADES Y OTROS', 'ENTRA', 'ENTREN GUAPOS', 'ENTRA TE ESPERO :)', 'VIRTUALITOS', 'AMISTADES SUDAMERICA', 'ENTRA AMOR', 'ENTRA AQUI :)', 'ENTREN ENTREN', 'VIRTUALITOS 2024']
group_link = "https://chat.whatsapp.com/KbrxPxeqIDCHUUdYUoPJMG"

def automate():
    try:
        options = webdriver.ChromeOptions()
        #mobile_emulation = { "deviceName": "Nexus 7" }
        #user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        #options.add_argument(f'user-agent={user_agent}')
        options.add_extension('proxy.crx')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #options.add_experimental_option("mobileEmulation", mobile_emulation)
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
        driver.get("chrome-extension://iejkjpdckomcjdhmkemlfdapjodcpgih/data/popup/popup.html")
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div/details[5]/summary').click()
        driver.find_element(By.XPATH,'//*[@id="http-host"]').send_keys(host)
        driver.find_element(By.XPATH,'//*[@id="http-port"]').send_keys(port)
        driver.find_element(By.XPATH,'//*[@id="single"]').click()
        driver.find_element(By.XPATH,'/html/body/div/details[5]/table/tbody/tr[1]/td[1]').click()
        time.sleep(15)
        driver.get("https://www.gruposwats.com")
        time.sleep(5)
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
                print("cookies salvos foram restaurados! - ", dt_string)
        except (OSError, IOError) as e:
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
            print("criando novos cookies no banco de dados... - ", dt_string)
                
        driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
        driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[2]/input').send_keys("Amistades")
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

