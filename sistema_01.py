#Criar um programa que rode o valor de um trasporte de classe economica, normal e alta:

from time import sleep
viagem = ''

def espaço():
    print()

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

def agradecimento():
    espaço()
    print('carregando resultado...')
    sleep(3)
    print('Compra bem sucedida')
    print('Obrigada pela preferencia!')
    print('Temos outras opções de passagens para você! Da classe ecônomica à alta.')



print('Viagens interestaduais com o menor preço e maior conforto?')
espaço()
print('NÃO PERCA TEMPO E GARANJA JÁ A SUA!')
espaço()
print('*********** MAS CORRA QUE É POR TEMPO LIMITADO ***********')
print('Promoção imperdível para você!')
print('Deseja consultar a Promoção? ')
espaço()
print('Digite (sim) ou (não)*')

pergunta = str(input('- ')).upper()

if pergunta == 'NAO' or pergunta == 'NÃO':
    print('Ok, temos outras opções de viagens para você.')

elif pergunta == '':
    print('Confira outras viagens semelhantes')

elif pergunta == 'SIM':
    espaço()
    print('                      ----SUPER PROMOÇÃO DE CARNAVAL----      ')
    espaço()
    
    print('OPÇÃO 1 :')

    print('Na compra de uma viagem com saída do (RS) para (SP) você ganha 15% de desconco na classe (normal).')

    espaço()

    print('OPÇÃO 2 :')

    print('Na compra de uma viagem com saída de (SP) para (SC) você ganha 10% de desconto na classe (alta).')

    espaço()

    print('Digite o número da opção escolhida. 1 ou 2:')
    opçao = int(input('- '))

    if opçao == 1:

        valor = 679.56

        novo = valor - (valor * 15 / 100)

        print('O valor da viagem fora da Promoção é {:.2f}.'.format(valor))

        print('Com o desconto de 15% você pagará apenas {:.2f}'.format(novo))

        espaço()

        compra = str(input('Deseja fazer essa compra?[SIM/NAO] ')).upper()

        if compra == 'SIM':
            agradecimento()
        
        elif compra == 'NAO' or compra == 'NÃO':
            print('Temos outras opções de passagens para você! Da classe ecônomica à alta.')

    elif opçao == 2:

        valor = 787.78

        novo = valor - (valor * 10 / 100)

        print('O valor da viagem fora da Promoção é {:.2f}.'.format(valor))

        print('Com o desconto de 15% você pagará apenas {:.2f}'.format(novo))

        compra = str(input('Deseja fazer essa compra? ')).upper()

        if compra == 'SIM':
            agradecimento()

        elif compra == 'NAO' or compra == 'NÃO':
            print('Temos  outras opções de passagens para você! Da classe ecônomica à alta.')
    else:
        print('Opçao {} não é considerada oferta de carnaval.Confira abaixo as viagens fora da promoção.'.format(opçao))

espaço()

print('*VIAGENS*')

print('''-------------------------------------------------
                ORIGEM     X    DESTINO

(1)  São Paulo             X      Rio de Janeiro
(2)  Rio Grande do Sul     X      Santa Catarina
(3)  Bahia                 X      Minas Gerais
(4)  Ceará                 X      Tocantins
(5)  Rio de Janeiro        X      Paraná
------------------------------------------------- ''')

espaço()
print('*VALORES*')

print('_' * 98)

print('       VIAGENS                         ECONÔMICA              NORMAL               ALTA')

espaço()

print('São Paulo X Rio de Janeiro:            (1) R$ 497.68          (6) R$ 597.68       (11) R$ 697.68')
print('Rio Grande do Sul X Santa Catarina:    (2) R$ 389.99          (7) R$ 489.99       (12) R$ 589.99')
print('Bahia X Minas Gerais:                  (3) R$ 525.45          (8) R$ 625.45       (13) R$ 725.45')
print('Ceará X Tocantins:                     (4) R$ 634.15          (9) R$ 734.15       (14) R$ 834.15')
print('Rio de Janeiro X Paraná:               (5) R$ 575.67         (10) R$ 675.67       (15) R$ 775.67')

print('_' * 98)


eSP = 497.68
eRS = 389.99
eBH = 525.45
eCE = 634.15
eRJ = 575.67

nSP = 597.68
nRS = 489.99
nBH = 634.15
nCE = 734.15
nRJ = 675.67

aSP = 697.68
aRS = 589.99
aBH = 734.15
aCE = 834.15
aRJ = 775.67


viagem = int(input('Digite o número da viagem desejada: '))

if viagem > 15 or viagem == '':
    print('OPS...viagem não encontrada')

elif viagem == 1:
    espaço()
    print_escolha('São Paulo', 'Rio de Janeiro', 'ECONÔMICA', eSP)

elif viagem == 2:
    espaço()
    print_escolha('Rio Grande do Sul', 'Santa Catarina', 'ECONÔMICA')
    
elif viagem == 3:
    espaço()
    print_escolha('Bahia', 'Minas Gerais', 'ECONÔMICA', eBH)

elif viagem == 4:
    espaço()
    print_escolha('Ceará', 'Tocantins', 'ECONÔMICA', eCE)

elif viagem == 5:
    espaço()
    print_escolha('Rio de Janeiro', 'Paraná', 'ECONÔMICA', eRJ)

elif viagem == 6:
    espaço()
    print_escolha('São Paulo', 'Rio de Janeiro', 'NORMAL', nSP)
    
elif viagem == 7:
    espaço()
    print_escolha('Rio Grande do Sul', 'Santa Catarina', 'NORMAL', nRS)
    
elif viagem == 8:
    espaço()
    print_escolha('Bahia', 'Minas Gerais', 'NORMAL', nBH)

elif viagem == 9:
    espaço()
    print_escolha('Ceará', 'Tocantins', 'NORMAL', nCE)

elif viagem == 10:
    espaço()
    print_escolha('Rio de Janeiro', 'Paraná', 'NORMAL', nRJ)

elif viagem == 11:
    espaço()
    print_escolha('Rio de Janeiro', 'São Paulo', 'ALTA', aRJ)

elif viagem == 12:
    espaço()
    print_escolha('Rio Grande do Sul', 'Santa Catarina', 'ALTA', aRS)

elif viagem == 13:
    espaço()
    print_escolha('Bahia', 'Minas Gerais', 'ALTA', aBH) 

elif viagem == 14:
    espaço()
    print_escolha('Ceará', 'Tocantins', 'ALTA', aCE)

elif viagem == 15:
    espaço()
    print_escolha('Rio de Janeiro', 'Paraná', 'ALTA', aRJ)
    