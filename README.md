# Spiff Data engineering challenge: creating a commission Calculator

In order to create a code for this commission calculator requested, I've created a python project to accomplish it.

## Project

The main code of the calculator is located in src/app. Here you have 3 functions:

1. get_deals_data: to access deals table, based on some parametres to get the data from a sales representant on a specific period of time; also, this functions returns the products sold.

2. get_products: bases on previous parametres and the product identifiers returned in "get_deals_data", this functions collects products data from its table.

3. calculate_commission: this functions creates the dataframe merging products and deals data in order to calculate the commission bases on the bussiness rules requested.

Besides the app.py file, there is a test folder that helps with some tests on each function created. With the help of some paremetres, the code can test if get_deals_data, and get_products functions give results. From the other side, there is a test for the commission calculator in order to see if the calculation works properly.

### Notes

The requirements.txt file should list all Python libraries that the code depends on, and they will be installed using:

pip install -r requirements.txt


### run app

In case you want to see how the app works from app.py file, you should uncomment this:

#print(calculate_commission('Ian', '2023-01-01', '2023-04-30'))
#print(calculate_commission('David', '2023-04-01', '2023-06-30'))
#print(calculate_commission('Poppy', '2023-03-01', '2023-05-30'))

And run the python code.

If you want to run the tests, you should open the terminal and run "python -m pytest -v".