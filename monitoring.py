import re
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
import requests
import spacy
from keras.preprocessing.text import Tokenizer
import keras

url_now =''
url_old=''
workFlag = True
TAG_RE = re.compile(r'<[^>]+>')
sp=spacy.load("ru_core_news_sm")
#импорт моделей векторизатора и классификатора
model = keras.models.load_model('text_classifier_ru_1.h5')
tokenizer = keras.models.load_model('text_vectorizer_ru_1.h5')

def remove_tags(text): 
    return TAG_RE.sub('', text)

def preWorkText(text):
    #Убираем все \n
    document = remove_tags(text)
    text = text.lower()
    #лематизация
    document=sp(text)
    document=[token.lemma_ for token in document]
    document = ' '.join(document)
    #убираем специальные знаки
    document = re.sub(r'\W', ' ', document)
    #убираем лишние пробелы
    document = re.sub(r'\s+', ' ', document)
    text=document
    return text

def urlControll():
    #выделение адресной строки
    try:
        pyautogui.hotkey('ctrl', 'l')
    except:
        pass
    pyautogui.hotkey('ctrl', 'c')
    #копирование url в переменную
    try:
        url_now = pyperclip.paste()
    except:
        pass
    if url_now != url_old and url_now != '':
        response = requests.get(url_now)
        if not response:
            soup = BeautifulSoup(response.text, 'html')
            x = preWorkText(soup)
            sequences = tokenizer.texts_to_sequences(x)
            y = model.predict(sequences)

            if y == 1:
                pyautogui.hotkey('ctrl', 'w')
                pyperclip.copy(r'C:\Users\Feirbrais\Desktop\Diplom\Pages\Blocked.html')
                pyautogui.hotkey('ctrl', 'l')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
            
def startMonitoring():
    workFlag == True
    while workFlag == True:        
        urlControll()

def stopMonitoring():
    if workFlag == True:
        workFlag = False