limite = 1500
numero_saque = 0
LIMITE_SAQUE = 3
extrato = []

while True :
    menu = input(f'''
####Banco Da Camila####

(s) saque
(d) depósito
(e) extrato
(f) sair
Digite o que deseja realizar:
''')

    if menu == 'f':
        print("Você saiu da operação.")
        break 


    if menu == 's':

        if numero_saque == LIMITE_SAQUE:
            print(f'O limite de {LIMITE_SAQUE} saques diários foi atingido')
             
        else:
            valor_saque = float(input('Digite o quanto quer sacar:'))

        if valor_saque <= 0:
            print("O valor do saque deve ser positivo.")

        elif valor_saque <= limite and valor_saque <= 500:
            if valor_saque <= 0:
                print("O valor do saque deve ser positivo.")
            limite -= valor_saque
            numero_saque += 1
            extrato.append(f'Saque feito de R${valor_saque}')
            print (f'Você sacou {valor_saque} e agora tem {limite} dísponivel')

        else:
            print('Valor indisponível para saque')


    if menu == 'd' : 
        valor_deposito = float(input('Digite o valor que gostaría de depositar:'))

        if valor_deposito > 0:
                 limite += valor_deposito
                 print(f'Você depositou {valor_deposito} e agora seu limite é de {limite}')
                 extrato.append(f'Extrato feito de R${valor_deposito}')
        else:
           print("O valor do depósito deve ser positivo.")
    

    elif menu == 'e':
        print(extrato)
      
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")