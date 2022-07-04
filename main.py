from flask import jsonify, request, Flask

app = Flask(__name__)

pizzas = [{'id': 2,
           "name": "Margarita",
           "price": 14.25},
          {'id': 3,
           "name": "Hawaiian",
           "price": 15.25
           }]


@app.route("/health", methods=["GET"])
def server_health():
    response = "Server is OK"
    return jsonify(response)


@app.route("/pizzas", methods=["GET"])
def list_pizzas():
    return jsonify(pizzas)


@app.route("/pizzas/<number>", methods=["GET"])
def show_pizza(number: int):
    for pizza in pizzas:
        if str(pizza['id']) == str(number):
            return jsonify(pizza), 200
    return {}, 404


@app.route("/pizzas", methods=["POST"])
def add_pizza():
    if not request.is_json:
        return jsonify("Request is not json"), 400
    pizza = request.get_json()
    pizza["id"] = next_id()
    pizzas.append(pizza)
    res = {'status': 'created'}
    return jsonify(res), 201


@app.route("/pizzas/<number>", methods=["DELETE"])
def delete_pizza(number: int):
    for pizza in pizzas:
        if str(pizza['id']) == str(number):
            pizzas.remove(pizza)
            return {}, 204
    return {}, 404


@app.route("/pizzas/<number>", methods=["PUT"])
def update_pizza(number: int):
    if request.is_json:
        updated_pizza = request.get_json()
        updated_pizza["id"] = int(number)
        for pizza in pizzas:
            if str(pizza['id']) == str(number):
                pizzas.remove(pizza)
                pizzas.append(updated_pizza)
                return {}, 204
        return {}, 404
    else:
        return jsonify("Request is not json"), 400


def next_id() -> int:
    if len(pizzas) == 0:
        return 1
    big = 1
    for pizza in pizzas:
        if pizza["id"] > big:
            big = pizza["id"]
    return big + 1

# TODO: please add comment what this app dose

if __name__ == '__main__':
    cos = next_id()
    print(cos)
    app.debug = True
    app.run()
