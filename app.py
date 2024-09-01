# importações
import os
from funcoes import *

# algoritmo principal
if __name__ == "__main__":
    # declarações
    campos = ('nome', 'email')

    # entra no programa e executa em loop
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                novo_arquivo = input('Informe o nome do novo arquivo: ')
                print(criar_arquivo(campos, novo_arquivo))
                continue
            case '2':
                abrir_arquivo = input('Informe o nome do arquivo a ser aberto: ')
                try:
                    os.system('cls')
                    usuarios = ler_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for i in range(len(usuarios)):
                        print(f'Índice: {i}.')
                        for campo in usuarios[i]:
                            print(f'{campo.capitalize()}: {usuarios[i].get(campo)}.')
                        print(f'\n{'-'*30}\n')
                except Exception as e:
                    print(f'Não foi possível ler o arquivo. {e}.')
                finally:
                    continue
            case '3':
                try:
                    usuario = {}
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for campo in campos:
                        usuario[campo] = input(f'Informe o campo {campo.capitalize()}: ')
                    usuarios.append(usuario)
                    print(salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Arquivo inexistente. Escolha "Abrir e ler arquivo" antes. {e}.')
                finally:
                    continue
            case '4':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    indice = int(input('Informe o índice do usuário a alterar os dados: '))
                    for campo in usuarios[indice]:
                        print(f'Valor atual do campo {campo.capitalize()}: {usuarios[indice].get(campo)}.')
                        novo_dado = input(f'Informe o novo dado do campo {campo} ou aperte "Enter" caso deseje manter o mesmo valor: ')
                        if novo_dado != '':
                            usuarios[indice][campo] = novo_dado
                        else:
                            ...
                    print(salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível alterar os dados. {e}.')
                finally:
                    continue
            case '5':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    indice = int(input('Informe o índice do usuário que deseja deletar: '))
                    nome_deletado = usuarios[indice]['nome']
                    opcao = input(f'Confirme com "SIM" para deletar o usuário {nome_deletado}: ').upper()
                    if opcao == 'SIM':
                        del(usuarios[indice])
                        print(salvar_dados(usuarios, abrir_arquivo))
                        print(f'Usuário {nome_deletado} deletado com sucesso.')
                    else:
                        print(f'Usuário {nome_deletado} não foi deletado.')
                except Exception as e:
                    print(f'Não foi possível deletar usuário. {e}.')
                finally:
                    continue
            case '6':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida.')
                continue