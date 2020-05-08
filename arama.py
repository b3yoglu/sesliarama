#!/usr/bin/env python3
#createdbeyoglu
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import playsound
import os
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio2 = r.listen(source)
try:
    data2 = r.recognize_google(audio2, language='tr-tr')
    data2 = data2.lower()
    playsound.playsound("lenacikti.mp3")
    removed = data2.replace("lena", "")
    site = requests.get('https://yandex.com.tr/search/?text=' + removed)
    cikti = BeautifulSoup(site.content, 'html.parser')
    cikti2 = cikti.find("div", {"class": "serp-title serp-title_type_supertitle serp-title_font-weight_bold typo typo_text_xl typo_line_m entity-search__title"})
    cikti3 = cikti.find("div", {"class": "serp-title serp-title_type_subtitle serp-title_black_yes typo typo_type_greenurl entity-search__subtitle"})
    cikti4 = cikti.find("span", {"class": "cut2__visible"})
    cikti5 = cikti.find("span", {"class": "cut2__invisible"})
    cikti6 = cikti.find("b", {"class": "key-value__item-title"})
    cikti7 = cikti.find("span", {"class": "text-cut2 typo typo_text_m typo_line_m"})
    birincicikti = "İsmi:" + cikti2.text
    print(birincicikti)
    tts1 = gTTS(text=birincicikti, lang='tr')
    tts1.save("birincicikti.mp3")
    playsound.playsound("birincicikti.mp3")
    ikincicikti = "Açıklaması da:" + cikti3.text
    print(ikincicikti)
    tts2 = gTTS(text=ikincicikti, lang='tr')
    tts2.save("ikincicikti.mp3")
    playsound.playsound("ikincicikti.mp3")
    ucuncucikti = "Vikipedide şöyle:" + cikti4.text + "\n" + cikti5.text
    print(ucuncucikti)
    tts3 = gTTS(text=ucuncucikti, lang='tr')
    tts3.save("ucuncucikti.mp3")
    playsound.playsound("ucuncucikti.mp3")
    if cikti6.text == "Abone: ":
        ciktieger1 = "Doğum, Kuruluş Tarihi yada Diğer Bilgilerinide vereyim:" + cikti7.text
        print(ciktieger1)
        tts4 = gTTS(text=ciktieger1, lang='tr')
        tts4.save("ciktieger1.mp3")
        playsound.playsound("ciktieger1.mp3")
    if cikti6.text == "Şehir: ":
        ciktieger1 = "Doğum, Kuruluş Tarihi yada Diğer Bilgilerinide vereyim:" + cikti7.text
        print(ciktieger1)
        tts4 = gTTS(text=ciktieger1, lang='tr')
        tts4.save("ciktieger1.mp3")
        playsound.playsound("ciktieger1.mp3")
    else:
        ciktieger2 = cikti6.text + cikti7.text
        print(cikti6.text + cikti7.text)
        tts5 = gTTS(text=ciktieger2, lang='tr')
        tts5.save("ciktieger2.mp3")
        playsound.playsound("ciktieger2.mp3")
except:
    print("Başka sonuç bulunamadı.")
    tts6 = gTTS(text="Başka sonuç bulamadım.", lang='tr')
    tts6.save("yok.mp3")
    playsound.playsound("yok.mp3")
    os.system("rm birincicikti.mp3")
    os.system("rm ikincicikti.mp3")
    os.system("rm ucuncucikti.mp3")
    os.system("rm yok.mp3")
else:
    tts7 = gTTS(text="Başka sonuç bulamadım.", lang='tr')
    tts7.save("bitti.mp3")
    playsound.playsound("bitti.mp3")
    os.system("rm birincicikti.mp3")
    os.system("rm ikincicikti.mp3")
    os.system("rm ucuncucikti.mp3")
    os.system("rm yok.mp3")