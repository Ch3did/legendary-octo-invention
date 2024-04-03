from flask import Flask, render_template,  request

app = Flask(__name__, template_folder="template")

@app.route("/", methods=['GET', 'POST'])
def auth():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        request.form["usuário"]
        request.form["senha"]


@app.route("/client/")
def client():
    return render_template("pag2Cliente.html")


@app.route("/table/")
def table():
    return render_template("tabela.html")


@app.route("/boletim1/")
def boletim1():
    return render_template("Boletim1.html")


@app.route("/boletim2/")
def boletim2():
    return render_template("Boletim2.html")


if __name__ == "__main__":
    app.run(debug=True)  # Executa a aplicação
