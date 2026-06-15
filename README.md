# Sprint 3 - Care Plus 2026 - Python

## Descrição do projeto

O sistema foi desenvolvido em Python com o objetivo de incentivar hábitos saudáveis através de um sistema gamificado de missões.

A aplicação funciona via terminal e permite que o usuário crie uma conta (informando seus dados físicos para o cálculo automático do IMC), faça login e interaja com missões do dia a dia, como beber água ou se exercitar. As missões iniciais são atribuídas de forma inteligente com base no IMC do usuário, visando adequar os desafios à sua condição física.

O projeto foi desenvolvido utilizando Python puro, com foco em lógica de programação, manipulação de dicionários e listas, e persistência de dados utilizando a biblioteca nativa `json`.

### Principais Funcionalidades:
- **Autenticação:** Criação de conta, login, logout e exclusão de usuário.
- **Saúde e Perfil:** Cálculo do IMC no cadastro e opção de editar peso/altura futuramente para recalcular as metas.
- **Gamificação:** Sistema de níveis e barra de XP. Cada missão completa concede 20 XP, fazendo o usuário subir de nível progressivamente.
- **Missões Personalizadas:** Além das missões geradas pelo sistema, o usuário pode cadastrar seus próprios hábitos.
- **Persistência de Dados:** Todo o progresso, missões e perfis ficam salvos localmente em um arquivo `dados.json`.

---

## Integrantes

- Artur Henrique Siqueira - RM566986  
- Davi de Souza Malta - RM560327  
- Guilherme de Oliveira Scremin - RM564788  
- Guilherme Cruz Alves - RM566861  
- Pedro Sales Ferreira - RM566910  

---

## Instruções de Uso

### Como testar a aplicação:

1. Execute o arquivo principal (`main.py` / `menu.py`).
2. Escolha a opção **1** para criar uma conta. O sistema pedirá um nome de usuário, senha, peso (kg) e altura (m).
3. Escolha a opção **2** para fazer login com as credenciais criadas.
4. Após logar, explore as opções do menu interativo:
   - **3** para listar suas missões pendentes e já completadas.
   - **4** para completar uma missão e ganhar XP.
   - **5** para criar e adicionar uma missão personalizada à sua lista.
   - **6** para visualizar seu progresso (Nível, XP acumulado, XP faltante para o próximo nível e IMC).
   - **7** para atualizar seu peso e altura.
   - **8** para excluir sua conta do banco de dados.
   - **9** para fazer logout.
5. Digite **0** a qualquer momento no menu principal para sair do sistema e salvar os dados.

---

### Estrutura de arquivos importante:

- `main.py` (ou `menu.py`) — Responsável pela interface do terminal, menu principal e interação direta com o usuário.
- `funcoes.py` — Contém a lógica de negócio, cálculos (como IMC e Nível), sistema de gamificação e as operações de leitura/escrita no banco de dados.
- `dados.json` — Arquivo gerado automaticamente pelo sistema na primeira execução para armazenar de forma persistente os perfis, missões e progresso de cada usuário.