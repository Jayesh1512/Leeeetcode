import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    res = views[views['author_id'] == views['viewer_id']][['author_id']]
    res = res.drop_duplicates()
    res = res.sort_values(by='author_id')
    res = res.rename(columns = {'author_id' : 'id'})
    return res
