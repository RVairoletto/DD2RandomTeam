import personagem
import json


# Função para criar e retornar uma instância de Personagem
def criar_personagem(nome, funcao, caminhos):
    return personagem.Personagem(nome, funcao, caminhos=[i.strip().capitalize() for i in caminhos.split(',')])


# Caso o arquivo já exista, ele vai ser carregado no dicionário
try:
    with open('personagens.json', 'r') as file:
        personagens = json.load(file)
except OSError as e:
    print(f'Não foi possível ler o arquivo\n{e}')


while True:
    novo_personagem = criar_personagem(
        nome=str.capitalize(input('Digite o nome do personagem: ')),
        funcao=str.capitalize(input('Digite a função do personagem: ')),
        caminhos=str.capitalize(input('Digite os caminhos do personagem, separados por vírgula: '))
    )

    personagens.update({
        novo_personagem.funcao: {
            'nome': novo_personagem.nome,
            'caminhos': list(novo_personagem.caminhos)
        }
    })

    if str.upper(input('Deseja inserir mais um personagem? ([S]/N): ')) == 'N':
        break

with open("personagens.json", "w") as file:
    json.dump(personagens, file)

with open('personagens.json', 'r') as file:
    json_obj = json.load(file)

print(json_obj)
