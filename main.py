'''
Nome: Tallysson Yuri Campelo Fidelis
R.A. 22.222.005-5
Equipe: 33
Este é o projeto semestral desenvolvido para a disciplina "Fundamentos de  Algoritmos" sob a monitoria dos docentes: Prof.º Charles Porto Ferreira e Prof.ª Gabriela Biondi
O objetivo é desenvolver um sistema bancário completo e este deve ser realizado todo em Python'''

# Começo o meu código definindo todas as funções, listas e imports que serão utilizados ao decorrer do programa

# A lista clientes receberá os dados de todos os clientes
global clientes
clientes = []

# Defini essa lista de clientes antes de armazenar as informações em arquivos para realizar os testes, deixarei registrado no código pois são informações utilizadas na demonstração do programa em PDF

'''clientes = [
    {'Nome': 'Joao',
     'CPF': '123',
     'Conta': 'Comum',
     'Saldo': 500,
     'Senha': 'abc'
     },
    {'Nome': 'Maria',
     'CPF': '456',
     'Conta': 'Plus',
     'Saldo': 700,
     'Senha': 'abc'
     },
    {'Nome': 'Jose',
     'CPF': '789',
     'Conta': 'Plus',
     'Saldo': 100,
     'Senha': 'abc'
     }
]'''


# A lista extrato receberá as informações de horários das operações e dos dados momentaneos 
global extratos
extratos = []

# A função 'recebe_extratos' será responsável por configurar a formatação e adicionar as ações dos clientes em uma lista
def recebe_extratos(nome, cpf, conta, data, valor, tarifa, saldo, sinal):

    # A variável 'verificador_extrato' inicia-se com valor 0, ela será utilizada para buscar se o cliente já tem registros em seu extrato
    verificador_extrato = 0

    # Cliente será a variável que representa o dicionário que contém os registros dos clientes na lista extratos
    for cliente in extratos:
        # Caso o cpf do cliente já esteja incluído em algum dicionário, será adicionado á chave 'Extrato' uma outra lista com os dados dessa operação
        
        # Se o CPF digitado estiver dentro de uma chave 'CPF' de algum cliente, significa que ele já tem registros e já existe uma chave para armazenar os extratos
        if cpf == cliente['CPF']:

            # Caso a variável receba 1, siginifica que o ciente já existe na lista extratos e será adicinado os novos valores a chave 'Extrato' do mesmo
            verificador_extrato = 1
            cliente['Extrato'].append(f'Data: {data}  {sinal} R$ {valor:.2f}  Tarifa: R$ {tarifa:.2f}  Saldo: R$ {saldo:.2f}')
            break

    # Se o verificador continua com 0. o cliente ainda não possui uma chave 'Extrato', será criada um dicionario 'histórico' que armazenará as informações
    if verificador_extrato == 0:
        historico = {
                'Nome' : nome,
                'CPF' : cpf,
                'Conta' : conta,
                'Extrato' : [f'Data: {data}  {sinal} R$ {valor:.2f}  Tarifa: R$ {tarifa:.2f}  Saldo: R$ {saldo:.2f}']
            }
        extratos.append(historico)
        
        
# A  função 'literal_eval' busca as informações em string e as transforma nas variáveis correspondentes
from ast import literal_eval

# A função 'leitura' tem como obejtivo ler as informações dos arquivos e colocar nas listas
def leitura():
    arquivo_clientes = open('cliente.txt', 'r')
    arquivo_extratos = open('extrato.txt', 'r')
    
    # A listas 'clientes' e 'extratos' são definidas globalmente para serem utilizadas em demais funções
    global clientes 
    global extratos
    
    clientes = []
    extratos = []
    
    # Os laços de repetição realizam a leitura de cada linha dos arquivo e adicionas nas listas globais
    for x in arquivo_clientes:
        clientes.append(literal_eval(x))
    
    for y in arquivo_extratos:
        extratos.append(literal_eval(y))
        
    arquivo_clientes.close()
    arquivo_extratos.close()
    
