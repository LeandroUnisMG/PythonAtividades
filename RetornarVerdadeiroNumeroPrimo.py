def N_primo(numero):
    """Retorna True se o número for primo, False caso contrário."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testando de 1 a 100
print("Números primos de 1 a 100:")
for n in range(1, 101):
    if N_primo(n):
        print(n, end=" ")
