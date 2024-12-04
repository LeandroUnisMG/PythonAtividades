def inverter_palavras(frase):

    palavras = frase.split()  # Divide a frase em palavras
    palavras_invertidas = [palavra[::-1] for palavra in palavras]  # Inverte cada palavra
    return " ".join(palavras_invertidas)  # Junta as palavras invertidas em uma nova frase

# Exemplo de uso
frase = "Inverter Palavras "
nova_frase = inverter_palavras(frase)
print("Frase original:", frase)
print("Frase com palavras invertidas:", nova_frase)