# A função 'escrita' tem como obejtivo ler as informações das listas e colocar nos arquivos
def escrita():
    arquivo_clientes = open('cliente.txt', 'w')
    arquivo_extratos = open('extrato.txt', 'w')
    
    # Os laços de repetição realizam a leitura de cada informação na lista e adicionaria em cada linha do arquivo
    for x in clientes:
        arquivo_clientes.write('{}\n'.format(x))
        
    for y in extratos:
        arquivo_extratos.write('{}\n'.format(y))
        
    arquivo_clientes.close()
    arquivo_extratos.close()        
    

# Importo a biblioteca responsável para buscar a data e hora que o usuário está utilizando o sistema
from datetime import datetime

data = datetime.now()
data = data.strftime('%d/%m/%Y %H:%M:%S')
print(data)
print()

# Inicio as minhas linhas de código designinando todas as funções que serão utilizadas no sistema, elas serão utilizadas quando o usuário selecionar as opções correspondentes as funções

# A função "novo_cliente" será utilizada para adicionar um cliente ao banco de dados ao banco, abaixo será solicitado ao usuário alguns dados para que esse cadastro seja feito
def novo_cliente ():
    print("NOVO CLIENTE")
    
    # O cadastro inicia-se como 'incompleto', e enquanto ele ter esse valor, seá pedidos dados ao usuário
    cadastro = 'incompleto'

    while cadastro == 'incompleto':
    
        print("Insira a seguir os dados do novo cliente\n")

        nome = input("Nome: ")
        print()

        cpf = input("CPF: ")
        print()
        
        # 'Dados' representa os dicionários com as informações dos clientes, caso o valor digitado estiver dentro de alguma chave 'CPF' de algum cliente, o cadastro desse CPF já está completo
        for dados in clientes:
            if cpf == dados['CPF']:
                print('CPF já cadastrado!\n')
                cadastro = 'completo'
                break
        # Se o cadastro está completo, termina o loop que adiciona dados
        if cadastro == 'completo':
            break

        # Neste momento, o cadastro ainda está 'incompleto' então o programa continuará com suas funções
        tipo_de_conta = input("Tipo de conta (Comum | Plus) : ")
        print()
        
        # Transformo o que o cliente digitar com a primeira inicial maiuscula e as demais minusculas, para que não correr o risco do usuario digitar a palavra correta porém não com a formatação certa. Ex.: comum, COMUM, cOmUM ...
        tipo_de_conta = tipo_de_conta.capitalize()

        # Existem apenas 2 tipos de conta possíveis, caso o usuário digitar uma opção inválida, o cadastro de cliente reiniciará, caso não, o programa seguirá em frente
        if tipo_de_conta == 'Comum' or tipo_de_conta == 'Plus':

            saldo = float(input("Valor inicial da conta: R$ "))
            print()
            senha = input("Digite sua senha: ")
            print()

            # Peço a confirmação dos dados digitados pelo usuário, se possuir algum erro, o usuário terá opção de refazer o cadastro
            confirma = input("Os dados digitados estão corretos? Aperte 0 para prosseguir ou qualquer outra tecla para retornar: ")
            print()

            # Se o cliente confirmou os dados inseridos com a tecla 0, exibirá na tela todos os dados cadastrados e uma mensagem de confirmação
            if confirma == '0':
                print("Novo cliente cadastrado!\n")
                print("Nome: ", nome)
                print("CPF: ", cpf)
                print("Conta: ", tipo_de_conta)
                print("Saldo: R$ %.2f" % saldo)
                print("Senha: ", senha)
                print()

                # A partir daqui, crio um dicionario onde os dados do cliente serão adicionados e após isso, os adiciono na lista global de clientes
                dados = {
                    'Nome': nome,
                    'CPF': cpf,
                    'Conta': tipo_de_conta,
                    'Saldo': saldo,
                    'Senha': senha
                }
                clientes.append(dados)
                cadastro = 'completo'

        # Este else é correspondente ao tipo de conta, caso o usuário não digitar uma opção válida, será informado na tela e ele poderá reescrever
        else:
            print('\nPor favor, selecione um tipo de conta válido!\n')  


