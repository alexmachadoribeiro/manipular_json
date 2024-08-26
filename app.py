import json
import os

def exibir_menu():
    print("1 - Criar novo arquivo.")
    print("2 - Ler arquivo.")
    print("3 - Salvar novo usuário.")
    print("4 - Alterar dados.")
    print("5 - Deletar usuário.")
    print("6 - Sair do programa.")

def criar_arquivo(campos, nome_arquivo):
    try:
        usuario = {
            campos[0]: 'Admin',
            campos[1]: 'admin@gmail.com'
        }

        json_dados = json.dumps(usuario)

        with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo:
            arquivo.write(json_dados)

        return f'{nome_arquivo}.json criado com sucesso.'
    except:
        return 'Não foi possível criar o arquivo.'

def ler_arquivo(nome_arquivo):
    with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

if __name__ == "__main__":
    campos = ('Nome', 'E-mail')
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                nome_arquivo = input('Informe o nome do novo arquivo: ')
                print(criar_arquivo(campos, nome_arquivo))
                continue
            case '2':
                nome_arquivo = input('Informe o nome do arquivo a ser aberto: ')
                try:
                    usuarios = ler_arquivo(nome_arquivo)
                    print(ler_arquivo(nome_arquivo))
                    # FIXME
                    # for usuario in usuarios:
                    #     for campo in campos:
                    #         print(f'{campo}: {usuario[campo]}.')
                    #     print(f'\n{'-'*30}\n')
                except:
                    print('Não foi possível ler o arquivo.')
            case '3':
                # TODO
                ...
            case '4':
                # TODO
                ...
            case '5':
                # TODO
                ...
            case '6':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida.')
                continue