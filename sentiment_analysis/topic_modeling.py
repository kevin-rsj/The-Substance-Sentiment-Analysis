import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

df = pd.read_csv("data_for_topic_modeling.csv")


vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = vectorizer.fit_transform(df['comment_tokenize_lemmatize'])


tfidf_transformer = TfidfTransformer()
tfidf_matrix = tfidf_transformer.fit_transform(dtm)

tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
tfidf_df['created_date'] = df['created_date']
tfidf_df['comment_date'] = df['comment_date']
tfidf_df['sentiment_score'] = df['sentiment_score'].round(2)
print("Se creo el df con la vectorizacion de token")

tfidf_long_df = pd.melt(tfidf_df, id_vars=['created_date','comment_date','sentiment_score'], var_name='token', value_name='tfidf_value')

tfidf_long_df = tfidf_long_df[tfidf_long_df['tfidf_value'] > 0]
tfidf_long_df['tfidf_value'] = tfidf_long_df['tfidf_value'].round(2)

csv_file = "tfidf_for_dashboard.csv"
tfidf_long_df.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")