# A função 'apaga_cliente' tem como objetivo remover clientes já cadastrados
def apaga_cliente ():
    print('APAGA CLIENTE\n')

    # Caso o tamanho da lista que armazena clientes for menor que 1, não há clientes cadastrados e isso é informado ao usuário, caso for maior que 1, a função irá prosseguir
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    else:
        cpf = input("Digite o CPF do cliente que será excluído: ")
        print()
        # Dados são os dicionarios que armazenam as informações do clientes dentro da lista. O laço de reptição irá iterar sobre toda lista e buscar se existe o cpf informado pelo usuario.
        for dados in clientes:
            if cpf == dados['CPF']:
                # A variável 'nome' receberá o valor que está dentro da chave 'Nome' no dicionário
                nome = dados['Nome']

                # Se estiver, com a função remove(), irá exluir o dicionario que contem os dados do cliente que possui o CPF informado
                clientes.remove(dados)

                print("Cliente %s, com CPF %s excuiído!\n" % (nome,cpf))
                break
        # Se o CPF não existir na lista de clientes, será informado ao usuário
        else:
                print("CPF %s não encontrado\n" % cpf)
                

# A função 'listar_clientes' irá apresentar ao usuário todos os clientes já cadastrados       
def listar_clientes ():
    print("CLIENTES CADASTRADOS\n")

    # Caso o tamanho da lista que armazena clientes for menor que 1, não há clientes cadastrados e isso é informado ao usuário, caso for maior que 1, a função irá prosseguir
    if len(clientes) < 1:
        print("Não há nenhum cliente cadastrado\n\n")
    else:
        # 'x' irá assumir todos os dicionarios dentro da lista clientes e irá apresentar na tela com o valor das chaves que estão descritas abaixo
        for x in clientes:
            print('Nome: ', x['Nome'])
            print('CPF: ', x['CPF'])
            print('Conta: ', x['Conta'])
            print('Saldo: R$ %.2f' % x['Saldo'])
            print('Senha: ', x['Senha'])
            print()

