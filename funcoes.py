import os
import json

ARQUIVO_BD = "dados.json"

DADOS_INICIAIS = {
    "usuarios": {},
    "missoes": [],
    "missoes_completas": []
}

DEFAULT_MISSOES = [
    {"nome": "Tomar 1 litro de água"},
    {"nome": "Dar 10.000 passos"},
    {"nome": "Correr por 20 minutos"},
]

def iniciar_arquivo():
    """Inicializa o arquivo de banco de dados JSON com a estrutura padrão, caso não exista."""
    if not os.path.exists(ARQUIVO_BD):
        print(f"Arquivo '{ARQUIVO_BD}' não encontrado. Inicializando novo banco de dados...")
        with open(ARQUIVO_BD, "w", encoding="utf-8") as arquivo:
            json.dump(DADOS_INICIAIS, arquivo, indent=4, ensure_ascii=False)
        print("Arquivo inicializado com sucesso!")

def carregar_dados():
    """Carrega e retorna os dados do arquivo JSON. Se estiver corrompido, recria do zero."""
    try:
        with open(ARQUIVO_BD, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
    except FileNotFoundError:
        iniciar_arquivo()
        conteudo = DADOS_INICIAIS.copy()
    except json.JSONDecodeError:
        iniciar_arquivo()
        conteudo = DADOS_INICIAIS.copy()
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar dados: {e}") from e

    for k, v in DADOS_INICIAIS.items():
        if k not in conteudo:
            conteudo[k] = v

    return conteudo

def salvar_dados(dados: dict) -> None:
    """Salva o dicionário de dados no arquivo JSON de forma formatada e segura."""
    try:
        with open(ARQUIVO_BD, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar dados: {e}") from e

def criar_usuario(username: str, password: str, peso: float, altura: float) -> bool:
    """Cria um novo usuário calculando o IMC, define níveis de XP iniciais e atribui missões."""
    data = carregar_dados()
    if username in data.get("usuarios", {}):
        return False

    try:
        peso_f = float(peso)
        altura_f = float(altura)
        if altura_f <= 0:
            raise ValueError("Altura deve ser maior que zero")
        imc = round(peso_f / (altura_f ** 2), 2)
    except Exception as e:
        raise ValueError(f"Dados físicos inválidos: {e}")

    if imc < 18.5:
        assigned = [
            {"nome": "Tomar 1 litro de água"},
            {"nome": "Caminhar 20 minutos"},
            {"nome": "Alongamento 10 minutos"},
        ]
    elif imc < 25:
        assigned = DEFAULT_MISSOES.copy()
    elif imc < 30:
        assigned = [
            {"nome": "Tomar 1 litro de água"},
            {"nome": "Caminhar 30 minutos"},
            {"nome": "Dar 5.000 passos"},
        ]
    else:
        assigned = [
            {"nome": "Tomar 1 litro de água"},
            {"nome": "Caminhar 15 minutos"},
            {"nome": "Alongamento 15 minutos"},
        ]

    if "usuarios" not in data:
        data["usuarios"] = {}
        
    data["usuarios"][username] = {
        "password": password,
        "peso": peso_f,
        "altura": altura_f,
        "imc": imc,
        "xp": 0,
        "nivel": 1,
        "missoes": assigned,
        "missoes_completas": []
    }

    salvar_dados(data)
    return True

def autenticar_usuario(username: str, password: str) -> bool:
    """Verifica se o usuário existe no banco de dados e se a senha fornecida está correta."""
    data = carregar_dados()
    user = data.get("usuarios", {}).get(username)
    if not user:
        return False
    return user.get("password") == password

def deletar_usuario(username: str) -> bool:
    """Remove o usuário e todos os seus dados permanentemente do banco de dados JSON."""
    data = carregar_dados()
    if "usuarios" in data and username in data["usuarios"]:
        del data["usuarios"][username]
        salvar_dados(data)
        return True
    return False

def editar_usuario(username: str, peso: float, altura: float) -> bool:
    """Edita as informações físicas do usuário (peso e altura) e recalcula o IMC."""
    data = carregar_dados()
    user = data.get("usuarios", {}).get(username)
    if not user:
        return False

    try:
        peso_f = float(peso)
        altura_f = float(altura)
        if altura_f <= 0:
            raise ValueError("Altura deve ser maior que zero")
        imc = round(peso_f / (altura_f ** 2), 2)
    except Exception as e:
        raise ValueError(f"Dados físicos inválidos: {e}")

    user["peso"] = peso_f
    user["altura"] = altura_f
    user["imc"] = imc
    
    salvar_dados(data)
    return True

def obter_perfil_usuario(username: str) -> dict:
    """Retorna os dados completos do usuário, útil para acessar XP, Nível e IMC."""
    data = carregar_dados()
    return data.get("usuarios", {}).get(username, {})

def obter_missoes_usuario(username: str) -> list:
    """Retorna a lista de missões que ainda estão pendentes para o usuário selecionado."""
    data = carregar_dados()
    return data.get("usuarios", {}).get(username, {}).get("missoes", [])

def obter_missoes_completas_usuario(username: str) -> list:
    """Retorna a lista de missões que o usuário selecionado já completou."""
    data = carregar_dados()
    return data.get("usuarios", {}).get(username, {}).get("missoes_completas", [])

def adicionar_missao_personalizada(username: str, nome_missao: str) -> bool:
    """Adiciona uma missão com título personalizado na lista de pendências do usuário."""
    data = carregar_dados()
    user = data.get("usuarios", {}).get(username)
    if not user:
        return False
        
    if "missoes" not in user:
        user["missoes"] = []
        
    user["missoes"].append({"nome": nome_missao})
    salvar_dados(data)
    return True

def completar_missao_usuario(username: str, index_1based: int) -> dict:
    """Completa a missão e retorna um dicionário com os resultados (XP e Level Up seguros)."""
    data = carregar_dados()
    user = data.get("usuarios", {}).get(username)
    
    if not user:
        return {"sucesso": False}
        
    idx = index_1based - 1
    missoes = user.get("missoes", [])
    
    if 0 <= idx < len(missoes):
        missao = missoes.pop(idx)
        if "missoes_completas" not in user:
            user["missoes_completas"] = []
        user["missoes_completas"].append(missao)
        
        # SISTEMA DE GAMIFICAÇÃO (Ficou mais fácil upar)
        xp_ganho = 20
        user["xp"] = user.get("xp", 0) + xp_ganho
        
        subiu_nivel = False
        xp_necessario = user.get("nivel", 1) * 30 # Alterado para 30
        
        while user["xp"] >= xp_necessario:
            user["xp"] -= xp_necessario  
            user["nivel"] += 1           
            subiu_nivel = True
            xp_necessario = user["nivel"] * 30 # Alterado para 30
        
        salvar_dados(data)
        return {
            "sucesso": True, 
            "xp_ganho": xp_ganho, 
            "subiu_nivel": subiu_nivel, 
            "nivel": user["nivel"]
        }
        
    return {"sucesso": False}

def listar_missoes(missoes: list) -> None:
    """Imprime no terminal de forma enumerada as missões pendentes."""
    print("Essas são as missões disponíveis:")
    try:
        if not missoes:
            print("  Nenhuma missão pendente!")
        for i, missao in enumerate(missoes, start=1):
            print(f"{i} - {missao['nome']}")
    except Exception as e:
        print(f"Erro ao listar missões: {e}")

def listar_missoes_completas(missoes_completas: list) -> None:
    """Imprime no terminal de forma enumerada as missões que já foram concluídas."""
    print("Essas são as missões completas:")
    try:
        if not missoes_completas:
            print("  Nenhuma missão completada ainda.")
        for i, missao_completa in enumerate(missoes_completas, start=1):
            print(f"{i} - {missao_completa['nome']}")
    except Exception as e:
        print(f"Erro ao listar missões completas: {e}")