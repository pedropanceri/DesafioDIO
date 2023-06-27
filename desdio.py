extrato = {"saque": [], "deposito": []}
saque = saldo = deposito = dd = cont = 0
print('MENU PRINCIPAL')
dm = 3

while True:
    print('1: Mostrar saldo.\n2: Realizar saque.\n3: Realizar depósito.\n4: Visualizar extrato.\n5: Sair do menu.')
    opc = int(input('Qual opção desejada? '))
    if opc == 1:
        print(f'Saldo atual: R${saldo:.2f}')
    elif opc == 2:
        saque = int(input('Qual valor gostaria de sacar? '))
        if saque > saldo:
            print(f'Impossivel sacar essa quantia! Cheque seu saldo. ')
        elif 0 < saque <= saldo:
            saldo -= saque
            print(f'Saque de R${saque:.2f} realizado com sucesso! Seu novo saldo é de R${saldo:.2f}. ')
            extrato["saque"].append(saque)
        elif saque < 0:
            print('Impossivel sacar valores negativos! Tente novamente. ')
    elif opc == 3:
        if dd == dm:
            print(f'Limite de depósitos diários máximos atingido! Volte amanhã para depositar novamente.')
        else:
            deposito = int(input('Qual valor gostaria de depositar? '))
            if 500 >= deposito > 0:
                dd += 1
                saldo += deposito
                print(f'Depósito de R${deposito:.2f} realizado com sucesso! Seu novo saldo é de R${saldo:.2f}')
                extrato["deposito"].append(deposito)
                cont += 1
            elif deposito > 500:
                print('Impossível depositar mais de R$500.00 de uma vez. Tente novamente.')
            else:
                print('Operação cancelada. Tente novamente. ')
    elif opc == 4:
        for k, v in extrato.items():
            print(f'{k}: {v}. ')
    elif opc == 5:
        print('Atendimento encerrado. Até a próxima. ')
        break
    else:
        print('Digite uma opção válida. ')


