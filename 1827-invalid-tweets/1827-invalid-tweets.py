import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    res = tweets[tweets['content'].str.len() > 15][['tweet_id']]
    return res