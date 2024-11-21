# Importar las bibliotecas necesarias
from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok

# Crear la aplicación Flask
app = Flask(__name__)

# Iniciar ngrok para exponer la API
run_with_ngrok(app)  # Esto abrirá un túnel público

# Ruta principal (GET)
@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a la API de Colab"})

# Ruta de datos (GET) - Ejemplo de datos simulados
@app.route('/datos', methods=['GET'])
def obtener_datos():
    datos = {
        "titulo": "API desde Google Colab",
        "numeros": [1, 2, 3, 4, 5],
        "estado": "Éxito"
    }
    return jsonify(datos)

# Ruta para recibir datos por POST
@app.route('/enviar', methods=['POST'])
def recibir_datos():
    # Obtiene los datos enviados en formato JSON
    datos = request.get_json()
    
    # Si no se envían datos, se responde con un error
    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400
    
    # Si se reciben los datos, los enviamos de vuelta en la respuesta
    return jsonify({"mensaje": "Datos recibidos correctamente", "datos": datos})

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run()
