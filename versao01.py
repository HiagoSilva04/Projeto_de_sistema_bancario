print('---BEM-VINDO AO BANCO---')
print('-------Revolution-------')

dados = list()
dicionario = dict()

dicionario['usuario'] = 'Hiago'
dicionario['senha'] = 12345
dicionario['saldo_inicial'] = 3800

cont = 0 
linha = '-=' * 20

print()

nome = input('Qual o seu nome?: ').strip().capitalize()

if nome == dicionario['usuario']:
    print(f'O nome {nome} está correto!')

while nome != dicionario['usuario']:
    
    nome = input('Tente novamente...qual o seu nome?: ').strip().capitalize()

    if nome == dicionario['usuario']:
        print(f'O nome {nome} está correto!')



print(linha)

if nome == dicionario['usuario']:

    senha = int(input('Qual a sua senha?: '))

    if senha == dicionario['senha']:
        print(f'A senha {senha} está correta!')

    else:
        while True:

            if cont <= 2:
                senha = int(input('Tente novamente...qual a sua senha?: '))
                if senha == dicionario['senha']:
                    print(f'A senha {senha} está correta!')
                    break
            else:
                print('Número de tentativas permitidas alcançado... Tente novamente mais tarde!')
                break

            cont += 1

print()

if senha == dicionario['senha']:
    print(linha)
    print(f'{'Bem vindo (a) a sua conta do banco':>20}')
    print(linha)

    print()

    sair = ''
    sacar_mais = ''
    valor_deposito = 0
    depositar_mais = ''
    total_conta = dicionario['saldo_inicial']
    ver_novamente = ''

    while sair != 'S':

        print()
        print(linha)
        print('O que você deseja fazer?\n'
            '[1] Saque\n'
            '[2] Depositar\n'
            '[3] Extrato da conta')
        print(linha)

        print()
        escolha = int(input('Digite aqui sua escolha: '))
     

        if escolha > 3 or escolha < 0:
            while escolha > 3 or escolha < 0:
                print('Opção inválida... Digite um número de 1 a 3: ')
                escolha = int(input('Digite sua escolha aqui: '))

        print()

        if escolha == 1:
            sacar_mais = 'S'
            while sacar_mais != 'N':

                saque = int(input('Quanto você deseja sacar?: '))

                if saque > total_conta:
                    while saque > total_conta:

                        print('Saldo indisponivel....')
                        saque = int(input('Tente novamente ... Valor superior a saldo em conta!: '))


                        if saque <= total_conta:
                            break

                elif saque <= 0:
                    while saque <= 0:
                        print('Valor inexistente...')
                        saque = int(input('Tente novamente... Valor menor que zero!: '))

                        if saque > 0:
                            break
    
                total_conta -= saque

                sacar_mais = input('Deseja sacar novamente?[S/N]: ').upper()

        print()

        if escolha == 2:
            depositar_mais = 'S'
            while depositar_mais != 'N':

                depositar = int(input('Qual o valor do déposito?: '))

                if depositar <= 0:
                    while depositar <= 0:
                        print('Tente novamente... valor inválido!')
                        depositar = int(input('Digite o valor do déposito novamente: '))

                        if depositar > 0:
                            break

                total_conta += depositar

                depositar_mais = input('Deseja depositar novamente?[S/N]: ').upper()

        print()

        if escolha == 3:
            ver_novamente = 'S'
            while ver_novamente != 'N':

                print('<<EXTRATO>>')
                print(f'Valor total em conta: {total_conta:.2f}')
                print()

                ver_novamente = input('Deseja consultar o extrato novamente?[S/N]: ').upper()


        sair = input('Deseja Sair?[S/N]: ').upper()
