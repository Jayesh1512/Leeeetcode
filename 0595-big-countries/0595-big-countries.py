import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res = world[(world['area']>=3000000) | (world['population'] >= 25000000)][['name','population','area']]
    return res