co = float(input('comprimento do cateto oposto:  '))
ca = float(input('comprimento do cateto adijacente:  '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'a hipotenusa vai medir {hi:.2f}')

#ou

#hi = math.hypot(co,ca) mais facil