# A função 'debito' tem como objetivo retirar um valor da conta de um cliente
def debito ():
    print('DEBITO\n')

    # Caso a lista de clientes for menor que 1, significa que não há nenhum cliente cadastrado e a função irá parar
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    # Caso contrário, a função seguirá normalmente solicitando os dados
    else:
        cpf = input("Digite o CPF do cliente: ")
        senha = input("Digite a senha: ")
        valor = float(input("Digite o valor do débito: R$ "))
        print()
        
        # Dados será o dicionário onde as informações dos clientes estão armazenadas, e a condição irá verificar se o CPF e senha estão corretos, caso contrário, não será possível realizar o débito
        for dados in clientes:
            if cpf == dados['CPF'] and senha == dados['Senha']:
                # A variável saldo passa a receber o valor da chave 'Saldo' do dicionario que as informações do cliente estão
                saldo = dados['Saldo']
                # A variável conta recebe o valor da chave 'Conta' para verificar o tipo que o usuário possuí
                conta = dados['Conta']

                # Caso o tipo de conta do cliente for 'Plus', a taxa de cada débito corresponde a 3% do valor, assim a variável valor recebe o próprio valor com este adicional antes de ser debitado do saldo
                if conta == 'Plus':
                    # A variável 'valor_tarifado' recebe o valor o valor com a tarifa inclusa
                    valor_tarifado = valor * 1.03
                    # A variável 'tarifa' recebe o valor que foi cobrado do débito
                    tarifa = valor * 0.03
                    # E desse saldo será debitado o valor digitado do usuário
                    saldo -= valor_tarifado
                    # A conta Plus permite um saldo negativo de até R$ 5.000,00, então se essa condição estiver dentro dos conformes, o processo de débito seguirá normalmente
                    if saldo >= -5000:
                        # Agora a chave 'Saldo' passará a recebr o novo valor do saldo atualizado pós débito
                        dados['Saldo'] = saldo
                        print('Débito realizado!\nSaldo atual: R$ %.2f\n' % saldo)
                        
                        # A partir daqui o código referente ao armazenamento dos valores na lista 'extratos'
                        
                        # Para adicionar a operação na lista de extratos, busco o valor da chave 'Nome' no dicionario que contém os dados do cliente
                        nome = dados['Nome']
                        # Com a função 'datetime.now()', atribuo a variável nome a data e hora do sistema operacional
                        data = datetime.now()
                        # Com a função 'strftime()', consigo alterar a formatação de data e hora e faço a mesma variável receber o valor na formatação desejada
                        data = data.strftime('%d/%m/%Y %H:%M:%S')
                        
                        # A função 'recebe_extratos' será utilizada para armezenar os dados que serão utilizadas no extrato
                        recebe_extratos(nome, cpf, conta, data, valor, tarifa, saldo, '-')
                        break
                    
                    # Se o saldo ultrapassar o limite negativo, a operação de débito não é realizada!
                    else:
                        print('Operação cancelada!\nO saldo pós essa operação ultrapassa o limite negativo de R$ 5000,00\n')
                        break

                # Caso não for 'Plus', só resta a opção 'Comum' onde é cobrado um débito de 5% do valor
                else:
                    # A variável 'valor_tarifado' recebe o valor o valor com a tarifa inclusa
                    valor_tarifado = valor * 1.05
                    # A variável tarifa recebe o valor que foi cobrado do débito
                    tarifa = valor * 0.05
                    # E desse saldo será debitado o valor digitado do usuário
                    saldo -= valor_tarifado
                    # A conta comum permite um saldo negatvo de apenas R$ 1.000,00, a operação só prossegue se estiver dentro dos conformes
                    if saldo >= -1000:
                        # Agora a chave 'Saldo' passará a recebr o novo valor do saldo atualizado pós débito
                        dados['Saldo'] = saldo
                        print('Débito realizado!\nSaldo atual: R$ %.2f\n' % saldo)
                        
                        # A partir daqui o código referente ao armazenamento dos valores na lista 'extratos'

                        # Para adicionar a operação na lista de extratos, busco o valor da chave 'Nome' no dicionario que contém os dados do cliente
                        nome = dados['Nome']
                        # Com a função 'datetime.now()', atribuo a variável nome a data e hora do sistema operacional
                        data = datetime.now()
                        # Com a função 'strftime()', consigo alterar a formatação de data e hora e faço a mesma variável receber o valor na formatação desejada
                        data = data.strftime('%d/%m/%Y %H:%M:%S')

                        # A função 'recebe_extratos' será utilizada para armezenar os dados que serão utilizadas no extrato
                        recebe_extratos(nome, cpf, conta, data, valor, tarifa, saldo, '-')
                        break

                    # Se o saldo ultrapassar o limite negativo, a operação de débito não é realizada!
                    else:
                        print('Operação cancelada!\nO saldo pós essa operação ultrapassa o limite negativo de R$ 1000,00\n')
                        break

        # Este else é referente caso o CPF e/ou Senha não perteçam a nenhum cliente
        else:   
            print("CPF ou senha inválidos!\n")
        
# A função 'deposito' tem como objetivo acrescentar um valor na conta do cliente
def deposito ():
    print('DEPÓSITO\n')
    
    # Caso a lista de clientes for menor que 1, significa que não há nenhum cliente cadastrado e a função irá parar
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    # Caso contrário, a função seguirá normalmente solicitando os dados
    else:
        cpf = input("Digite o CPF do cliente: ")
        valor = float(input("Digite o valor do depósito: R$ "))
        print()

        # Dados será o dicionário onde as informações dos clientes estão armazenadas, e a condição irá verificar se o CPF e está correto, caso contrário, não será possível realizar o depósito
        for dados in clientes:
            if cpf == dados['CPF']:
                # A váriavel saldo passa a receber o valor da chave 'Saldo' do dicionario que as informações do cliente estão
                saldo = dados['Saldo']
                # E desse saldo será depositado o valor digitado do usuário
                saldo += valor
                # Agora a chave 'Saldo' passará a recebr o novo valor do saldo atualizado pós depositado
                dados['Saldo'] = saldo
                print('Depósito realizado!\nSaldo atual: R$ %.2f\n' % saldo)
                
                # A partir daqui o código referente ao armazenamento dos valores na lista 'extratos'

                # Para adicionar a operação na lista de extratos, busco o valor da chave 'Nome' e da chave 'Conta' no dicionario que contém os dados do cliente
                nome = dados['Nome']
                conta = dados['Conta']
                # Neste caso, a variável 'tarifa' recebe o valor zero pois não há cobrança em cima de depósito
                tarifa = 0

                # Com a função 'datetime.now()', atribuo a variável nome a data e hora do sistema operacional
                data = datetime.now()
                # Com a função 'strftime()', consigo alterar a formatação de data e hora e faço a mesma variável receber o valor na formatação desejada
                data = data.strftime('%d/%m/%Y %H:%M:%S')
                
                # A função 'recebe_extratos' será utilizada para armezenar os dados que serão utilizadas no extrato
                recebe_extratos(nome, cpf, conta, data, valor, tarifa, saldo, '+')
                break

        # Caso não for encontrado nenhum CPF, será informado ao usuário
        else:
            print("CPF inválido!\n")

