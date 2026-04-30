def registrar_conta(dict_contas: dict, input_usuario: str, input_senha: str) -> bool:
    # Registra um novo usuário no sistema
    if dict_contas.get(input_usuario):
        print("Usuário já cadastrado.")
        return False
    dict_contas[input_usuario] = input_senha

def fazer_login(dict_contas: dict, input_usuario: str, input_senha: str) -> None:
    # Checa se o usuário está no dicionário de contas. Caso não esteja, mostra erro
    if input_usuario in dict_contas and dict_contas[input_usuario] == input_senha:
        input("\nConta logada com sucesso! Enter para voltar... ")
    else:
        input("\nUsuário ou senha inválidos. Enter para voltar... ")
        
def listar_missoes(missoes: list) -> None:
    # Lista as missões disponíveis para o usuário completar
    print("Essas são as missões disponíveis:")
    for i, missao in enumerate(missoes, start = 1):
        print(f"{i} - {missao["nome"]}")
        
def listar_missoes_completas(missoes_completas: list) -> None:
    # Lista as missões já completas pelo usuário
    print("Essas são as missões completas:")
    for i, missao_completa in enumerate(missoes_completas, start = 1):
        # A lista começa em 1 para o usuário, mas o índice interno continua começando em 0
        print(f"{i} - {missao_completa["nome"]}")

def completar_missoes(escolha: int, missoes: list, missoes_completas: list) -> list:
    # Move uma missão da lista de disponíveis para a lista de completas
    indice_real = escolha - 1
    
    if 0 <= indice_real < len(missoes):  
        missao = missoes.pop(indice_real)
        missoes_completas.append(missao)
    return missoes, missoes_completas