def registrar_conta(dict_contas: dict, input_usuario, input_senha) -> bool:
    if dict_contas.get(input_usuario):
        print("Usuario já cadastrado.")
        return False
    dict_contas[input_usuario] = input_senha





if __name__ == "__main__":
    dict_logins = {"Artur": 1234}
    registrar_conta(dict_logins,"artur", "1234")

    # for items in dict_logins.items():
    #     print(items)

    for i in dict_logins.items():
        print(i)