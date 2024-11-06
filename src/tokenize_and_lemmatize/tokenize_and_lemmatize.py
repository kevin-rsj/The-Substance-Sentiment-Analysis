import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


df = pd.read_csv("data_with_sentiment.csv")

stop_words = set(stopwords.words('english')) 
lemmatizer = WordNetLemmatizer()
irrelevant_words = ['sustancia', 'substance', 'demi','moore', 'margaret', 'qualley', 'sue', 'dennis','quaid','harvey']

def tokenize_and_lemmatize(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in irrelevant_words]
    return ' '.join(tokens) if tokens else text

df['comment_tokenize_lemmatize'] = df['comment_body_cleaned']. apply(tokenize_and_lemmatize)
print("Se realizo la la Tokenización y Lematización")

csv_file = "data_for_topic_modeling.csv"
df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")