A = float(input('Coeficiente A: '))
B = float(input('Coeficiente B: '))
C = float(input('Coeficiente C: '))
if A == 0 or (B == 0 and C == 0):
  print('Não é uma Equação do 2° Grau.')
else:
  delta = B ** 2 - 4 * A * C
  print(f'Valor de Delta: {delta: .2f}')
  if delta < 0:
    print('Não tem Raízes no conjunto dos números reais.')
  elif delta == 0:
    X1 = -B / (2 * A)
    print(f'Raiz X1 = X2 = {X1: .2f}')
  else:
    raizDelta = delta ** 0.5
    print(f'Valor da Raíz de Delta: {raizDelta: .2f}')
    X1 = (-B + raizDelta) / (2 * A)
    X2 = (-B - raizDelta) / (2 * A)
    print(f'Raiz X1 = {X1: .2f}')
    print(f'Raiz X2 = {X2: .2f}')