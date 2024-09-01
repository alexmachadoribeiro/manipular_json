# importação da biblioteca json
import json

# função exibir menu
def exibir_menu():
    print("1 - Criar novo arquivo.")
    print("2 - Abrir e ler arquivo.")
    print("3 - Salvar novo usuário.")
    print("4 - Alterar dados.")
    print("5 - Deletar usuário.")
    print("6 - Sair do programa.")

# função criar arquivo
def criar_arquivo(campos, nome_arquivo):
    try:
        # lista de dicionários com objeto python
        usuarios = [
            {
                campos[0]: 'Admin',
                campos[1]: 'admin@gmail.com'
            }
        ]

        # serializando objeto python em json
        json_dados = json.dumps(usuarios)
        with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo:
            arquivo.write(json_dados)
        return f'{nome_arquivo}.json criado com sucesso.'
    except Exception as e:
        return f'Não foi possível criar o arquivo. {e}.'

# função ler arquivo
def ler_arquivo(nome_arquivo):
    # desserializando objeto json em objeto python
    with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

# função salvar novos dados
def salvar_dados(usuarios, nome_arquivo):
    try:
        with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo:
            json.dump(usuarios, arquivo)
        return 'Dados salvos com sucesso.'
    except Exception as e:
        return f'Não foi possível salvar os dados. {e}.'