from srv.view import View

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="template")


view = View()


@app.route("/", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if id := view.auth_validation(usuario, senha):
            return redirect(url_for("client", id=id))
        else:
            return render_template("index.html", erro="Usuário ou senha inválidos")


@app.route("/client/<int:id>")
def client(id):
    return render_template("pag2Cliente.html")


@app.route("/table/")
def table():
    id = request.form["id"]
    database = LambeijosDB()
    dados = database.ler_mensagens()

    return render_template("tabela.html", dados)


if __name__ == "__main__":
    app.run(debug=True)  # Executa a aplicação
