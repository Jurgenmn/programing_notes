from flask import Flask, request, jsonify

app = Flask(__name__)

cars = [
    {"id": 1, "brand": "audi", "model": "A4"},
    {"id": 2, "brand": "mercedes", "model": "S-class"},
    {"id": 3, "brand": "mercedes", "model": "E-class"},
    {"id": 4, "brand": "mercedes", "model": "A-class"},
    {"id": 5, "brand": "bmw", "model": "x-5"},
    {"id": 6, "brand": "bmw", "model": "x-7"}
]


@app.route("/cars")
def retrive_all_cars():
    return jsonify(cars)


@app.route("/cars/<int:id>")
def retrive_car(id):
    for car in cars:
        if car["id"] == id:
            return jsonify(car)

    return jsonify({})


@app.route("/cars/create", methods=["POST"])
def create_car():
    id = len(cars) + 1
    car = {"id": id}
    car["brand"] = request.json["brand"]
    car["model"] = request.json["model"]
    cars.append(car)
    return jsonify(car)


app.run("localhost", 3000, debug=True)