# A função 'extrato' tem como objetivo demonstrar ao usuário os registros de todas as operações do cliente
def extrato():
    print('EXTRATO\n')

    # Caso a lista de clientes for menor que 1, significa que não há nenhum cliente cadastrado e a função irá parar
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    # Caso contrário, a função seguirá normalmente solicitando os dados
    else:
        cpf = input('Digite o CPF: ')
        senha = input('Digite a senha: ')
        print()

        # A variável 'extrato_encontrato' será utilizada para definir se existe ou não registros do cliente
        extrato_encontrado = 0

        # A variável 'cliente_encontrado' será utilizada para definir se o CPF e senha do cliente se encontra na lista
        cliente_encontrado = 0

        # Este laço de repetição irá percorrer durante a lista de clientes, buscando se há um cliente com CPF e Senha digitados
        for dados in clientes:
            if cpf == dados['CPF'] and senha == dados['Senha']:
                # Se encontrado, a variável receberá 1 e significa que há um cliente com CPF e senha digitados
                cliente_encontrado = 1
                for registros in extratos:
                    if cpf == registros['CPF']:
                        # Se encontrado, a variável receberá 1 e signigica que há registros desse cliente na lista extratos
                        extrato_encontrado = 1
                        print()
                        print('Nome: %s' % registros['Nome'])
                        print('CPF: %s' % registros['CPF'])
                        print('Conta: %s' % registros['Conta'])
                        for operacoes in registros['Extrato']:
                            print(operacoes)
                        print()
                        break
                else:
                    extrato_encontrado = 0
            else:
                extrato_encontrado = 1


        # Se a variável 'cliente_encontrado' continua recebendo 0, significa que não foi encontrado um dicionario com os dados dos clientes na lista que correspondem o CPF e senha digitados
        if cliente_encontrado == 0:
            print('CPF ou senha inválidos!\n')

        

        # Se a variável 'extrato_encontrado' continua recebendo 0, significa que não há registros nesse CPF
        if extrato_encontrado == 0:
            print('Não há registros nesse CPF\n')
                    
