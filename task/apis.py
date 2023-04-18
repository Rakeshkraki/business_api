from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store the business data
businesses = {}


@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    return jsonify(businesses)


@app.route('/api/businesses', methods=['POST'])
def add_business():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    legal_name = data['legal_name']
    aadhaar_number = data['aadhaar_number']
    pan_number = data['pan_number']
    gstin_number = data['gstin_number']
    address = data['address']
    state_code = data['state_code']
    pin_code = data['pin_code']
    # create a new business object and add it to the dictionary
    business = {
        'first_name': first_name,
        'last_name': last_name,
        'legal_name': legal_name,
        'aadhaar_number': aadhaar_number,
        'pan_number': pan_number,
        'gstin_number': gstin_number,
        'address': address,
        'state_code': state_code,
        'pin_code': pin_code
    }
    businesses[aadhaar_number] = business
    return jsonify({'message': 'Business added successfully'})


data = {
    "first_name": "John",
    "last_name": "Doe",
    "legal_name": "John Doe Inc.",
    "adhar": "1234 5678 9012",
    "pan": "ABCDE1234F",
    "gstin": "12ABCDE1234F1Z5",
    "address": "123 Main St",
    "state_code": "CA",
    "state_name": "California",
    "pin_code": "12345"
}

# Define the API endpoints


@app.route('/api/first_name', methods=['GET'])
def get_first_name():
    return jsonify(data['first_name'])


@app.route('/api/last_name', methods=['GET'])
def get_last_name():
    return jsonify(data['last_name'])


@app.route('/api/legal_name', methods=['GET'])
def get_legal_name():
    return jsonify(data['legal_name'])


@app.route('/api/adhar', methods=['GET'])
def get_adhar():
    return jsonify(data['adhar'])


@app.route('/api/pan', methods=['GET'])
def get_pan():
    return jsonify(data['pan'])


@app.route('/api/gstin', methods=['GET'])
def get_gstin():
    return jsonify(data['gstin'])


@app.route('/api/address', methods=['GET'])
def get_address():
    return jsonify(data['address'])


@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify({"code": data['state_code'], "name": data['state_name']})


@app.route('/api/pin_code', methods=['GET'])
def get_pin_code():
    return jsonify(data['pin_code'])


if __name__ == '__main__':
    app.run(debug=True)
