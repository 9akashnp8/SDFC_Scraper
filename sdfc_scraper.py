from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import csv

url = "https://www.tecnoware.com/en-US/"

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url)

#Click on the "Accept" button from the banner
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button').click()

#List of IDS to search
#to_search = ['FGCEDP1202RTIEC','FGCEDP2402RTIEC','FGCEDP3602RTIEC','FBBEDP3602RT/00','FGCEVDP6503MM','FGCEVDP6MM2/00','FGCEVDP10MM2/00','FBBEVDP192A/00','FGCERAPL802UNI','FGCERAPL1202UNI','FGCERAPL2002IEC','FGCERAPL2602IEC','BCC950'
#]

datas = []
#Main loop of the program
#Click on the search button
driver.find_element(By.XPATH, '//*[@id="logoPart"]/div/div/div[2]/div/div[2]/div[1]').click()
#Set the text box as a variable
search = driver.find_element(By.XPATH, '//*[@id="Txt_ricerca"]')
#Enter the ID from the to_search list based on i
search.send_keys("FGCEDP1202RTIEC")
#wait 5 seconds
time.sleep(5)
#click on the search result
driver.find_element(By.XPATH, '//*[@id="searchResults"]/a').click()
#wait 5 seconds
time.sleep(5)
documents = driver.find_element(By.XPATH, '//*[@id="downloadTop"]')
doc1 = documents.find_element(By.XPATH, './/div[1]')
doc1_text = doc1.text
doc1_link = doc1.get_attribute("onclick")
doc2 = documents.find_element(By.XPATH, './/div[2]')
doc2_text = doc2.text
doc2_link = doc2.get_attribute("onclick")
doc3 = documents.find_element(By.XPATH, './/div[3]')
doc3_text = doc3.text
doc3_link = doc3.get_attribute("onclick")
datas.append([doc1_text, doc1_link, doc2_text, doc2_link, doc3_text, doc3_link])

with open('kishan.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    headers = ['ID','Document text','Document 1 Link', 'Certification']
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)
