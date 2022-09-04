salario = float(input())
if salario <= 400.00:
    reajuste = 0.15
    percent = int(reajuste*100)
    valor_reajuste = salario*reajuste
    novo_salario = salario + valor_reajuste
    print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(novo_salario, valor_reajuste, percent))
else:
    if salario > 400.00 and salario <= 800.00:
        reajuste = 0.12
        percent = int(reajuste*100)
        valor_reajuste = salario*reajuste
        novo_salario = salario + valor_reajuste
        print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(novo_salario, valor_reajuste, percent))
    else:
        if salario > 800.00 and salario <= 1200.00:
            reajuste = 0.10
            percent = int(reajuste*100)
            valor_reajuste = salario*reajuste
            novo_salario = salario + valor_reajuste
            print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(novo_salario, valor_reajuste, percent))
        else:
            if salario > 1200.00 and salario <= 2000.00:
                reajuste = 0.07
                percent = int(reajuste*100)
                valor_reajuste = salario*reajuste
                novo_salario = salario + valor_reajuste
                print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(novo_salario, valor_reajuste, percent))
            else:
                reajuste = 0.04
                percent = int(reajuste*100)
                valor_reajuste = salario*reajuste
                novo_salario = salario + valor_reajuste
                print('Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2} %'.format(novo_salario, valor_reajuste, percent))