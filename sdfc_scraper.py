import os
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import csv

url = "https://www.tecnoware.com/en-US/"

#Open chrome and go to 'url'
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url)

#Click on the "Accept" button from the banner
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="iubenda-cs-banner"]/div/div/div/div[3]/div[2]/button').click()

#List of IDS to search
to_search = ['FGCEDP1202RTIEC','FGCEDP2402RTIEC','FGCEDP3602RTIEC','FBBEDP3602RT/00','FGCEVDP6503MM','FGCEVDP6MM2/00','FGCEVDP10MM2/00','FBBEVDP192A/00','FGCERAPL802UNI','FGCERAPL1202UNI','FGCERAPL2002IEC','FGCERAPL2602IEC']

datas = []
tracker = 0
#Main loop of the program
for i in range(len(to_search)):
    time.sleep(5)
    #Click on the search button
    driver.find_element(By.XPATH, '//*[@id="logoPart"]/div/div/div[2]/div/div[2]/div[1]').click()
    #Set the text box as a variable
    search = driver.find_element(By.XPATH, '//*[@id="Txt_ricerca"]')
    #Enter the ID from the to_search list based on i
    search.send_keys(to_search[i])
    #wait 5 seconds
    time.sleep(5)
    #click on the search result
    driver.find_element(By.XPATH, '//*[@id="searchResults"]/a').click()
    #once search result has click on, replace any "/" in the name to "-"
    product_id = to_search[i].replace("/", "-")
    #wait 5 seconds
    time.sleep(5)
    #Find the downloads (Documents)
    documents = driver.find_element(By.XPATH, '//*[@id="downloadTop"]')
    #Create the folders and subfolders for the search ID
    main_folder = fr'E:\Private\Programming\VSCode\SDFC\{product_id}'
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    photos_sub_folder = fr'E:\Private\Programming\VSCode\SDFC\{product_id}\PHOTOS'
    if not os.path.exists(photos_sub_folder):
        os.makedirs(photos_sub_folder)
    doc_sub_folder = fr'E:\Private\Programming\VSCode\SDFC\{product_id}\TECHNICAL DOCUMENTS'
    if not os.path.exists(doc_sub_folder):
        os.makedirs(doc_sub_folder)
    #Download the first docoument to the Technical Documents folder with the right naming
    try:
        doc1 = documents.find_element(By.XPATH, './/div[1]')
        doc1_name = doc1.text
        doc1_link_pre = doc1.get_attribute("onclick")[14:-2]
        doc1_link = f"https://www.tecnoware.com{doc1_link_pre}"
        doc1_link_final = doc1_link.replace(" ","%20")
        urlretrieve(doc1_link_final, f"{doc_sub_folder}\{product_id} - {doc1_name}.pdf")
    except NoSuchElementException:
        pass
    try:
        doc2 = documents.find_element(By.XPATH, './/div[2]')
        doc2_name = doc2.text
        doc2_link_pre = doc2.get_attribute("onclick")[14:-2]
        doc2_link = f"https://www.tecnoware.com{doc2_link_pre}"
        doc2_link_final = doc2_link.replace(" ", "%20")
        urlretrieve(doc2_link_final, f"{doc_sub_folder}\{product_id} - {doc2_name}.pdf")
    except NoSuchElementException:
        pass
    try:
        doc3 = documents.find_element(By.XPATH, './/div[3]')
        doc3_name = doc3.text
        doc3_link_pre = doc3.get_attribute("onclick")[14:-2]
        doc3_link = f"https://www.tecnoware.com{doc3_link_pre}"
        doc3_link_final = doc3_link.replace(" ", "%20")
        urlretrieve(doc3_link_final, f"{doc_sub_folder}\{product_id} - {doc3_name}.pdf")
    except NoSuchElementException:
        pass
    tracker += 1
    print(tracker)
