from flask import Flask, jsonify

app = Flask(__name__)

pizzas = [{"id": 2,
           "name": 'margeritha',
           "price": 14.25},
          {"id": 3,
           "name": 'hawaian',
           "price": 15.25
           }]


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world"


@app.route("/health", methods=["GET"])
def server_health():
    response = "Server is OK"
    return jsonify(response)


@app.route("/order", methods=["GET"])
def to_order():
    return jsonify(pizzas)


if __name__ == '__main__':
    app.debug = True
    app.run()
