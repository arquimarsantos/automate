from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
group_names = ['AMISTADES & STICKERS ENTREN', 'ENTRA BB', 'ENTREN GUAPOS', 'ENTRA AMOR TE ESPERO', 'VIRTUALITOS']
group_link = "https://chat.whatsapp.com/IiCl4YhSt1qHduNAW7IWWZ"

def automate():
    try:
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36' 
        options.add_extension('urban.crx')
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
        driver = webdriver.Chrome(options=options)
        dtime = datetime.now()
        dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
        names = random.choice(group_names)
        print("Automação iniciada! - ", dt_string)
        driver.get('chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent')
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/button[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/button[2]').click()
        driver.get('chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html')
        time.sleep(10)
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/input').click()
        time.sleep(5)
        br_button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/ul[2]/li[8]/p')
        time.sleep(5)
        ActionChains(driver).move_to_element(br_button).click(br_button).perform()
        time.sleep(5)
        driver.get("https://www.gruposwats.com")
        driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
        driver.find_element(By.XPATH, '//*[@id="myDiv3"]/span[6]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="mailgrupo"]').click()
        driver.find_element(By.XPATH, '//*[@id="mailgrupo"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="FRMgest"]/button').click()
        #time.sleep(10)
        with MailBox('imap.gmail.com').login(email, password) as mailbox:
            for msg in mailbox.fetch(limit=1, reverse=True, mark_seen=True):
                uids = []
                if (msg.from_ != "info@gruposwats.com"):
                    print("Email selecionado não é válido com a automação, reiniciando sistema... - ", dt_string)
                    uids.append(msg.uid)
                    mailbox.delete(uids)
                    return automate()
                    
                body = msg.text or msg.html
                extractor = URLExtract()
                url = extractor.find_urls(body)
                first_url = url[0]
                print("==================================================\n\nDe: ", msg.from_, "\nPara: ", msg.to, "\nAssunto: ", msg.subject, "\nData: ", msg.date, "\nUID: ", msg.uid, "\n\nMensagem: \n\n", body)
                driver.get(first_url)
                time.sleep(5)
                check = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[1]/span[5]')
                state = "Estado: *** en revisión ***"
                if state in check.text:
                    uids.append(msg.uid)
                    mailbox.delete(uids)
                    driver.quit()
                    return print("O grupo segue em revisão, por isso a automação será cancelada. - ", dt_string)
                    
                driver.find_element(By.XPATH, '//*[starts-with(@id,"btn")]/input').click()
                time.sleep(5)
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
                driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
                driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[2]/input').send_keys(names)
                driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[3]/input').send_keys(group_link)
                driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[5]/div/input[2]').click()
                driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[6]/div/input[1]').send_keys("arquimarsx@gmail.com")
                driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[6]/div/input[2]').send_keys("arquimarsx@gmail.com")
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
                driver.find_element(By.XPATH, '//*[@id="frmALTA2"]/button[1]').click()
                time.sleep(5)
                uids.append(msg.uid)
                mailbox.delete(uids)
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