# A função 'transferencia' tem como objetivo transferir um valor de uma conta para outra conta, desde que amabas estejam cadastradas no banco
def transferencia():
    print('TRANSFERÊNCIA ENTRE CONTAS\n')
    
    # Caso a lista de clientes for menor que 1, significa que não há nenhum cliente cadastrado e a função irá parar
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    # Caso contrário, a função seguirá normalmente solicitando os dados
    else:
        cpfOrigem = input('Digite o CPF da origem da transfêrencia: ')
        senhaOrigem = input('Digite a senha da conta de origem: ')
        cpfDestino = input('Digite o CPF de destino: ')
        valor = float(input('Digite o valor da transfêrencia: R$ '))
        print()
        
        # Este laço for irá verificar se as informações do cliente de origem contém no banco, caso contrário será informado ao usuário
        for dados in clientes:
            # Este laço for irá verificar se as informações do cliente de destino contém no banco, caso contrário será informado ao usuário
            if cpfOrigem == dados['CPF'] and senhaOrigem == dados['Senha']:
                # A variável conta irá receber o tipo de conta do cliente de origem, pois os limites de saldo negativo são diferentes
                conta = dados['Conta']
                for dados1 in clientes:
                    if cpfDestino in dados1.values():
                        # As variáveis 'saldoOrigem' e 'saldoDestino' armazenam os valores de saldo dos clientes e pós isso elas debitam e creditam respectivamente o valor informado
                        saldoOrigem = dados['Saldo']
                        saldoDestino = dados1['Saldo']
                        saldoOrigem -= valor
                        # Caso a conta for Plus, pode alcançar um saldo negativo de até R$ 5000,00
                        if conta == 'Plus' and saldoOrigem >= -5000:
                            saldoDestino += valor
                            # Pós esse processo, o valor das váriaveis é novamente armazenado dentro da cahve correspondente no dicionário que contém os dados do cliente
                            dados['Saldo'] = saldoOrigem
                            dados1['Saldo'] = saldoDestino
                        
                            print('Transferência realizada!\n')
                        
                            print('Saldo atual na conta de origem: R$ %.2f\n' % saldoOrigem)
                            print('Saldo atual na conta de destino: R$ %.2f\n' % saldoDestino)
                            
                            # A partir daqui o código referente ao armazenamento dos valores na lista 'extratos'

                            # Com a função 'datetime.now()', atribuo a variável nome a data e hora do sistema operacional
                            data = datetime.now()
                            # Com a função 'strftime()', consigo alterar a formatação de data e hora e faço a mesma variável receber o valor na formatação desejada
                            data = data.strftime('%d/%m/%Y %H:%M:%S')
                            
                            # A variável 'nome_origem' vai receber o valor da chave 'Nome' do cliente que a transferência tem origem
                            nome_origem = dados['Nome']
                            # A variável 'nome_destino' vai receber o valor da chave 'Nome' do cliente que a transferência tem destino
                            nome_destino = dados1['Nome']
                            # A variável 'tarifa' recebe 0 pois não há nenhum tipo de cobrança nesta operação
                            tarifa = 0

                            # A função 'recebe_extratos' será utilizada para armezenar os dados que serão utilizadas no extrato do cliente de origem
                            recebe_extratos(nome_origem, cpfOrigem, conta, data, valor, tarifa, saldoOrigem, '-')
                            # Agora está função será utilizada para armezenar os dados que serão utilizadas no extrato do cliente de destino
                            recebe_extratos(nome_destino, cpfDestino, conta, data, valor, tarifa, saldoDestino, '+')
                            break
                        
                        # Caso contrário, operação não poderá ser realizada
                        elif conta == 'Plus' and saldoOrigem < -5000:
                            print('Operação cancelada!\nO saldo de origem ultrapassará o limite negativo de R$ 5000,00\n')
                            break
                        # Caso a conta for Comum, pode alcançar um saldo negativo de até R$ 1000,00
                        elif conta == 'Comum' and saldoOrigem >= -1000:
                            saldoDestino += valor
                            # Pós esse processo, o valor das váriaveis é novamente armazenado dentro da chave correspondente no dicionário que contém os dados do cliente
                            dados['Saldo'] = saldoOrigem
                            dados1['Saldo'] = saldoDestino
                        
                            print('Transferência realizada!\n')
                        
                            print('Saldo atual na conta de origem: R$ %.2f\n' % saldoOrigem)
                            print('Saldo atual na conta de destino: R$ %.2f\n' % saldoDestino)
                            
                            # A partir daqui o código referente ao armazenamento dos valores na lista 'extratos'

                            # Com a função 'datetime.now()', atribuo a variável nome a data e hora do sistema operacional
                            data = datetime.now()
                            # Com a função 'strftime()', consigo alterar a formatação de data e hora e faço a mesma variável receber o valor na formatação desejada
                            data = data.strftime('%d/%m/%Y %H:%M:%S')
                            
                            # A variável 'nome_origem' vai receber o valor da chave 'Nome' do cliente que a transferência tem origem
                            nome_origem = dados['Nome']
                            # A variável 'nome_destino' vai receber o valor da chave 'Nome' do cliente que a transferência tem destino
                            nome_destino = dados1['Nome']
                            # A variável 'tarifa' recebe 0 pois não há nenhum tipo de cobrança nesta operação
                            tarifa = 0

                            # A função 'recebe_extratos' será utilizada para armezenar os dados que serão utilizadas no extrato do cliente de origem
                            recebe_extratos(nome_origem, cpfOrigem, conta, data, valor, tarifa, saldoOrigem, '-')
                            # Agora está função será utilizada para armezenar os dados que serão utilizadas no extrato do cliente de destino
                            recebe_extratos(nome_destino, cpfDestino, conta, data, valor, tarifa, saldoDestino, '+')
                            break
                        # Caso contrário, operação não poderá ser realizada
                        else:
                            print('Operação cancelada!\nO saldo de origem ultrapassará o limite negativo de R$ 1000,00\n')
                            break
                else:
                    print('CPF de destino não encontrado!\n\n')   
                break     
        else:
            print('CPF ou senha inválidos!\n\n')


