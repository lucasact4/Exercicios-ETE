# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
f = float(input('Digita a temperatura em graus Fahrenheit: '))
c = 5 * ((f-32) / 9)
print(f'A temperatura {f}° em graus Fahrenheit será {c:.1f}° em graus Celcius.')
