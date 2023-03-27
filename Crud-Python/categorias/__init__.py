from time import sleep

def tela_opcoes():
    return print('''  
                O QUE DESEJA FAZER ? 
                1 - CRIAR MEU CADASTRO
                2 - VISUALIZAR CADASTROS
                3 - ATUALIZAR  MEU CADASTRO
                4 - DELETAR MEU CADASTRO
                0 - VOLTAR AO MENU CATEGORIAS''')

def cadastro(nome='Não informado', cpf="Não informado", idade=0, sexo='Não informado', categoria=0):
    print()
    print('CRIE SEU CADASTRO')
    if categoria == 1:
        tabela = "professores"
    elif categoria == 2:
        tabela = "alunos"
    nome = nome
    cpf = cpf
    idade = idade
    sexo = sexo

    comand_sql = f"INSERT INTO {tabela} (nome, cpf, idade, sexo) VALUES('{nome}', '{cpf}', {idade}, '{sexo}')"
    return comand_sql

def update(categoria=0):
    if categoria == 1:
        tabela = "professores"
    elif categoria == 2:
        tabela = "alunos"

    num = str(input("Digite o CPF contido no cadastro que deseja atualizar: "))
    print('Aguarde...')
    sleep(0.4)
    print("ATUALIZE SEU CADASTRO")
    nome = str(input("Nome: "))
    cpf = str(input("CPF: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: "))
    print()

    comand_sql = (f"UPDATE {tabela} SET nome = '{nome}', cpf = '{cpf}', idade={idade}, sexo = '{sexo}' WHERE cpf = '{num}' ")
    return comand_sql

def delete(categoria=0):
    if categoria == 1:
        tabela = "professores"
    elif categoria == 2:
        tabela = "alunos"

    num = str(input("Digite o CPF contido no cadastro que deseja deletar: "))
    comand_sql = f"DELETE FROM {tabela} WHERE cpf='{num}'"
    return comand_sql