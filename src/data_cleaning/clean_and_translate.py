import pandas as pd
from datetime import datetime
from googletrans import Translator
from langdetect import detect
import re


df = pd.read_csv("reddit_comments.csv")
df['created_date'] = df['created_utc'].apply(lambda x : datetime.utcfromtimestamp(x))
df['comment_date'] = df['comment_date'].apply(lambda x : datetime.utcfromtimestamp(x))

df = df[df['created_date'] >= '2024-01-01']
print("Se elimino post creados antes del año 2024")

df = df[~df['comment_body'].str.contains("deleted", case=False, na=False)]
print("Se elimino comentatios que cuyo contenido fue suprimido")

translator = Translator()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'@\w+', '', text) 
    text = re.sub(r'http\S+|www.\S+', '', text) 
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s,]', '', text)  
    text = re.sub(r'(.)\1{2,}', r'\1', text)  
    return text

df['comment_body_cleaned'] = df['comment_body'].apply(clean_text)

df = df.drop_duplicates(subset='comment_body_cleaned')
df = df.dropna(subset=['comment_body_cleaned'])
print("Se realizó la limpieza inicial de los datos")


def translate_to_english(text):
    try:
        if detect(text) == 'es':  
            return translator.translate(text, src='es', dest='en').text
        else:
            return text
    except Exception as e:
        print(f"Error en la traducción: {e}")
        return text

df['comment_body_cleaned'] = df['comment_body_cleaned'].apply(translate_to_english)

df = df[df['comment_body_cleaned'].str.len() > 0]

print("Se realizo la traduccion de los comentarios en español al inglés") 

csv_file = "data_cleaned.csv"
df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")