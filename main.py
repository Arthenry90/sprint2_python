import os
from funcoes import *

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    iniciar_arquivo()
    
    rodando = True
    current_user = None

    while rodando:
        limpar()
        print(r"""
  __  __                    _____                _____  _        
 |  \/  |                  / ____|              |  __ \| |       
 | \  / | ___ _ __  _   _ | |     __ _ _ __ ___ | |__) | |_   _ ___ 
 | |\/| |/ _ \ '_ \| | | || |    / _` | '__/ _ \|  ___/| | | | / __|
 | |  | |  __/ | | | |_| || |___| (_| | | |  __/| |    | | |_| \__ \
 |_|  |_|\___|_| |_|\__,_| \_____\__,_|_|  \___||_|    |_|\__,_|___/
              """)
        print("======================================================================")
        if current_user:
            perfil = obter_perfil_usuario(current_user)
            nivel = perfil.get('nivel', 1)
            xp = perfil.get('xp', 0)
            imc = perfil.get('imc', 0)
            xp_necessario = nivel * 30
            
            print(f" Status: LOGADO como '{current_user}' | Nível: {nivel} | XP: {xp}/{xp_necessario} | IMC: {imc}")
        else:
            print(" Status: NÃO LOGADO")
        print("======================================================================\n")
        
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Listar missões")
        print("4 - Completar missão")
        print("5 - Adicionar missão personalizada")
        print("6 - Ver meu progresso")
        print("7 - Editar meu perfil")
        print("8 - Excluir minha conta")
        if current_user:
            print("9 - Fazer Logout")
        print("0 - Sair\n")

        input_escolha = input("Opção: ")

        match input_escolha:
            case "1":
                limpar()
                print("--- CADASTRO DE CONTA ---")
                nome = input("Usuário.....: ")
                senha = input("Senha.......: ")
                peso = input("Peso (kg)...: ")
                altura = input("Altura (m)..: ")
                try:
                    if not nome.strip() or not senha.strip():
                        input("\nNome ou senha inválidos. Enter para voltar... ")
                    else:
                        ok = criar_usuario(nome.strip(), senha.strip(), peso, altura)
                        if ok:
                            input("\nConta registrada! Faça login para continuar. Enter para voltar... ")
                        else:
                            input("\nUsuário já existe. Enter para voltar... ")
                except Exception as e:
                    input(f"\nErro ao criar conta: {e}. Enter para voltar... ")

            case "2":
                limpar()
                if current_user:
                    input("Você já está logado! Faça logout primeiro se quiser trocar de conta. Enter para voltar... ")
                    continue
                print("--- LOGAR NA CONTA ---")
                login_nome = input("Usuário.....: ")
                login_senha = input("Senha.......: ")
                try:
                    if autenticar_usuario(login_nome.strip(), login_senha.strip()):
                        current_user = login_nome.strip()
                        input("\nConta logada com sucesso! Enter para continuar... ")
                    else:
                        input("\nUsuário ou senha inválidos. Enter para voltar... ")
                except Exception as e:
                    input(f"\nErro ao tentar autenticar: {e}. Enter para voltar... ")

            case "3":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa fazer login para visualizar suas missões. Enter para voltar... ")
                    continue
                
                print(f"--- MISSÕES DE {current_user.upper()} ---")
                try:
                    listar_missoes(obter_missoes_usuario(current_user))
                    print("\n--- MISSÕES COMPLETAS ---")
                    listar_missoes_completas(obter_missoes_completas_usuario(current_user))
                except Exception as e:
                    print(f"Erro ao listar missões: {e}")
                input("\nEnter para voltar... ")
                
            case "4":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa fazer login para completar missões. Enter para voltar... ")
                    continue
                
                missoes_atual = obter_missoes_usuario(current_user)
                listar_missoes(missoes_atual)
                
                if not missoes_atual:
                    input("\nVocê não possui missões pendentes. Enter para voltar... ")
                    continue

                escolha = input("\nDigite um número para completar uma missão (ou 0 para voltar): ")
                if escolha == "0":
                    continue
                try:
                    if not escolha.isdigit():
                        input("\nEntrada inválida. Enter para voltar... ")
                    else:
                        indice = int(escolha)
                        resultado = completar_missao_usuario(current_user, indice)
                        
                        if resultado.get("sucesso"):
                            print(f"\nMissão completa! Você ganhou +{resultado['xp_ganho']} XP.")
                            if resultado.get("subiu_nivel"):
                                print(f"🎉 PARABÉNS! Você subiu para o Nível {resultado['nivel']}! 🎉")
                            input("\nEnter para voltar... ")
                        else:
                            input("\nÍndice inválido. Enter para voltar... ")
                except Exception as e:
                    input(f"\nErro ao completar missão: {e}. Enter para voltar... ")
                    
            case "5":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa fazer login para adicionar missões. Enter para voltar... ")
                    continue
                
                print("--- ADICIONAR MISSÃO PERSONALIZADA ---")
                nova_missao = input("Digite o hábito/missão que deseja adicionar (ou deixe em branco para cancelar): ")
                
                if nova_missao.strip():
                    if adicionar_missao_personalizada(current_user, nova_missao.strip()):
                        input("\nMissão adicionada com sucesso! Enter para voltar... ")
                    else:
                        input("\nErro ao adicionar missão. Enter para voltar... ")
            
            case "6":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa fazer login para ver seu progresso. Enter para voltar... ")
                    continue
                
                perfil = obter_perfil_usuario(current_user)
                nivel = perfil.get('nivel', 1)
                xp = perfil.get('xp', 0)
                missoes_completadas = len(perfil.get('missoes_completas', []))
                
                xp_necessario = nivel * 30
                xp_faltante = xp_necessario - xp
                
                print(f"--- PROGRESSO DE {current_user.upper()} ---")
                print(f"Nível Atual.......: {nivel}")
                print(f"Progresso da Barra: {xp} / {xp_necessario} XP")
                print(f"Missões Concluídas: {missoes_completadas}")
                print(f"Faltam {xp_faltante} XP para alcançar o Nível {nivel + 1}!")
                
                input("\nEnter para voltar... ")

            case "7":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa estar logado para editar seu perfil. Enter para voltar... ")
                    continue
                
                print("--- EDITAR PERFIL ---")
                print("Atualize suas informações corporais. Deixe em branco caso deseje cancelar.")
                novo_peso = input("Novo Peso (kg)...: ")
                if not novo_peso.strip():
                    continue
                    
                nova_altura = input("Nova Altura (m)..: ")
                if not nova_altura.strip():
                    continue
                
                try:
                    if editar_usuario(current_user, novo_peso, nova_altura):
                        input("\nPerfil atualizado com sucesso! Seu IMC foi recalculado. Enter para voltar... ")
                    else:
                        input("\nErro ao atualizar perfil. Enter para voltar... ")
                except Exception as e:
                    input(f"\nErro ao editar perfil: {e}. Enter para voltar... ")

            case "8":
                limpar()
                if not current_user:
                    input("ACESSO NEGADO: Você precisa estar logado para excluir sua conta. Enter para voltar... ")
                    continue
                
                print("--- EXCLUSÃO DE CONTA ---")
                print("CUIDADO: Esta ação apagará permanentemente seu usuário e histórico de missões!")
                confirmar = input(f"Tem certeza que deseja deletar a conta '{current_user}'? (S/N): ")
                
                if confirmar.strip().upper() == "S":
                    if deletar_usuario(current_user):
                        current_user = None
                        input("\nSua conta foi removida com sucesso. Enter para voltar... ")
                    else:
                        input("\nErro ao deletar conta. Enter para voltar... ")
                else:
                    input("\nOperação cancelada. Enter para voltar... ")

            case "9":
                if current_user:
                    current_user = None
                    input("\nLogout efetuado com sucesso. Enter para continuar... ")
                else:
                    print("\nOpção inválida!")
                    input("Pressione Enter para continuar... ")

            case "0":
                print("Salvando dados e saindo do sistema... Até logo!")
                rodando = False
            
            case _:
                print("\nOpção inválida!")
                input("Pressione Enter para continuar... ")

if __name__ == "__main__":
    exibir_menu()