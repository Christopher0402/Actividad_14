from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Función para registrar movimientos (Punto 4, 7 y 10)
def registrar_log(mensaje):
    with open("backup.log", "a") as f:
        f.write(mensaje + "\n")

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        val1 = request.form.get("val1")
        val2 = request.form.get("val2")
        operacion = request.form.get("op")
        tipo = request.form.get("tipo")

        try:
            # --- PARTE 1: ARITMÉTICA ---
            if tipo == "aritmetica":
                n1, n2 = float(val1), float(val2)
                if operacion == "+": resultado = n1 + n2
                elif operacion == "-": resultado = n1 - n2
                elif operacion == "*": resultado = n1 * n2
                elif operacion == "/": resultado = n1 / n2 if n2 != 0 else "Error: Div/0"
                registrar_log(f"Aritmética: {val1} {operacion} {val2} = {resultado}")

            # --- PARTE 2: BINARIA ---
            elif tipo == "binaria":
                n1_bin = int(val1, 2)
                n2_bin = int(val2, 2)
                if operacion == "+": res_num = n1_bin + n2_bin
                elif operacion == "-": res_num = n1_bin - n2_bin
                elif operacion == "*": res_num = n1_bin * n2_bin
                elif operacion == "/": res_num = n1_bin // n2_bin if n2_bin != 0 else 0
                resultado = bin(res_num).replace("0b", "")
                registrar_log(f"Binaria: {val1} {operacion} {val2} = {resultado}")

            # --- PARTE 3: LÓGICA (Punto 8) ---
            elif tipo == "logica":
                b1 = val1.lower() in ['true', '1', 't']
                b2 = val2.lower() in ['true', '1', 't']
                if operacion == "AND": resultado = b1 and b2
                elif operacion == "OR": resultado = b1 or b2
                registrar_log(f"Lógica: {b1} {operacion} {b2} = {resultado}")

        except Exception as e:
            resultado = "Error de entrada"
            registrar_log(f"Error: {str(e)}")
            
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, port=5000)