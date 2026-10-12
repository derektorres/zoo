from flask import Flask, jsonify, render_template, request

from entities.animal import Animal

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/animals', methods=["POST"])
def create_animal():
    data = request.get_json()

    name = data.get("name")
    species = data.get("species")
    age = data.get("age")
    food = data.get("food")

    Animal.save(name, species, age, food)

    return jsonify({"success": True, "message": "El animal fue creado correctamente."}), 201


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
