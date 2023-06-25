
from time import sleep
#veiculo = {'montadora':'', 'modelo': '', 'ano': '', 'placa':''}
frota = []
limite = 2

def cadastro(chave_e = None):
    #print('Cadastrando carro')
    qtd_estoque = len(frota)

    if qtd_estoque < limite:
        veiculo = {
            'Placa': '',
            'Montadora': '',
            'Modelo': '',
            'Ano': 0,
            'Cor': '',
            'Proprietário': ''
        }



        print('Digite os campos abaixo para cadastrar um veículo: ')
        for chave in veiculo:
            veiculo[chave] = input(chave + ': ').strip().upper()

        if chave_e is None:
            frota.append(veiculo)
            sleep(1)
            print('Veiculo Cadastrado com Sucesso!')
        else:
            frota[chave_e] = veiculo
            sleep(1)
            print('Veículo atualizado com sucesso!')

    else:
        print(f'Não é possível cadastrar mais carros. Limite de {limite} carros atingido.')

    return

def pesquisa():
    #print(' pesquisando carro')
    if len(frota) > 0:
        veiculo = {
                'Placa': '',
                'Montadora': '',
                'Modelo': '',
                'Ano': 0,
                'Cor': '',
                'Proprietário': ''
            }

        carro_e = []

        termo_pesquisa = input('Digite o termo a ser pesquisado no estoque carros: ')


        for chave in veiculo:
            carro_e.extend([carro for carro in frota if termo_pesquisa.lower() in str(carro[chave]).lower()])

        if len(carro_e) > 0:
            print('Estoque de carros!')
            print('Nr'.center(3), end='')
            print('Placa'.center(14), end='')
            print('Montadora'.center(18), end='')
            print('Modelo'.center(12), end='')
            print('Ano'.center(8), end='')
            print('Cor'.center(12), end='')
            print('Proprietário'.center(22), end='')

            for posicao_e_veiculo in list(enumerate(carro_e, start=1)):

                posicao_encontrada = posicao_e_veiculo[0]
                veiculo_e = posicao_e_veiculo[1]
                print()
                print(str(posicao_encontrada).center(3), end='')
                print(str(veiculo_e['Placa']).center(14), end='')
                print(str(veiculo_e['Montadora']).center(18), end='')
                print(str(veiculo_e['Modelo']).center(12), end='')
                print(str(veiculo_e['Ano']).center(8), end='')
                print(str(veiculo_e['Cor']).center(12), end='')
                print(str(veiculo_e['Proprietário']).center(22))
        else:
            print(f'Nenhum veículo encontrado para o termo: {termo_pesquisa}')
    else:
        print('Não é possível pesquisar porque o estoque de carros está vazio.')


    return

def imprimir():
    #imprimindo carro
    if len(frota) > 0:
        print('Frota de Carros')
        print('Nr'.center(3), end='')
        print('Placa'.center(14), end='')
        print('Montadora'.center(18), end='')
        print('Modelo'.center(12), end='')
        print('Ano'.center(8), end='')
        print('Cor'.center(12), end='')
        print('Proprietário'.center(22))

        for posicao_veiculo in list(enumerate(frota, start=1)):
            #print(veiculo)

            posicao = posicao_veiculo[0]
            veiculo = posicao_veiculo[1]

            print(str(posicao).center(3), end='')
            print(str(veiculo['Placa']).center(14), end='')
            print(str(veiculo['Montadora']).center(18), end='')
            print(str(veiculo['Modelo']).center(12), end='')
            print(str(veiculo['Ano']).center(8), end='')
            print(str(veiculo['Cor']).center(12), end='')
            print(str(veiculo['Proprietário']).center(22))
    else:
        print('Estoque de carros vazio')
    return

def imprimir_o():

    if len(frota) > 0:
        print('Frota de Carros')
        print('Nr'.center(3), end='')
        print('Placa'.center(14), end='')
        print('Montadora'.center(18), end='')
        print('Modelo'.center(12), end='')
        print('Ano'.center(8), end='')
        print('Cor'.center(12), end='')
        print('Proprietário'.center(22))

        for posicao_veiculo in list(enumerate(sorted(frota, key=lambda item: item['Ano'], reverse=True), start=1)):


            posicao = posicao_veiculo[0]
            veiculo = posicao_veiculo[1]

            print(str(posicao).center(3), end='')
            print(str(veiculo['Placa']).center(14), end='')
            print(str(veiculo['Montadora']).center(18), end='')
            print(str(veiculo['Modelo']).center(12), end='')
            print(str(veiculo['Ano']).center(8), end='')
            print(str(veiculo['Cor']).center(12), end='')
            print(str(veiculo['Proprietário']).center(22))
    else:
        print('Estoque de carros vazio.')

    return

def remover():
    #print('removendo carro')
    if len(frota) > 0:

        placa_informada = input('Digite a placa do veículo a ser removido do estoque: ').strip().upper()
        carro_encontrado_placa = [carro for carro in frota if placa_informada == (carro['Placa'])]

        if len(carro_encontrado_placa) > 0:
            for carro_e in carro_encontrado_placa:
                frota.remove(carro_e)

            print(f'Foram removidos {len(carro_encontrado_placa)} veículos com a placa {placa_informada}')
        else:
            print(f'Não foram encontrados veículos com a placa {placa_informada}')

    else:
        print('Não é possível remover nenhum veículo porque o estoque de carros está vazio.')

    return

def atualizar():
    #print('atualizando carro')

    qtd_frota = len(frota)

    if qtd_frota > 0:

        imprimir()

        indice_informado = int(input('Digite o número do veículo a ser atualizado no estoque: '))

        if indice_informado > qtd_frota or indice_informado < 1:
            print('O número do veículo precisa ser maior que zero e existir no estoque.')
        else:
            cadastro(indice_informado-1)
    else:
        print('Não é possível atualizar nenhum veículo porque o estoque de carros está vazio.')

    return


def menu():
    print()
    print('Menu')
    print('1 - Cadastrar Veículo')
    print('2 - Pesquisar Veículo')
    print('3 - Imprimir Veículo Cadastrado')
    print('4 - Remover Veículo Cadastrado')
    print('5 - Atualizar Veículo')
    print('0 - Sair')
menu()
opcao = int(input('Digite sua Opção: '))
print()
while 0 <= opcao <= 5:
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        pesquisa()
    elif opcao == 3:
        imprimir()
    elif opcao == 4:
        remover()
    elif opcao == 5:
        atualizar()
    elif opcao == 0:
       print('programa encerrado')
       exit()

    menu()
    opcao = int(input('Digite sua Opção: '))
else:
    print('Opção Inválida, programa encerrado')






