from flask import Flask, jsonify, render_template, request

from entities.animal import Animal

app = Flask(__name__)


@app.route('/')
def index():
    try:
        animals = Animal.get_all_animals()
        return render_template('index.html', animals=animals)
    except Exception as e:
        print("Error al obtener los animales:", e)
        return render_template(
            'index.html',
            animals=[],
            error="No se pudieron cargar los animales. Revisa la conexión con la base de datos."
        ), 500

@app.route('/api/animals', methods=["POST"])
def create_animal():
    data = request.get_json()

    name = data.get("name")
    species = data.get("species")
    age = data.get("age")
    food = data.get("food")

    try:
        Animal.save(name, species, age, food)
    except Exception as e:
        print("Error al guardar el animal:", e)
        return jsonify({
            "success": False,
            "message": "No se pudo guardar el animal. Revisa la conexión con la base de datos."
        }), 500

    return jsonify({"success": True, "message": "El animal fue creado correctamente."}), 201


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
