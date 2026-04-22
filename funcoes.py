def registrar_conta(dict_contas: dict, input_usuario: str, input_senha: str) -> bool:
    if dict_contas.get(input_usuario):
        print("Usuario já cadastrado.")
        return False
    dict_contas[input_usuario] = input_senha


def fazer_login(dict_contas: dict, input_usuario: str, input_senha: str):
    for usuario, senha in dict_contas.items():
        print(usuario, senha)
        if usuario == input_usuario and senha == input_senha:
            print("Conta logada com sucesso!")
        else:
            print("Erro ao logar! Senha ou úsuario invalídos")
        
def listar_missoes(missoes: list) -> None:
    print("Essas sao as missoes disponiveis:")
    for i, missao in enumerate(missoes, start = 1):
        print(f"{i} - {missao["nome"]}")
        
def listar_missoes_completas(missoes_completas: list) -> None:
    print("Essas sao as missoes completas:")
    for i, missao_completa in enumerate(missoes_completas, start = 1):
        print(f"{i} - {missao_completa["nome"]}")

def completar_missoes(escolha: int, missoes: list, missoes_completas: list) -> list:
    indice_real = escolha - 1
    
    if 0 <= indice_real < len(missoes):  
        missao = missoes.pop(indice_real)
        missoes_completas.append(missao)
    return missoes, missoes_completas

if __name__ == "__main__":
    dict_logins = {"Artur": "1234"}
    # registrar_conta(dict_logins,"artur", "1234")

    fazer_login(dict_logins,"Artur", "1234")
    # for items in dict_logins.items():
    #     print(items)

    # for i in dict_logins.items():
    #     print(i)