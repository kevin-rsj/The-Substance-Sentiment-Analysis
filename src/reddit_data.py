import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="T8oxS6L1ITDEQYerxPqqfw",
    client_secret="z2TOqDgjAkF9MpGXA_Y5JwMxASw08w",
    user_agent="movie_analysis_script",
)

def fetch_reddit_comments(query, post_limit=500, comment_limit=500):
    comments_data = []
    total_comments_fetched = 0
    
    for submission in reddit.subreddit("all").search(query, sort='relevance', limit=post_limit):
        if "The Substance" in submission.title or "La Sustancia" in submission.title:
            print(f"Extrayendo comentarios del post: {submission.title}")

            submission.comments.replace_more(limit=0)
            comments_extracted = 0
            for comment in submission.comments.list():
                if comments_extracted >= comment_limit:
                    break
                comments_data.append({
                    "post_title": submission.title,
                    'created_utc': submission.created_utc,
                    "comment_body": comment.body,
                    "comment_score": comment.score
                })
                comments_extracted += 1
                total_comments_fetched += 1

            if total_comments_fetched >= 5000:
                break

    return comments_data

comments_data = fetch_reddit_comments("The Substance", post_limit=500, comment_limit=500)
comments_data += fetch_reddit_comments("La Sustancia", post_limit=500, comment_limit=500)

df_comments = pd.DataFrame(comments_data)

csv_file = "reddit_comments.csv"
df_comments.to_csv(csv_file, index=False, encoding='utf-8')
print(f"Datos guardados en {csv_file}")