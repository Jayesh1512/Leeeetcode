import pandas as pd

def calculate_bonus(row):
    if row['employee_id'] % 2 == 1 and row['name'][0] != 'M':
        return  row['salary']
    return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(calculate_bonus, axis=1)
    employees = employees.sort_values(by='employee_id')
    return employees[['employee_id','bonus']]
