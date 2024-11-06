import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv("data_cleaned.csv")

analyzer = SentimentIntensityAnalyzer()

df['sentiment_score'] = df['comment_body_cleaned'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
print("Se aplico el sentiment score")

csv_file = "data_with_sentiment.csv"
df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")