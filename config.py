import os
import pandas as pd


def create_archive():
    '''
    Cria uma planilha no diretório atual nomeada seed.xlsx no qual será armazenada as sementes que o usuário deseja salvar.

    Utilizando métodos para descobrir o nome do diretório atual (os.path.diname(os.path.abspaht(__file__))).
    Depois concatenamos com o nome que desejamos dar ao arquivo. Logo após, o algoritmo verifica se esse arquivo
    já não existe dentro do diretório atual: Caso existe, ele exibi uma mensagem mostrando, caso não ele cria o arquivo
    a partir de um dicionário com as chaves Name, Seed e Step, transformando num DataFrame e depois numa planilha.

    Args:
        None
    
    Returns:
        None
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    destiny_dir = os.path.join(current_dir, 'seed.xlsx')

    if (os.path.exists(destiny_dir)):
        print('file seed.xlsx already exists in current directory\n\n')
        return

    tmp = {'Name': [], 'Seed': [], 'Step':[]}

    df = pd.DataFrame(tmp)
    df.to_excel(destiny_dir, index=False)

