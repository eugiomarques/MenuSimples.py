# Abra o arquivo "crescente.txt" para escrita
with open("crescente.txt", "w") as arquivo:
    # Escreva os números no arquivo, separados por ";"
    for numero in range(1, 101):
        arquivo.write(str(numero))
        # Adicione um ";" após cada número, exceto o último
        if numero < 100:
            arquivo.write(";")

import csv
import os


# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    # Verifica se o arquivo já existe
    arquivo_existe = os.path.exists("alunos.csv")

    # Abre o arquivo em modo de escrita (append) para adicionar novos registros
    with open("alunos.csv", mode="a", newline="") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        # Se o arquivo não existia, escreve o cabeçalho
        if not arquivo_existe:
            escritor.writerow(["Nome", "Email", "Curso"])

        # Escreve o registro do aluno no arquivo
        escritor.writerow([nome, email, curso])

    print("Aluno cadastrado com sucesso!")


# Função para listar todos os alunos cadastrados
def listar_alunos():
    # Verifica se o arquivo existe
    if os.path.exists("alunos.csv"):
        with open("alunos.csv", mode="r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            for linha in leitor:
                print(f"Nome: {linha[0]}, Email: {linha[1]}, Curso: {linha[2]}")
    else:
        print("Nenhum aluno cadastrado.")


# Função para buscar um aluno pelo nome
def buscar_aluno_por_nome():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False

    # Verifica se o arquivo existe
    if os.path.exists("alunos.csv"):
        with open("alunos.csv", mode="r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            for linha in leitor:
                if nome_busca.lower() in linha[0].lower():
                    print(f"Nome: {linha[0]}, Email: {linha[1]}, Curso: {linha[2]}")
                    encontrado = True

    if not encontrado:
        print(f"Nenhum aluno com o nome '{nome_busca}' encontrado.")


# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar um novo aluno")
    print("2. Listar os alunos cadastrados")
    print("3. Buscar um aluno pelo nome")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_aluno_por_nome()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    # Verificar se os campos estão vazios
    if not nome or not email or not curso:
        print("Erro: Todos os campos (nome, email e curso) devem ser preenchidos.")
        return
    # Resto do código de cadastro aqui

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    # Verificar se os campos estão vazios
    if not nome or not email or not curso:
        print("Erro: Todos os campos (nome, email e curso) devem ser preenchidos.")
        return

    # Verificar se o nome contém números
    if any(char.isdigit() for char in nome):
        print("Erro: O nome do aluno não pode conter números.")
        return
    # Resto do código de cadastro aqui

def listar_alunos():
    try:
        with open("alunos.csv", mode="r") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")
            for linha in leitor:
                print(f"Nome: {linha[0]}, Email: {linha[1]}, Curso: {linha[2]}")
    except FileNotFoundError:
        print("Erro: O arquivo 'alunos.csv' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao listar alunos: {e}")

import sqlite3

# Conecte-se ao banco de dados (ou crie-o se não existir)
conexao = sqlite3.connect("alunos.db")

# Crie uma tabela para armazenar os dados dos alunos
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    curso TEXT NOT NULL
                )''')

# Salve as alterações e feche a conexão com o banco de dados
conexao.commit()
conexao.close()

import sqlite3

# Função para cadastrar um novo aluno no banco de dados
def cadastrar_aluno(nome, email, curso):
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, email, curso) VALUES (?, ?, ?)", (nome, email, curso))
        conexao.commit()
        conexao.close()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar aluno: {erro}")

# Função para listar todos os alunos do banco de dados
def listar_alunos():
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        conexao.close()
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
    except sqlite3.Error as erro:
        print(f"Erro ao listar alunos: {erro}")

# Função para buscar um aluno pelo nome no banco de dados
def buscar_aluno_por_nome(nome_busca):
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE ?", (f"%{nome_busca}%",))
        alunos = cursor.fetchall()
        conexao.close()
        if not alunos:
            print(f"Nenhum aluno com o nome '{nome_busca}' encontrado.")
        else:
            for aluno in alunos:
                print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
    except sqlite3.Error as erro:
        print(f"Erro ao buscar aluno: {erro}")

def buscar_aluno_por_matricula(matricula):
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE matricula = ?", (matricula,))
        aluno = cursor.fetchone()
        conexao.close()
        if aluno:
            print(f"Matrícula: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
        else:
            print(f"Aluno com a matrícula {matricula} não encontrado.")
    except sqlite3.Error as erro:
        print(f"Erro ao buscar aluno: {erro}")

def listar_alunos_por_curso(curso):
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos WHERE curso = ?", (curso,))
        alunos = cursor.fetchall()
        conexao.close()
        if not alunos:
            print(f"Nenhum aluno no curso {curso} encontrado.")
        else:
            for aluno in alunos:
                print(f"Matrícula: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
    except sqlite3.Error as erro:
        print(f"Erro ao listar alunos: {erro}")

def listar_notas_alunos():
    try:
        conexao = sqlite3.connect("alunos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT alunos.nome, notas.nota FROM alunos JOIN notas ON alunos.matricula = notas.matricula ORDER BY alunos.nome")
        notas_alunos = cursor.fetchall()
        conexao.close()
        if not notas_alunos:
            print("Nenhuma nota de aluno encontrada.")
        else:
            for aluno, nota in notas_alunos:
                print(f"Aluno: {aluno}, Nota: {nota}")
    except sqlite3.Error as erro:
        print
