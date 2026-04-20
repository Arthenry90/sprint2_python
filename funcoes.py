def registrar_conta(dict_contas: dict, input_usuario, input_senha) -> bool:
    if dict_contas.get(input_usuario):
        print("Usuario já cadastrado.")
        return False
    dict_contas[input_usuario] = input_senha


def fazer_login(dict_contas: dict, input_usuario, input_senha):
    for usuario, senha in dict_contas.items():
        print(usuario, senha)
        if usuario == input_usuario and senha == input_senha:
            print("Fez login")
        else:
            print("Erro ao logar")
        


if __name__ == "__main__":
    dict_logins = {"Artur": "1234"}
    # registrar_conta(dict_logins,"artur", "1234")

    fazer_login(dict_logins,"Artur", "1234")
    # for items in dict_logins.items():
    #     print(items)

    # for i in dict_logins.items():
    #     print(i)