import pymysql as pybd
from time import sleep
from categorias import *
from conexao import *

conexaodb = conectar("localhost", "root", "", "escola")


while True:
    escolha = 5
    print(f'''
    
{'=-' * 5} BANCO DE DADOS ESCOLAR {'-=' * 5}

        SEJAM BEM VINDOS !!!


            CATEGORIAS

        [1] PROFESSORES
        [2] ALUNOS

        [0] EXIT 

    ''')
    categoria = int(input("SUA CATEGORIA: "))
    if categoria == 0:
        break
    elif categoria != 1 and categoria != 2 and categoria != 0:
        print("[ERRO] CATEGORIA INVALIDA! TENTE NOVAMENTE!")
    else:
        while True:
            if categoria == 1:
                print()
                print(f'CONECTANDO-SE AO BANCO DE DADOS...')
                print()
                sleep(2)
                cursor = conexaodb.cursor()
                tela_opcoes()

                escolha = int(input("Opção: "))

                if escolha == 1:
                    cursor.execute(cadastro(input('Nome: '), input('CPF: '), int(input('Idade: ')) ,input('Sexo: '), categoria))
                    conexaodb.commit()
                    print("CADASTRANDO NO SISTEMA...")
                    sleep(1.5)
                    print(cursor.rowcount, "PROFESSOR(A) CADASTRATADO COM SUCESSO !!! ")

                elif escolha == 2:
                    comand_sql  = "SELECT * FROM professores"
                    cursor.execute(comand_sql)
                    print('BUSCANDO CADASTROS...')
                    sleep(1)
                    totalRows = cursor.rowcount
                    resultado = cursor.fetchall()
                    print()
                    if totalRows > 0:
                        print('ID  -  NOME  -  CPF  -  IDADE  -  SEXO')
                        for x in resultado:
                            print(x)
                    else:
                        print('Não há Cadastros no sistema!')

                elif escolha == 3:
                    cursor.execute(update(categoria))
                    conexaodb.commit()
                    print("ATUALIZANDO CADASTRO...")
                    sleep(1.5)
                    print(cursor.rowcount, "CADASTRO ATUALIZADO COM SUCESSO !!!")

                elif escolha == 4:
                    cursor.execute(delete(categoria))
                    conexaodb.commit()
                    print()
                    print("DELETANDO CADASTRO...")
                    sleep(1.5)
                    print(cursor.rowcount, "CADASTRO DELETADO COM SUCESSO !!!")

                elif escolha == 0:
                    break
                else:
                    print()
                    print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
            elif categoria == 2:
                print()
                print(f'CONECTANDO-SE AO BANCO DE DADOS...')
                print()
                sleep(2)
                cursor = conexaodb.cursor()
                tela_opcoes()

                escolha = int(input("Opção: "))

                if escolha == 1:
                    cursor.execute(cadastro(input('Nome: '), input('CPF: '), int(input('Idade: ')), input('Sexo: '), categoria))
                    conexaodb.commit()
                    print("CADASTRANDO NO SISTEMA...")
                    sleep(1.5)
                    print(cursor.rowcount, "ALUNO(A) CADASTRATADO COM SUCESSO !!! ")

                elif escolha == 2:
                    comand_sql = "SELECT * FROM alunos"
                    cursor.execute(comand_sql)
                    print("BUSCANDO CADASTROS...")
                    sleep(1.5)
                    totalRows = cursor.rowcount
                    resultado = cursor.fetchall()
                    print()
                    if totalRows > 0:
                        print('ID  -  NOME  -  CPF  -  IDADE  -  SEXO')
                        for x in resultado:
                            print(x)
                    else:
                        print('Não há Cadastros no sistema!')

                elif escolha == 3:

                    cursor.execute(update(categoria))

                    conexaodb.commit()

                    print("ATUALIZANDO CADASTRO...")

                    sleep(1.5)

                    print(cursor.rowcount, "CADASTRO ATUALIZADO COM SUCESSO !!!")

                elif escolha == 4:

                    cursor.execute(delete(categoria))
                    conexaodb.commit()
                    print()
                    print("DELETANDO CADASTRO...")
                    sleep(1.5)
                    print(cursor.rowcount, "CADASTRO DELETADO COM SUCESSO !!!")

                elif escolha == 0:
                    break
                else:
                    print()
                    print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
            elif categoria == 0:
                break

print('''
SAINDO...
''')
sleep(1.5)
print('OBRIGADO PELA PREFERÊNCIA ! VOLTE SEMPRE  ')
