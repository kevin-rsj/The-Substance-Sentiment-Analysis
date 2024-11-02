import pandas as pd
from datetime import datetime
from googletrans import Translator
from langdetect import detect
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

df = pd.read_csv(r"C:\Users\Kevin\code\kevin-rsj\The-Substance-Sentiment-Analysis\data\raw\reddit_comments.csv")
df['created_date'] = df['created_utc'].apply(lambda x : datetime.utcfromtimestamp(x))

df = df[df['created_date'] >= '2024-01-01']
print("Se elimino post creados antes del año 2024")

df = df[~df['comment_body'].str.contains("deleted", case=False, na=False)]
print("Se elimino comentatios que cuyo contenido fue suprimido")

translator = Translator()
stop_words = set(stopwords.words('english')) 
lemmatizer = WordNetLemmatizer()

irrelevant_words = ['sustancia', 'substance', 'demi','moore', 'margaret', 'qualley', 'sue', 'dennis','quaid','harvey']

def clean_text(text):
    text = text.lower()
    text = re.sub(r'@\w+', '', text) 
    text = re.sub(r'http\S+|www.\S+', '', text) 
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)  
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

print("Se realizo la traduccion de los comentarios en español al inglés")

def tokenize_and_lemmatize(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in irrelevant_words]
    return ' '.join(tokens)

df['comment_body_cleaned'] = df['comment_body_cleaned']. apply(tokenize_and_lemmatize)
df = df[df['comment_body_cleaned'].str.len() > 3]  
print("Se realizo la la Tokenización y Lematización")

csv_file = "data_cleaned.csv"
df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")