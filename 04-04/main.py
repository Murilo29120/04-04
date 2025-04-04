import json

arquivo_cadastros = "cadastros.json" 

def exibir_menu():
    print("\n---- MENU CADASTRO ----")
    print("1 - Cadastrar pessoa")
    print("2- Ver cadastros")
    print("3 - sair")
    print("-----------------------------")

def salvar_cadastros (cadastros):
     with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
          json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)
def carregar_cadastros():
     try:
          with open (arquivo_cadastros, "R", encoding="utf-8") as arquivo:
               return json. load(arquivo)
     except (FileNotFoundError, json.JSONDecodeError):
          return[]
     
     def cadastrar_pessoa(cadastros):
          nome = input("nome:")
          idade = input("idade")
          turma = input("turma")
          curso = input("curso")

     cadastros.append({"Nome:": nome, "Idade": idade, "Turma": turma, "Curso": curso})
     salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso")