from bs4 import BeautifulSoup, SoupStrainer
from gtts import gTTS
import requests
import os
try:
    
    article_links = input("Enter url of medium blog\n")
    path='/home/amit/Documents'
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
 
    r = requests.get(article_links, headers=headers, timeout=5)
        
    page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('main'))
    article_text = []
    file_name = ""
    for title in page.find_all('h1', {'class': 'graf'}):
        article_title = 'Title: ' + str(title.text)
        file_name = title.text
        article_text.append(article_title)   
    for paragraphs in page.find_all('p', {'class': 'graf'}):
        article_text.append(paragraphs.text)
    text_for_speech = '\n\n'.join(article_text)
    tts = gTTS(text=text_for_speech, lang='en')
    filename=file_name + " .mp3"
    fullpath=os.path.join(path,filename)
    tts.save(fullpath)
    #tts.save(file_name + ".mp3")
except requests.RequestException as e :
    print(str(e))
    print("error")

