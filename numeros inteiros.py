# Solicita ao usuário que digite um número inteiro
N = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if N > 0:
    # Calcula a soma de 1 até N usando a fórmula da soma de uma PA
    soma = (N * (N + 1)) // 2
    print(f"A soma de 1 até {N} é: {soma}")
else:
    print("Por favor, digite um número inteiro positivo.")
