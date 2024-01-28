import os
import shutil

def organizar_arquivos(diretorio_origem, diretorio_destino):
    # Lista todos os arquivos no diretório de origem
    arquivos = [f for f in os.listdir(diretorio_origem) if os.path.isfile(os.path.join(diretorio_origem, f))]

    for arquivo in arquivos:
        # Obtém a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1].lower()

        # Cria o diretório correspondente se não existir
        novo_diretorio = os.path.join(diretorio_destino, extensao[1:])
        os.makedirs(novo_diretorio, exist_ok=True)

        # Move o arquivo para o novo diretório
        shutil.move(os.path.join(diretorio_origem, arquivo), os.path.join(novo_diretorio, arquivo))
        print(f"Arquivo {arquivo} movido para {novo_diretorio}")

# Diretório de origem (onde os arquivos estão inicialmente)
diretorio_origem = '/caminho/do/diretorio/origem'

# Diretório de destino (onde os arquivos serão organizados)
diretorio_destino = '/caminho/do/diretorio/destino'

# Chama a função para organizar os arquivos
organizar_arquivos(diretorio_origem, diretorio_destino)
