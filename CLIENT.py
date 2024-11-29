

import requests
import json

BASE_URL = 'http://127.0.0.1:5000/products'  # Base URL for the API

def add_product(name, description, price):
    """
    Adds a new product by sending a POST request to the /products endpoint.
    """
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    
    response = requests.post(BASE_URL, json=product_data)

    if response.status_code == 201:
        print("Product added successfully:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Failed to add product: {response.status_code} - {response.json().get('error', 'No error message')}")

def get_products():
    """
    Retrieves and prints the list of all products by sending a GET request to the /products endpoint.
    """
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        products = response.json()
        print("List of Products:")
        print(json.dumps(products, indent=4))
    else:
        print(f"Failed to retrieve products: {response.status_code} - {response.json().get('error', 'No error message')}")

if __name__ == '__main__':
    # Example usage
    add_product("Sample Product 1", "This is the first sample product.", 29.99)
    add_product("Sample Product 2", "This is the second sample product.", 39.99)
    
    # Retrieve and print all products
    get_products()