# A função 'randint' da biblioteca 'random' retorna um número aleatório inteiro dentro de um intervalo pré-definido, ela será utilizada dentro da função 'investimentos'
from random import randint

# A função 'investimentos' é uma opção que o usuário pode aplicar uma parte de seu dinheiro e uma compra de ação e essa ação retornar lucro ou prejuizo ao mesmo
def investimentos():
    print('INVESTIMENTOS\n')

    # Caso a lista de clientes for menor que 1, significa que não há nenhum cliente cadastrado e a função irá parar
    if len(clientes) < 1: 
        print("Não há nenhum cliente cadastrado\n\n")
    else:
        print('Bem vindo a seção de investimentos do Banco QuemPoupaTem!\n\nNesta área você pode comprar ações de empresas parceiras de risco alto, médio ou baixo\n')
        
        print('EMPRESA 1: Gabi Cosméticos\nRISCO: Baixo\nPERCENTUAL DE GANHO: 10 %\n')
        print('EMPRESA 2: Bebidas Charles\nRISCO: Médio\nPERCENTUAL DE GANHO: 25 %\n')
        print('EMPRESA 3: Casa de Shows FEI\nRISCO: Alto\nPERCENTUAL DE GANHO: 40 %\n')
        
        print('O valor investido em caso de lucro será multiplicado pelo percentual de ganho, já em caso de prejuízo, você perderá todo o valor investido! Escolha sabiamente.\n')

        print('Você deseja prosseguir?\n')
        x = input('Digite 0 para prosseguir ou qualquer outra tecla para desistir: ')
        print()

        if x == '0':
            cpf = input('Digite o CPF: ')
            senha = input('Digite a senha: ')
            empresa = input('Digite o número da empresa que você deseja investir o seu dinheiro: ')
            valor = float(input('Digite o valor a ser investido: R$ '))       

            # Dados será o dicionário onde as informações dos clientes estão armazenadas, e a condição irá verificar se o CPF e senha estão corretos, caso contrário, não será possível realizar o investimento
            for dados in clientes:
                if cpf == dados['CPF'] and senha == dados['Senha']:
                    # O investimento só poderá ser realizado caso o cliente tenha o valor suficiente em conta, caso contrário, não poderá prosseguir
                    if valor <= dados['Saldo']:
                        # A empresa '1' é uma empresa de baixo risco, esse risco assumirá um valor de 1 a 5, caso for 1, o que corresponde a 20% das chances, o cliente terá prejuizo, se não o cliente terá lucro!
                        if empresa == '1':
                            risco = randint(1,5)
                            if risco >= 2:
                                print('\nParabéns! O valor investido deu lucro\n')
                                invest = valor * 0.1
                                print('Você ganhou R$ %.2f !\n' % invest)                                
                                saldo = dados['Saldo']
                                saldo += invest
                                dados['Saldo'] = saldo
                                break
                            else:
                                print('\nQue pena, seu investimento será um prejuízo :(\n')
                                print('Você perdeu R$ %.2f !\n' % valor)
                                saldo = dados['Saldo']
                                saldo -= valor
                                dados['Saldo'] = saldo
                                break

                        # A empresa '2' é uma empresa de risco médio, esse risco assumirá um valor de 1 a 6, caso for 1, 2 ou 3, o que corresponde a 50% das chances, o cliente terá prejuízo, se não o cliente terá lucro!
                        elif empresa == '2':
                            risco = randint(1,6)
                            if risco >= 4:
                                print('\nParabéns! O valor investido deu lucro\n')
                                invest = valor * 0.25
                                print('Você ganhou R$ %.2f !\n' % invest)
                                saldo = dados['Saldo']
                                saldo += invest
                                dados['Saldo'] = saldo
                                break
                            else:
                                print('\nQue pena, seu investimento será um prejuízo :(\n')
                                print('Você perdeu R$ %.2f !\n' % valor)
                                saldo = dados['Saldo']
                                saldo -= valor
                                dados['Saldo'] = saldo
                                break

                        # A empresa '3' é uma empresa de risco alto, esse risco assumirá um valor de 1 a 4, caso for 1, 2, 3 ou 4, o que corresponde a 75% das chances, o cliente terá prejuizo, se não o cliente terá lucro!
                        elif empresa == '3':
                            risco = randint(1,4)
                            if risco == 4:
                                print('\nParabéns! O valor investido deu lucro\n')
                                invest = valor * 0.4
                                print('Você ganhou R$ %.2f !\n' % invest)
                                saldo = dados['Saldo']
                                saldo += invest
                                dados['Saldo'] = saldo
                                break
                            else:
                                print('\nQue pena, seu investimento será um prejuízo :(\n')
                                print('Você perdeu R$ %.2f !\n' % valor)
                                saldo = dados['Saldo']
                                saldo -= valor
                                dados['Saldo'] = saldo
                                break
                        else:
                            print('\nPor favor, escolha uma empresa válida\n')
                            break
                    else:
                        print('\nVocê não tem saldo suficiente para investir!\n')
                        break
            else:
                print('\nCPF ou senha inválidos!\n')
        else:
            print('Eu sei, o mundo dos investimentos não é para qualquer um, volte aqui quando estiver pronto.\n')
                            
