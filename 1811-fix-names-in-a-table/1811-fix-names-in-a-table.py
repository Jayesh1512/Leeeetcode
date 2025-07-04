import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def case(name:str) -> str:
        return name.capitalize()
    users['name'] = users['name'].apply(case)
    users = users.sort_values(by='user_id')
    return users