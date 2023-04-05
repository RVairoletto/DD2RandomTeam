import json


def criar_base_de_dados():
    while True:
        nome = input('Insira o nome do personagem: ')
        personagem = {nome, get_playstiles()}

        if str.upper(input('Deseja salvar outro personagem? ([S]/N): ')) == 'N':
            print(personagem)
            # with open('personagens.json', 'a') as file:
            #     json.dump(dict(personagem), file)
            break


def get_playstiles():
    estilos = list()

    while True:
        estilo = input('Insira um estilo de jogo deste personagem: ')

        if estilo != '':
            estilos.append(estilo)
        else:
            break

    return tuple(estilos)


criar_base_de_dados()
