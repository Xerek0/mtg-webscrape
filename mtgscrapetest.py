import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#empty lists
name = []
cmc = []
manacost = []
typeline = []
rulestxt = []

#main loop
    #manually changing number of pages, ik there is a better way
page = -1
while page <= 3:   
    page = page + 1
    url = 'https://gatherer.wizards.com/Pages/Search/Default.aspx?page={}&format=[%22Commander%22]'.format(page)
    results = requests.get(url)
    soup = BeautifulSoup(results.text, "html.parser")
    
    mtgAll = soup.find_all('table')
    

    for tables in mtgAll:
    
        #name
        cardtitle = tables.find('span', class_='cardTitle').text
        name.append(cardtitle)
    
        #converted mana cost
        mcost = tables.find('span', class_='convertedManaCost').text
        cmc.append(mcost)
    
        #typeline
        cardtype = tables.find('span', class_='typeLine').text
        typeline.append(cardtype)
    
        #rulestext
        rules = tables.find('div', class_='rulesText').text
        rulestxt.append(rules)
        
#make data frame
#I need to add more data frames

cards = pd.DataFrame({
'CardName': name,
'CMC': cmc,
'Rules': rulestxt,
'Types': typeline,
})

#cleaningdata
cards['CMC'] = cards['CMC'].astype(int)
cards['CardName'] = cards['CardName'].str.replace('\n', '')

cards.to_csv('cardlistTest.csv')
