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

def ver_cadastros(cadastros):
     if not cadastros:
                 print("Nenhum cadastro no sistema.")
     else:
      print("\n------ LISTA DE CADASTROS------")
      for i, pessoa in enumerate (cadastros, 1):
                     print(F"{i}. Nome:{pessoa['Nome']}, Idade:
 {pessoa ['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']})
     input("\nPressione Enter para voltar ao menu....)
           
      def main():
     cadastros= []
     cadastros = []
     while True:
         exibir_menu ()
         opção= input("Escolha uma opção: ")
         if opção == "1":
         exibir_menu()
         opcao = input("Escolha uma opção: ")
         if opcao == "1":
             cadastrar_pessoa(cadastros)
         elif opção == "2":
         elif opcao == "2":
             ver_cadastros(cadastros)
         elif opção == "3":
             print("Obrigado por utilizar nosso sistemas!")      
         elif opcao == "3":
             print("Obrigado por utilizar nosso sistema!")      
             break      
         else:
             print("Opção incorreta! Tente novamente.")
 
 if __name__ == "__main__":
     main()