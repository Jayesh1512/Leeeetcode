import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]
    res = self_views[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})
    res = res.sort_values(by='id')
    return res
