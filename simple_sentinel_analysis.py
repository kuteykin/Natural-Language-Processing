"""Sentinel analysis of News article"""
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
req2 = requests.get(input('Enter link to the article: '))
soup2 = BeautifulSoup(req2.text, "lxml")
text2 = soup2.get_text(strip=False)
blob2 = TextBlob(text2)
print(f'General Score: {blob2.sentiment}\n\n')
for sentence in blob2.sentences:
    print(f'{sentence}  [{sentence.sentiment}]') 