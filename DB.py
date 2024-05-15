import mysql.connector

# C R U D 
# CREATE
# READ
# UPDATE
# DELETE

def BancoDados(opc='',id_c=0,nome_c='', idade_c=0):
    conexao = mysql.connector.connect(
        # "Coloque aqui as informações do seu SGBD MySQL"
        host = 'xxxx',
        user='xxxx',
        password='xxxx',
        database='xxxx',
    )

    cursor = conexao.cursor()

    n = 1
    id = id_c
    nome = nome_c
    idade = idade_c
    listaNomes = []
    lista = ''
    espaco = ' '
    traco = '-'
    nm = 'Nome'
    di = 'Id'
    age1 = 'Idade'
    try:
        match opc:
            case 'BuscaID':
                comandoSelect = f'SELECT * FROM usuarios where id = "{id_c}"'
                cursor.execute(comandoSelect)
                resultado = cursor.fetchall() # ler o banco de dados
                a = 0
                
                for c in resultado:
                    law = [c[a], c[a+1], c[a+2]]
                listaNomes.append(law)
                return listaNomes

            
            case 'BuscaIdade':
                num = 0
                comandoSelect1 = f'SELECT * FROM usuarios WHERE idade = {idade}'
                cursor.execute(comandoSelect1)
                resultado1 = cursor.fetchall() # ler o banco de dados

                for c in resultado1:
                    m = str(resultado1[num][0]).center(10)
                    l = resultado1[num][1].center(50)
                    p = str(resultado1[num][2]).center(10)
                    law = [m,l,p]
                    listaNomes.append(law)
                    num += 1

                return listaNomes
            
            case 'BuscaNome':
                num = 0
                comandoSelect2 = f'SELECT * FROM usuarios WHERE nome  LIKE "%{nome}%"'
                cursor.execute(comandoSelect2)
                resultado2 = cursor.fetchall() # ler o banco de dados
                a = 0
                for c in resultado2:
                    law = [c[a], c[a+1], c[a+2]]
                listaNomes.append(law)
                return listaNomes
            case 'ALL':
                comandoSelect2 = f'SELECT * FROM usuarios'
                cursor.execute(comandoSelect2)
                resultado2 = cursor.fetchall() # ler o banco de dados
                num = 0
                for c in resultado2:
                    m = str(resultado2[num][0]).center(10)
                    l = resultado2[num][1].center(50)
                    p = str(resultado2[num][2]).center(10)
                    law = [m,l,p]
                    listaNomes.append(law)
                    num += 1
                return listaNomes


            case 'Cadastrar':
                comandoInsert = f'INSERT INTO usuarios (id, nome, idade) VALUES ({id},"{nome}", {idade})'
                cursor.execute(comandoInsert)
                conexao.commit() # edita o banco de dados
            case 'Excluir':
                comandoDelete  = f'DELETE FROM usuarios WHERE id = {id}'
                cursor.execute(comandoDelete)
                conexao.commit() # edita o banco de dados
            case 'Editar':
                comandoEdita  = f'UPDATE usuarios SET nome = "{nome}", idade={idade} WHERE id = {id}'
                cursor.execute(comandoEdita)
                conexao.commit() # edita o banco de dados             
    except:
        erro = 'Usuário não encontrado'
        return erro
    cursor.close()
    conexao.close()



