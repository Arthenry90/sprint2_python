import os
from funcoes import *

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    dict_logins = {}
    
    rodando = True
    while rodando:
        print("--- MENU CARE PLUS ---\n")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("0 - Sair")

        input_escolha = input("Opção: ")

        match input_escolha:
            case "1":
                limpar()
                print("--- CADASTRO DE CONTA")
                nome = input("Usuário: ")
                senha = input("Senha: ")
                
                registrar_conta(dict_logins, nome, senha)
                
                input("\nConta registrada! Enter para voltar...")
                limpar()

            case "2":
                # Terminar essa aqui
                print("Ola")
                fazer_login()

            case "0":
                print("Saindo do sistema...")
                rodando = False
            
            case _:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
                limpar()

limpar()
exibir_menu()