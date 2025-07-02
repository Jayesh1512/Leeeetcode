import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    purchasers = orders['customerId']
    res = customers[~(customers['id'].isin(purchasers))][['name']]
    res['Customers'] = res['name']
    res = res.drop(columns = 'name')
    return res