import json
import os
import re

# função para ler usuarios JSON


def ler_usuarios():
    if not os.path.exists("banco.json"):
        return []

    with open("banco.json", "r", encoding="utf-8") as file:
        return json.load(file)

# função para salvar usuarios no json


def salvar_usuarios(usuarios):
    with open("banco.json", "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)


# função adicionar usuarios
def adicionar_usuarios(name, email, telefone, senha):
    # Se `ler_usuarios()` retornar None, usa uma lista vazia
    usuarios = ler_usuarios() or []

    # Verifica se o e-mail já existe
    if any(user["email"] == email for user in usuarios):
        return {"erro": "E-mail já cadastrado!"}

    novo_id = max([user["id"] for user in usuarios], default=0) + \
        1  # Garante que o ID seja único
    novo_usuario = {
        "id": novo_id,
        "name": name,
        "email": email,
        "senha": senha,
        "telefone": telefone
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)  # Salva no JSON

    return novo_usuario  # Retorna os dados do novo usuário

# deleta usuarios do json


def deletar_usuarios(user_id):
    usuarios = ler_usuarios()
    usuarios = [user for user in usuarios if user["id"] != user_id]
    salvar_usuarios(usuarios)
    print(f"usuarios com id {user_id} removido!")

# função para listar


def listar_usuarios():
    usuarios = ler_usuarios()
    if not usuarios:
        print("nenhum usuario encontrado.")
        return
    for user in usuarios:
        print(f"{user['id']} - {user['name']} ({user['email']})")
