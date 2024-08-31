from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from flask import Flask
from imap_tools import MailBox
from urlextract import URLExtract
import time
#import pickle
import random
from datetime import datetime

app = Flask(__name__)
email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMISTADES Y OTROS', 'ENTRA', 'ENTREN GUAPOS', 'ENTRA TE ESPERO :)', 'VIRTUALITOS', 'AMISTADES SUDAMERICA', 'ENTRA AMOR', 'ENTRA AQUI :)', 'ENTREN ENTREN', 'VIRTUALITOS 2024']
group_link = "https://chat.whatsapp.com/KbrxPxeqIDCHUUdYUoPJMG"
host = "74.119.144.60"
port = "4145"
# 189.240.60.164:9090 mx
# 189.240.60.169:9090 mx
# 200.174.198.86:8888 br
# 172.233.155.25:1080 us socks5
# 199.229.254.129:4145 us socks5
# 74.119.144.60:4145 us socks5

def automate():
    try:
        options = webdriver.ChromeOptions()
        #mobile_emulation = { "deviceName": "iPhone X" }
        #user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        #options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_extension('proxy.crx')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--user-data-dir=selenium")
        options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        #options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        dtime = datetime.now()
        dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
        names = random.choice(group_names)
        print("Automação iniciada! - ", dt_string)
        driver.get("chrome-extension://iejkjpdckomcjdhmkemlfdapjodcpgih/data/popup/popup.html")
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div/details[5]/summary').click()
        #driver.find_element(By.XPATH,'//*[@id="socks5-scheme"]').click()
        protocol_bt = driver.find_element(By.XPATH,'//*[@id="socks5-scheme"]')
        ActionChains(driver).move_to_element(protocol_bt).click(protocol_bt).perform()
        driver.find_element(By.XPATH,'//*[@id="http-host"]').send_keys(host)
        driver.find_element(By.XPATH,'//*[@id="http-port"]').send_keys(port)
        driver.find_element(By.XPATH,'//*[@id="single"]').click()
        driver.find_element(By.XPATH,'/html/body/div/details[5]/table/tbody/tr[1]/td[1]').click()
        time.sleep(15)
        driver.get("https://www.gruposwats.com")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
        driver.find_element(By.XPATH, '//*[@id="myDiv3"]/span[6]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="mailgrupo"]').click()
        driver.find_element(By.XPATH, '//*[@id="mailgrupo"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="FRMgest"]/button').click()
        time.sleep(5)
        check_account = driver.find_element(By.XPATH, '//*[@id="gestgrupo"]/span')
        state_account = ". Email no correcto"
        if state_account in check_account.text:
            print("Não foi encontrado conta criada para o email: ", email, "\npublicando um novo grupo... - ", dt_string)
            driver.get("https://www.gruposwats.com")
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="btnpublica"]').click()
            driver.find_element(By.XPATH, '//*[@id="frmALTA1"]/div[2]/input').send_keys("aprueben mi grupo :(")
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
            return print("Automação concluída com sucesso! - ", dt_string)
        
        time.sleep(10)
        with MailBox('imap.gmail.com').login(email, password) as mailbox:
            for msg in mailbox.fetch(limit=1, reverse=True, mark_seen=True):
                uids = []
                if (msg.from_ != "info@gruposwats.com"):
                    print("Email selecionado não é válido com a automação, reiniciando sistema... - ", dt_string)
                    return automate()
                    
                body = msg.text or msg.html
                extractor = URLExtract()
                url = extractor.find_urls(body)
                first_url = url[0]
                print("==================================================\n\nDe: ", msg.from_, "\nPara: ", msg.to, "\nAssunto: ", msg.subject, "\nData: ", msg.date, "\nUID: ", msg.uid, "\n\nMensagem: \n\n", body)
                driver.get(first_url)
                #time.sleep(10)
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

