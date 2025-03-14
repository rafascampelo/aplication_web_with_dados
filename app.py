from flask import Flask, render_template, request, jsonify
import json
import os
app = Flask(__name__)

JSON_FILE = "banco.json"

# função para carregar usuarios do JSON


def ler_usuarios():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

# Função para salvar usuários no JSON


def salvar_usuarios(usuarios):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)

# rota para exibir os usuarios na pg html


@app.route("/")
def index():
    users = ler_usuarios()
    return render_template("index.html", users=users)

# rota para adicionar um usuario pelo forms


@app.route("/add", methods=["POST"])
def adicionar_usuarios():
    data = request.form
    usuarios = ler_usuarios()
    novo_id = max([user["id"] for user in usuarios], default=0) + 1

    novo_usuario = {
        "id": novo_id,
        "name": data["name"],
        "email": data["email"],
        "telefone": data["telefone"],
        "senha": data["senha"]
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)


if __name__ == "__main__":
    app.run(debug=True)
