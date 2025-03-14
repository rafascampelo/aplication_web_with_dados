
from flask import Flask, render_template, jsonify, request, redirect, url_for
# Importando as funções do banco.py
from banco import ler_usuarios, adicionar_usuarios, salvar_usuarios
import re
import os
import json


app = Flask(__name__)

JSON_FILE = "banco.json"

# rota para exibir os usuarios na pg html


@app.route("/")
def index():
    users = ler_usuarios()
    return render_template("index.html", users=users)

# rota para adicionar um usuario pelo forms


@app.route("/add", methods=["POST"])
def cadastrar_usuarios():
    data = request.form
    if not all(key in data for key in ["name", "email", "telefone", "senha"]):
        return jsonify({"erro": "todos os campos são obrigatorios!"}), 400

    resultado = adicionar_usuarios(
        data["name"], data["email"], data["telefone"], data["senha"])

    if "erro" in resultado:
        return jsonify(resultado), 400
    return redirect(url_for("index.html"))


if __name__ == "__main__":
    app.run(debug=True)
