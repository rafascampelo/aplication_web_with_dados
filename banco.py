import json
import os

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
    usuarios = ler_usuarios()
# 🚨 1. Verifica se o nome está vazio
    if not name.strip():
        print("Erro: O nome não pode estar vazio!")
        return

    # 🚨 2. Valida o formato do e-mail usando REGEX
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        print("Erro: E-mail inválido!")
        return

    # 🚨 3. Verifica se o telefone tem pelo menos 10 dígitos
    if len(telefone) < 10:
        print("Erro: O telefone deve ter pelo menos 10 dígitos!")
        return

    # 🚨 4. Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("Erro: A senha deve ter pelo menos 8 caracteres!")
        return

    novo_id = max([user["id"] for user in usuarios], default=0) + 1
    novo_usuario = {
        "id": novo_id,
        "name": name,
        "email": email,
        "senha": senha,
        "telefone": telefone
    }
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print(f"usuario {name} adicionado com sucesso!")


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

# teste das funções
# if __name__ == "__main__":
 #   adicionar_usuarios("ana", "ana@gmail", "11989879999", "senhaforte")
  #  listar_usuarios()
   # deletar_usuarios()
    # listar_usuarios()
