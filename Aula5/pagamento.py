def valorPagamento(a,b):
     if b <= 0:
          return a
     else:
          a = a * 1.03 + (b * 0.001 * a)
          return a

total = []
while 1:
     parcela = float(input('Qual o valor da prestação?: '))
     if parcela == 0:
          break

     atraso = int(input('Quandos dias de atraso?: '))
     total.append(valorPagamento(parcela,atraso))
     print('O valor a ser pago é: R$ {:.2f}\n'.format(valorPagamento(parcela,atraso)))

print('\nO valor total do dia foi: R$ {:.2f}'.format(sum(total)))
print('A quantidade de prestações pagas foi de: {}\n'.format(len(total)))