from gtts import gTTS
from googletrans import Translator
import os

translator = Translator()

def language_selection():
    global language
    print ("Welcome to the Text to Speech Converter!")
    print ("Select language")

    languages = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('ja', 'Japanese'),
        ('ko', 'Korean'),
        ('zh', 'Chinese')
    ]

    print ("Available languages:",languages)
    

    for len in languages:
        print (len[1])
    lang_input = input("Enter the language code (e.g., 'en' for English): ").strip().lower()
    if lang_input in dict(languages):
        language = lang_input
        print(f"Selected language: {dict(languages)[language]}")
    else:
        print("Invalid language selection. Defaulting to English.")
        language = 'en'



def translation():
    print("Enter the text you want to convert to speech: ")
    text = input()
    f = open("text.txt", "w")
    f.write(text)
    f.close()
    
    import asyncio

    f = open("text.txt", "r")
    
    input_text = f.read().replace("\n",'')

    async def get_translated_text(text, dest_lang):
        result = await translator.translate(text, dest=dest_lang)
        return result.text

    translated_text = asyncio.run(get_translated_text(input_text, language))

    voice = gTTS(text=translated_text, lang=language, slow=False)

    voice.save("text.mp3")  

    os.system("start text.mp3")
    
    
    
    return input_text

if os.name == ('nt'):
    os.system('cls')

else:
    os.system('clear')

language_selection()
translation()