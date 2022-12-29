import time, os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

load_dotenv()

texts = "paraphrase thirty times the following sentence where is the movie theater?"
email = os.getenv('email')
password = os.getenv('password')

driver = uc.Chrome()
url = "https://chat.openai.com/chat"

driver.get(url)
driver.maximize_window()


WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > div > div.flex.flex-row.gap-3 > button:nth-child(1)'))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/section/div/div/div/div[3]/form[1]/button'))).click()


WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'identifierId'))).send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
time.sleep(2)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))).send_keys(password)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button'))).click()
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]'))).click()
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]'))).click()



for i in range(1,60,2):

    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/form/div/div[2]/textarea').send_keys(texts)
    driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[2]/form/div/div[2]/button').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/main/div[2]/form/div/div[1]')))

    inputs1=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[1]/div/div/div/div['+str(i)+']/div/div[2]/div[1]/div').text
    response1 = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[1]/div/div/div/div['+str(i+1)+']/div/div[2]/div[1]/div/div').text
    
    with open('input_sentence.txt', 'a') as f:
        f.write(inputs1)
        f.write('\n')

    with open('chatgpt_sentence.txt', 'a') as f:
        f.write(response1)
        f.write('\n')
    


