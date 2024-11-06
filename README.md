# The Substance Sentiment Analysis

Este proyecto analiza los sentimientos y temas presentes en los comentarios de usuarios sobre la película The Substance (2024) en Reddit. Utilizamos técnicas de análisis de texto y visualización de datos para obtener información valiosa sobre la recepción de la película.
    
### Descripción del Flujo de Trabajo

1-  Extracción de Datos:

Se extraen comentarios con la API de Reddit, los datos estan en relación a la película utilizando palabras clave del titulo "The Substance" y "La Sustancia" para asegurar una cobertura completa.
Los datos se almacenan en la carpeta data/[raw](https://github.com/kevin-rsj/The-Substance-Sentiment-Analysis/tree/main/data/raw).

2-  Limpieza y Traducción:

Se preprocesan los comentarios eliminando ruido textual y caracteres especiales, se traducen los comentarios en español al inglés para estandarizar el análisis.
Este paso garantiza que los datos estén en un formato adecuado para el análisis de sentimientos sin alterar el contexto emocional de los comentarios.Lo resultados se guardan en archivo csv [data_cleaned](https://github.com/kevin-rsj/The-Substance-Sentiment-Analysis/blob/main/data/processed/data_cleaned.csv)

3-  Análisis de Sentimiento con VADER:

Después de la limpieza y traducción, se aplica el análisis de sentimiento utilizando el modelo VADER antes de realizar la tokenización y lematización.

Al realizar el análisis de sentimiento antes de la tokenización, conservamos el contexto completo de las frases, lo cual permite a VADER captar matices emocionales como negaciones y expresiones idiomáticas. Esto mejora la precisión del análisis, ya que el contexto y las combinaciones de palabras se mantienen intactos.

Los resultados de este análisis se guardan en data/processed [data_with_sentiment](https://github.com/kevin-rsj/The-Substance-Sentiment-Analysis/blob/main/data/processed/data_with_sentiment.csv).

4-  Tokenización y Lematización:

Luego del análisis de sentimientos, los comentarios se tokenizan y lematizan para dividir el texto en palabras individuales y raíces, lo que permite un análisis más detallado de temas y palabras clave.
Este paso ayuda a identificar términos recurrentes y temas de conversación en torno a la película sin comprometer el análisis de sentimientos.

Análisis de Temas:

En este paso, utilizamos TF-IDF (Term Frequency-Inverse Document Frequency) para identificar palabras clave y temas en los comentarios. Primero, aplicamos CountVectorizer para generar una matriz de términos, excluyendo palabras comunes y términos que aparecen en pocos o demasiados documentos. Luego, transformamos esta matriz con TfidfTransformer para ponderar la relevancia de cada palabra en función de su frecuencia y rareza.

El resultado es un DataFrame con valores TF-IDF para cada palabra relevante en los comentarios, junto con información adicional (fecha de creación, fecha del comentario y puntuación de sentimiento). Finalmente, convertimos estos datos a un formato largo y los exportamos como [tfidf_for_dashboard](https://github.com/kevin-rsj/The-Substance-Sentiment-Analysis/blob/main/data/processed/tfidf_for_dashboard.csv), para su integración en el dashboard y visualización de temas clave en las opiniones.

### Visualización:

Los datos procesados se exportan y visualizan en un dashboard de Tableau, que incluye una nube de palabras, distribución de sentimientos, y una serie temporal de puntuaciones de sentimiento para observar las tendencias en la percepción de la película a lo largo del tiempo. link [tableau](https://public.tableau.com/views/Libro1_17309152783770/THESUBSTANCE?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


### Requerimientos
-  Python 3.8+
  Bibliotecas: pandas, nltk, vaderSentiment
  API de Reddit para la extracción de datos (praw)
-  tableau

### Resultados y Conclusiones

-  El dashboard final incluye:

Nube de palabras: Visualización de las palabras más mencionadas en los comentarios, mostrando las emociones y temas recurrentes.
Distribución de sentimientos: Muestra la proporción de comentarios positivos, negativos y neutros.
Puntuación de sentimiento por fecha: Serie temporal que refleja cómo ha evolucionado la percepción de la audiencia sobre la película desde su estreno.

-  Conclusion:

El análisis de sentimiento de los comentarios sobre la película The Substance arroja un promedio de sentiment score de 0.19, indicando una tendencia ligeramente positiva en las opiniones generales. Entre las palabras clave más relevantes y frecuentemente mencionadas destacan "horror", "like", "think", "really", y "good", lo que sugiere que los espectadores discutieron ampliamente aspectos relacionados con el género de terror y sus impresiones personales. La distribución de sentimiento muestra una variabilidad notable, pero se observa una inclinación hacia opiniones positivas, especialmente en fechas recientes. Esto podría implicar una recepción favorable entre la audiencia, con ciertos picos de entusiasmo en momentos específicos.







