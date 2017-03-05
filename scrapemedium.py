from bs4 import BeautifulSoup, SoupStrainer
from gtts import gTTS
import requests
import os
import sys
try:
    flag="idlelib" in sys.modules
   # print(flag)
    if(flag):
        article_links = input("Enter url of medium blog\n")
    else:
        article_links = sys.argv
        for link in range(1,len(article_links)):
            url=article_links[link]
        article_links=url    
    path='/home/amit/Documents'
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
 
    r = requests.get(article_links, headers=headers, timeout=5)
        
    page = BeautifulSoup(r.content, "lxml", parse_only=SoupStrainer('main'))
    article_text = []
    file_name = ""
    for title in page.find_all('h1', {'class': 'graf'}):
        if(sys.version_info >= (3, 0)):
           article_title = 'Title: ' + str((title.text))
        else:
           article_title = 'Title: ' + str((title.text).encode('utf-8'))
           
        #article_title = 'Title: ' + str(title.text)
       # article_title = 'Title: ' + str((title.text).encode('utf-8'))
        #article_title = u' '.join(('Title: ',title.txt)).encode('utf-8').strip()
        file_name = title.text
        article_text.append(article_title)   
    for paragraphs in page.find_all(['p','h3','blockquote'], {'class': 'graf'}):
           if(sys.version_info >= (3, 0)):
              article_text.append(str((paragraphs.text)))
           else:
              article_text.append(str((paragraphs.text).encode('utf-8')))
              
    text_for_speech = '\n\n'.join(article_text)
    tts = gTTS(text=text_for_speech, lang='en')
    filename=file_name + " .mp3"
    fullpath=os.path.join(path,filename)
    tts.save(fullpath)
    #tts.save(file_name + ".mp3")
except requests.RequestException as e :
    print(str(e))
    print("error")

