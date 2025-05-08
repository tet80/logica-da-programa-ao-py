#um algoritmo que calcula o peso ideial
#Para homens: (72,7*h) - 58
#Para mulhers: (62,1*h) - 44,7 (h - altura)

altura = float(input("digite sua altura: "))
sexo =input("digite seu sexo (M ou F):")

if(sexo=="M"):
    peso_ideal = (72,7*altura) - 58
    print("sexo Masculino!")
else:
    peso_ideal = (62,1*altura) - 44,7
    print("sexo Feminino!")

print(f"O seu peso ideal seria: {peso_ideal}")