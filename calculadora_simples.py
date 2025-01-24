# Calculadora Simples

num1 = 0
num2 = 0
resultado = 0
op = ""

num1 = int(input('Digite o num1: '))
operacao = input('digite a op: ')
num2 = int(input('Digite o num2: '))

if operacao == '+':
  resultado = num1 + num2
elif operacao == '-':
  resultado = num1 - num2
elif operacao == '*':
  resultado = num1 * num2
elif operacao == '/':
  resultado = num1 / num2
else:
  rsultado = 'Operação Inválida'
print(str(num1) + ' ' + str(operacao) + ' ' + str(num2) + ' = ' + str(resultado))
