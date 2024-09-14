import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Inicializar la app Flask
app = Flask(__name__, static_url_path='/static')

# incializar flask
app= Flask(__name__)

# Definir una ruta para la pagina principal
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para manejar la interacción con el chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("prompt")

    # Llamar a la API de GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres Albert Einstein, el famoso físico teórico. Habla como lo haría él, con un profundo conocimiento de la física, pero también con su sentido del humor."},
            {"role": "user", "content": user_input}
        ]
    )

    # Obtener la respuesta del chatbot
    chatbot_response = response['choices'][0]['message']['content']
    
    return jsonify({"response": chatbot_response})

# Ejecutar la app Flask
if __name__ == "__main__":
    app.run(debug=True)

# este bloque de codigo debe ser descomentareado para que trabaje el chat desde la terminal

# def chat_with_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "Eres Albert Einstein, el famoso físico teórico. Habla como lo haría él, con una profunda comprensión científica y un interés por la física, pero también con su sentido del humor característico y humildad."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response['choices'][0]['message']['content']

# Bucle del chatbot esto para trabajarlo por la terminal si se desea probar este codigo solo debe descomentariar esta parte
# y ejecutar el archivo

# while True:
#     user_input = input("Tú: ")
#     if user_input.lower() in ["salir", "exit", "quit"]:
#         break
#     response = chat_with_gpt(user_input)
#     print("Albert Einstein Chatbot:", response)
