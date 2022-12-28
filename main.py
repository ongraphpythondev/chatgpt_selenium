import time, os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


driver = uc.Chrome()
url = "https://chat.openai.com/chat"

driver.get(url)
driver.maximize_window()


text = "where is the movie theater?"  # Enetr the text here
email = "dilshad.ongraph@gmail.com" # Enter the Email here
password = "Dilshad0435" # Enter the password here

WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > div > div.flex.flex-row.gap-3 > button:nth-child(1)')))
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div.flex.flex-row.gap-3 > button:nth-child(1)').click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/section/div/div/div/div[3]/form[1]/button')))
driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/div[3]/form[1]/button').click()


WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'identifierId')))
driver.find_element(By.ID, 'identifierId').send_keys(email)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()


WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()


WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button').click()


WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]').click()


WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button[2]').click()
df = pd.DataFrame([],columns=['inputs','response'])


for i in range(1,60,2):

    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/form/div/div[2]/textarea').send_keys(text)
    driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[2]/form/div/div[2]/button').click()
    time.sleep(15)

    print(driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[1]/div/div/div/div['+str(i)+']/div/div[2]/div[1]/div').text)
    print("---------------------------------------------------------------------------------------------------------------------")
    print(driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[1]/div/div/div/div['+str(i+1)+']/div/div[2]/div[1]/div/div').text)
    
    inputs1=driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[1]/div/div/div/div['+str(i)+']/div/div[2]/div[1]/div').text
    response1 = driver.find_element(By.XPATH,'/html/body/div/div/div/main/div[1]/div/div/div/div['+str(i+1)+']/div/div[2]/div[1]/div/div').text

    df1 = pd.DataFrame([{'inputs':inputs1,'response':response1}])
    df = pd.concat([df,df1],ignore_index=True)
    print(df)


df.to_csv("final.csv")
time.sleep(30)
print("done")

