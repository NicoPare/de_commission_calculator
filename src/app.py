import json
import pandas as pd
from datetime import datetime


# function to get a list from deals table and all product_id
def get_deals_data (sales_rep_name, start_date, end_date):
    with open('data/deals.json') as urls:
        file_contents = json.load(urls)

    id = sales_rep_name
    s_date = datetime.strptime(str(start_date),'%Y-%m-%d')
    e_date = datetime.strptime(str(end_date),'%Y-%m-%d')

    # list with all deals from sales_rep_name
    deal_list = [d for d in file_contents if d['sales_rep_name'] in sales_rep_name]
    
    # filter for period of time requested
    f_list = [ ele for ele in deal_list if s_date <= datetime.strptime(ele['date'],'%Y-%m-%d') <= e_date ]
    
    product = set(d['product_id'] for d in f_list)

    return f_list, product 

# function to get data from the products in matters
def get_products(sales_rep_name, start_date, end_date):
    with open('data/products.json') as path:
        product_contents = json.load(path)
        
    products = get_deals_data(sales_rep_name, start_date, end_date)[1]
    product_l = list(products)

    # filter product
    expected_p = [d for d in product_contents if d['id'] in product_l]
    return expected_p

# function that calculates the commission
def calculate_commission(sales_rep_name, start_date, end_date):
    
    lst1 = get_deals_data(sales_rep_name, start_date, end_date)[0]
    lst2 = get_products(sales_rep_name, start_date, end_date)

    # create and merge dataframes
    lst1_df = pd.DataFrame(lst1)
    lst2_df = pd.DataFrame(lst2)
    lst2_df = lst2_df.rename(columns={'id': 'product_id'})

    df = lst1_df.merge(lst2_df, on='product_id')
    
    # calculate commission
    df['total_comission'] = df['quantity_products_sold'] * df['product_amount'] * df['commission_rate']
    total_commission = round(df['total_comission'].sum(), 2)

    return total_commission

#print(calculate_commission('Ian', '2023-01-01', '2023-04-30'))
#print(calculate_commission('David', '2023-04-01', '2023-06-30'))
#print(calculate_commission('Poppy', '2023-03-01', '2023-05-30'))