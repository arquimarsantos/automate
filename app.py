from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imap_tools import MailBox
from urlextract import URLExtract
import time
import random
from datetime import datetime

email = "arquimarsx@gmail.com"
password = "szgcbdzxgjkzggbq"
group_names = ['AMISTADES & STICKERS ENTREN', 'ENTRA BB', 'ENTREN GUAPOS', 'ENTRA AMOR TE ESPERO', 'VIRTUALITOS']
group_link = "https://chat.whatsapp.com/KFxBPIgH2ad1Shi14KcJB2"

def automate():
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument('--disable-gpu')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            dtime = datetime.now()
            dt_string = dtime.strftime("%d/%m/%Y %H:%M:%S")
            names = random.choice(group_names)
            print("Automação iniciada! - ", dt_string)
            driver.get("https://www.gruposwats.com")
            driver.find_element("xpath", '//*[@id="btnpublica"]').click()
            driver.find_element("xpath", '//*[@id="myDiv3"]/span[6]').click()
            driver.find_element("xpath", '/html/body/div[2]/div/div[1]/button').click()
            driver.find_element("xpath", '//*[@id="mailgrupo"]').click()
            driver.find_element("xpath", '//*[@id="mailgrupo"]').send_keys(email)
            driver.find_element("xpath", '//*[@id="FRMgest"]/button').click()
            time.sleep(5)
            driver.get("https://www.google.com")
            time.sleep(290)
            with MailBox('imap.gmail.com').login(email, password) as mailbox:
                for msg in mailbox.fetch(limit=1, reverse=True, mark_seen=True):
                    time.sleep(10)
                    if (msg.from_ != "info@gruposwats.com"):
                        print("Email selecionado não é válido com a automação, reiniciando sistema... - ", dt_string)
                        automate()
                        
                    body = msg.text or msg.html
                    extractor = URLExtract()
                    url = extractor.find_urls(body)
                    first_url = url[0]
                    print("==================================================\n\nDe: ", msg.from_, "\nPara: ", msg.to, "\nAssunto: ", msg.subject, "\nData: ", msg.date, "\nUID: ", msg.uid, "\n\nMensagem: \n\n", body)
                    driver.get(first_url)
                    time.sleep(10)
                    driver.find_element("xpath", '//*[starts-with(@id,"btn")]/input').click()
                    time.sleep(10)
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
                    time.sleep(10)
                    driver.find_element("xpath", '//*[@id="frmALTA2"]/button[1]').click()
                    time.sleep(10)
                    uids = []
                    uids.append(msg.uid)
                    mailbox.delete(uids)
                    driver.quit()
                    print("Automação concluída com sucesso! - ", dt_string)
                    time.sleep(3300)
        except Exception as e:
            print (e)
            automate()


automate()
