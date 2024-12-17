import pandas as pd

def load_and_merge_data():
    sales = pd.read_csv('data/sales_data.csv')
    products = pd.read_csv('data/product_info.csv')
    context = pd.read_csv('data/contextual_data.csv')
    data = sales.merge(products, on='item_id').merge(context, on='date')
    return data

def preprocess_data(data):
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values(by='date')
    data = data.fillna(0)
    return data
