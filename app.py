from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Función para registrar cambios en el log (Punto 4 del ejercicio)
def registrar_log(accion):
    with open("backup.log", "a") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] - {accion}\n")

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        val1 = request.form.get("val1")
        val2 = request.form.get("val2")
        operacion = request.form.get("op")
        tipo = request.form.get("tipo")

        try:
            if tipo == "aritmetica":
                # Evalúa operaciones como 5 + 5
                resultado = eval(f"{val1} {operacion} {val2}")
                registrar_log(f"Cálculo Aritmético: {val1} {operacion} {val2} = {resultado}")
            
            elif tipo == "binaria":
                # Convierte de binario a decimal, opera y vuelve a binario
                num1 = int(val1, 2)
                num2 = int(val2, 2)
                res_dec = eval(f"{num1} {operacion} {num2}")
                resultado = bin(res_dec).replace("0b", "")
                registrar_log(f"Cálculo Binario: {val1} {operacion} {val2} = {resultado}")

        except Exception as e:
            resultado = "Error en los datos"
            
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, port=5000)