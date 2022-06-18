from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Cross Origin Resource Sharing

@app.route("/", methods=['GET'])
def index():
    # items = {
    #     {'item': "apple", 'price': 100},
    #     {'item': "orange", 'price': 120},
    #     {'item': "grape", 'price': 300},
    #     {'item': "melon", 'price': 400}
    # }
    items = {'item': "apple", 'price': 120}
    return make_response(items)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)