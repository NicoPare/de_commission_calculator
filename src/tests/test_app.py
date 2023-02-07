import pytest
from src.app import get_deals_data, get_products, calculate_commission

# test product data not null
@pytest.mark.parametrize(
    "input_x, input_y, input_z",
    [
        ('Ian', '2023-01-01', '2023-04-30'),
        ('David', '2023-04-01', '2023-06-30'),
        ('Poppy', '2023-03-01', '2023-05-30')
    ]
)
def test_get_products_not_none(input_x, input_y, input_z):
    products = get_products(input_x, input_y, input_z)
    assert products != None

# test deals data not null
@pytest.mark.parametrize(
    "input_x, input_y, input_z",
    [
        ('Ian', '2023-01-01', '2023-04-30'),
        ('David', '2023-04-01', '2023-06-30'),
        ('Poppy', '2023-03-01', '2023-05-30')
    ]
)
def test_get_deals_data_not_none(input_x, input_y, input_z):
    deals = get_deals_data(input_x, input_y, input_z)
    assert deals != None

# test commission calculation
@pytest.mark.parametrize(
    "input_x, input_y, input_z, expected",
    [
        ('Ian', '2023-01-01', '2023-04-30', 55350),
        ('David', '2023-04-01', '2023-06-30', 89540),
        ('Poppy', '2023-03-01', '2023-05-30', 118190)

    ]
)
def test_get_commission_param(input_x, input_y, input_z, expected):
    assert calculate_commission(input_x, input_y, input_z) == expected    