import os
from funcoes import *

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    
    # Define um dicionário de contas que armazena usuário e senha
    dict_contas = {}
    
    # Lista de missões disponíveis
    missoes = [{"nome": "Tomar 1 litro de água"}, 
               {"nome": "Dar 10.000 passos"},
               {"nome": "Correr por 20 minutos"},]
    
    # Lista de missões completas
    missoes_completas = []
    
    rodando = True
    # Loop do menu
    while rodando:
        print("""
  __  __                     _____                 _____  _        
 |  \/  |                   / ____|               |  __ \| |          
 | \  / | ___ _ __  _   _  | |     __ _ _ __ ___  | |__) | |_   _ ___ 
 | |\/| |/ _ \ '_ \| | | | | |    / _` | '__/ _ \ |  ___/| | | | / __|
 | |  | |  __/ | | | |_| | | |___| (_| | | |  __/ | |    | | |_| \__ \\
 |_|  |_|\___|_| |_|\__,_|  \_____\__,_|_|  \___| |_|    |_|\__,_|___/
              """)
        print("======================================================================\n")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Listar missões")
        print("4 - Completar missão")
        print("0 - Sair")

        input_escolha = input("Opção: ")

        match input_escolha:
            case "1":
                limpar()
                print("--- CADASTRO DE CONTA")
                nome = input("Usuário.....: ")
                senha = input("Senha.......: ")
                
                registrar_conta(dict_contas, nome, senha)
                
                input("\nConta registrada! Enter para voltar... ")
                limpar()

            case "2":
                limpar()
                print("--- LOGAR NA CONTA")
                login_nome = input("Usuário.....: ")
                login_senha = input("Senha.......: ")
                
                fazer_login(dict_contas, login_nome, login_senha)
                
                limpar()

            case "3":
                limpar()
                print("--- MISSÕES DISPONÍVEIS")
                listar_missoes(missoes)
                print("\n--- MISSÕES COMPLETAS")
                listar_missoes_completas(missoes_completas)
                input("\nEnter para voltar... ")
                limpar()
                
            case "4":
                limpar()
                listar_missoes(missoes)
                completa_missao = int(input("\nDigite um número para completar uma missão: "))
                completar_missoes(completa_missao, missoes, missoes_completas)
                input("\nMissão completa! Enter para voltar... ")
                limpar()
                
            case "0":
                print("Saindo do sistema...")
                rodando = False
            
            case _:
                print("\nOpção inválida!")
                input("Pressione Enter para continuar... ")
                limpar()

limpar()
exibir_menu()