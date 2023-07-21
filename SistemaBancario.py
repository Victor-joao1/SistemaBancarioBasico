menu = '''------------ \n
BANCO FICÇAO \n
------------ \n
[d] Depositar \n
[s] SACAR \n
[e] EXTRATO \n
[x] SAIR \n
------------
'''
valor_depositado = 0
saldo = 0
limite = 501
numero_saque = 0
LIMITE_SAQUE = 0
extrato = ""

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_depositado = float(
            input('Digite o valor que deseja depositar: '))
        saldo += valor_depositado
        extrato += f'Déposito: R$:{valor_depositado :.2f} \n'

    elif opcao == 's':
        if LIMITE_SAQUE != 3:
            valor_saque = float(input('Digite Quanto deseja sacar: '))
            if saldo > valor_saque:
                if valor_saque < limite:
                    saldo -= valor_saque
                    extrato += f'Saque: R$:{valor_saque :.2f} \n'
                    LIMITE_SAQUE += 1
                else:
                    print('Saque limitado no valor de R$:500.00 tente um valor menor.')
            else:
                print('Não a saldo suficiente para realizar está operação!')
        else:
            print('Você atingiu seu limite de saques por hoje, retorne amanhã!')

    elif opcao == 'e':
        print('-='*25)
        print('-----EXTRATO----')
        print('-='*25)
        if saldo == 0:
            print('Não foram realizadas movimentações!')
        else:
            print(extrato)
            print('-='*25)
            print(f'Saldo Atual: R${saldo}')

    elif opcao == 'x':
        break

    else:
        print('Opção invalida, digite uma das opções disponibilizadas no Menu.')

print('-='*30)
print('FIM DA OPERAÇÃO')
print('-='*30)
