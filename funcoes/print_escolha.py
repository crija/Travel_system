from time import sleep
from funcoes.espaco import espaço

def print_escolha(origem, destino, classe, valor):
    espaço()
    print('Sua passagem está sendo processada...')
    sleep(2)
    espaço()
    print(f'Origem: {origem}')
    print(f'Destino: {destino}')
    print(f'Classe: {classe}')
    print(f'Valor final: {valor}')
    espaço()
    print('OBRIGADA PELA PREFERERENCIA!')

