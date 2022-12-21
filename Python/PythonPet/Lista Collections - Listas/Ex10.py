# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. F = (C * 1,8) + 32.
c = float(input('Digita a temperatura em graus Celcius: '))
f = (c * 1.8) + 32
print(f'A temperatura {c}° em graus Celcius será {f:.1f}° em graus Fahrenheit.')
