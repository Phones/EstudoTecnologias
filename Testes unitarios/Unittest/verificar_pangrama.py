import string

def verificar_pangrama(frase):
    frase = frase.lower()
    for letra in string.ascii_lowercase:
        if letra not in frase:
            return False
    
    return True