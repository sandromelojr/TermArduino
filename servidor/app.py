from flask import Flask, render_template, jsonify
from serial_reader import iniciar_serial, ler_temperatura
import threading, time

app = Flask(__name__)
arduino = iniciar_serial("COM6")  # abre a COM uma vez

temp_atual = 0.0

def atualizar_temp():
    global temp_atual
    while True:
        try:
            temp = ler_temperatura(arduino)
            if temp is not None:
                temp_atual = temp
        except Exception as e:
            print("Erro na thread de leitura:", e)
        time.sleep(1)

# Thread para atualizar temperatura em segundo plano
thread = threading.Thread(target=atualizar_temp, daemon=True)
thread.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/temperatura")
def temperatura():
    return jsonify({"temp": temp_atual})

if __name__ == "__main__":
    app.run(debug=False)