# Aqui começa a exbição do programa ao usuário

# Exibe uma mensagem de boas vindas inicial e logo após, inicia-se um laço de repetição infinito, onde é explicado ao usuário como funciona o menu inicial e o que ele precisa digitar para prosseguir, assim que o usuário finaliza a ação, a mensagem do menu retornará até ele optar pela opção sair, que quebrará o laço infinito

# O programa tenta executar a função 'leitura' e caso nenhum arquivo exista, e ao invés do programa para com um erro, o código executará a função 'escrita' que cria os arquivos
try:
    leitura()
except:
    escrita()

print("Seja bem vindo ao Banco QuemPoupaTem!\n")

while True:
    print("Qual operação você deseja realizar?\n")

    print("1. Novo cliente")
    print("2. Apaga cliente")
    print("3. Listar clientes")
    print("4. Débito")
    print("5. Depósito")
    print("6. Extrato")
    print("7. Transferência entre contas")
    print("8. Investimentos")
    print("9. Sair")
    print()

    operacao = input("Digite o número correspondente a operação escolhida: ")
    print()

    if operacao == '1':
        leitura()
        novo_cliente()
        escrita()
    elif operacao == '2':
        leitura()
        apaga_cliente()
        escrita()
    elif operacao == '3':
        leitura()
        listar_clientes()
        escrita()
    elif operacao == '4':
        leitura()
        debito()
        escrita()
    elif operacao == '5':
        leitura()
        deposito()
        escrita()
    elif operacao == '6':
        leitura()
        extrato()
        escrita()
    elif operacao == '7':
        leitura()
        transferencia()
        escrita()
    elif operacao == '8':
        leitura()
        investimentos()
        escrita()
    elif operacao == '9':
        break
    else:
        print("Por favor, digite uma operação válida\n")
    
# Esta mensagem será exibida após o usuario optar por sair do laço de repetição e assim, finalizando as ações no programa
print("Obrigado por utilizar os serviços do Banco QuemPoupaTem!\n") 
