from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
from imap_tools import MailBox
from urlextract import URLExtract
import time
import random
from datetime import datetime

app = Flask(__name__)
email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMISTADES & STICKERS ENTREN', 'ENTRA BB', 'ENTREN GUAPOS', 'ENTRA AMOR TE ESPERO', 'VIRTUALITOS']
group_link = "https://chat.whatsapp.com/BZ3YQdAR3TjKrgBtBbz7Lk"
proxy = "200.174.198.86:8888"

def automate():
    try:
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36' 
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f"--proxy-server={proxy}")
        driver = webdriver.Chrome(options=options)
        dtime = datetime.now()
        dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
        names = random.choice(group_names)
        print("Automação iniciada! - ", dt_string)
        driver.get("https://www.gruposwats.com")
        driver.find_element("xpath", '//*[@id="btnpublica"]').click()
        driver.find_element("xpath", '//*[@id="myDiv3"]/span[6]').click()
        driver.find_element("xpath", '/html/body/div[2]/div/div[1]/button').click()
        driver.implicitly_wait(10)
        driver.find_element("xpath", '//*[@id="mailgrupo"]').click()
        driver.find_element("xpath", '//*[@id="mailgrupo"]').send_keys(email)
        driver.find_element("xpath", '//*[@id="FRMgest"]/button').click()
        time.sleep(5)
        with MailBox('imap.gmail.com').login(email, password) as mailbox:
            for msg in mailbox.fetch(limit=1, reverse=True, mark_seen=True):
                if (msg.from_ != "info@gruposwats.com"):
                    print("Email selecionado não é válido com a automação, reiniciando sistema... - ", dt_string)
                    return automate()                
                body = msg.text or msg.html
                extractor = URLExtract()
                url = extractor.find_urls(body)
                first_url = url[0]
                print("==================================================\n\nDe: ", msg.from_, "\nPara: ", msg.to, "\nAssunto: ", msg.subject, "\nData: ", msg.date, "\nUID: ", msg.uid, "\n\nMensagem: \n\n", body)
                driver.get(first_url)
                driver.find_element("xpath", '//*[starts-with(@id,"btn")]/input').click()
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
                driver.find_element("xpath", '//*[@id="btnpublica"]').click()
                driver.find_element("xpath", '//*[@id="frmALTA1"]/div[2]/input').send_keys(names)
                driver.find_element("xpath", '//*[@id="frmALTA1"]/div[3]/input').send_keys(group_link)
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
                driver.implicitly_wait(10)
                driver.find_element("xpath", '//*[@id="frmALTA2"]/button[1]').click()
                driver.implicitly_wait(5)
                uids = []
                uids.append(msg.uid)
                mailbox.delete(uids)
                driver.implicitly_wait(5)
                driver.quit()
                print("Automação concluída com sucesso! - ", dt_string)
    except Exception as e:
        print(e)
        automate()
        

@app.route('/')
def index():
    automate()
    return 'Automação ativada!'


if __name__ == '__main__':
    app.run()
