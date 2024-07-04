def decodificar_cifra_cesar(texto_codificado, deslocamento):
    texto_decodificado = ""

    for char in texto_codificado:
        if char.isalpha():
            num = ord(char)
            num -= deslocamento

            if char.isupper():
                if num < ord('A'):
                    num += 26
                texto_decodificado += chr(num)
            elif char.islower():
                if num < ord('a'):
                    num += 26
                texto_decodificado += chr(num)
        else:
            texto_decodificado += char

    return texto_decodificado

# Exemplo de uso
texto_codificado = "Khoor Zruog!"
deslocamento = 3
texto_decodificado = decodificar_cifra_cesar(texto_codificado, deslocamento)
print("Texto decodificado:", texto_decodificado)
