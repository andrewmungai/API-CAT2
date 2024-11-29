from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

@app.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product.
    Accepts a JSON object with 'name', 'description', and 'price'.
    Responds with 201 Created or 400 Bad Request.
    """
    data = request.get_json()

    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    name = data['name']
    description = data['description']
    price = data['price']

    if not isinstance(price, (float, int)) or price < 0:
        return jsonify({'error': 'Price must be a positive number'}), 400

    
    new_product = Product(name, description, price)
    products.append(new_product)

    return jsonify(new_product.to_dict()), 201

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve a list of all products.
    Responds with 200 OK and a JSON array of products.
    """
    return jsonify([product.to_dict() for product in products]), 200

if __name__ == '__main__':
    app.run(debug=True)