import os
from funcoes import *

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    dict_logins = {}
    missoes = [{"nome" : "Dragao"}, {"nome" : "Caverna"}]
    missoes_completas = []
    
    rodando = True
    while rodando:
        print("--- MENU CARE PLUS ---\n")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Listar missoes")
        print("4 - Completar missao")
        print("0 - Sair")

        input_escolha = input("Opção: ")

        match input_escolha:
            case "1":
                limpar()
                print("--- CADASTRO DE CONTA")
                nome = input("Usuário: ")
                senha = input("Senha: ")
                
                registrar_conta(dict_logins, nome, senha)
                
                input("\nConta registrada! Enter para voltar... ")
                limpar()

            case "2":
                # Terminar essa aqui
                print("Ola")
                fazer_login()
                
            case "3":
                limpar()
                listar_missoes(missoes)
                listar_missoes_completas(missoes_completas)
                
            case "4":
                limpar()
                listar_missoes(missoes)
                completa_missao = int(input("Digite um numero para completar uma missao: "))
                completar_missoes(completa_missao, missoes, missoes_completas)
                input("\nMissao Completa! Enter para voltar... ")
                limpar()
                
            case "0":
                print("Saindo do sistema...")
                rodando = False
            
            case _:
                print("Opção inválida!")
                input("Pressione Enter para continuar... ")
                limpar()

limpar()
exibir_menu()