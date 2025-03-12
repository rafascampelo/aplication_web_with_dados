from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# função para conectar o bd


def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row  # retorna os dados como dicionário
    return conn

# rota para exibir os usuários


@app.route('/')
def home():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# rota para dicionar usuarios


@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']
    if not telefone.isdigit():
        return "ERRO: O telefone deve conter apenas números."

    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, email, senha, telefone) VALUES (?, ?, ?, ?)',
                 (name, email, senha, int(telefone)))
    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
