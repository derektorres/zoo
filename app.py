<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
print("hello world")
print("prueba de docker")


print("hola desde acá :D")
>>>>>>> 81d42b165e597229b87c91732c16b657f9884b90
