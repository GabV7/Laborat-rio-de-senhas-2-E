# cifrador.py

def criptografar_cesar(texto, deslocamento=1):
    """Criptografa o texto deslocando os caracteres com base no deslocamento fornecido."""
    resultado = ""
    for caractere in texto:
        if caractere.isdigit():
            novo_digito = (int(caractere) + deslocamento) % 10
            resultado += str(novo_digito)
        elif caractere.isalpha():
            codigo = ord(caractere)
            limite = ord('A') if caractere.isupper() else ord('a')
            novo_caractere = chr((codigo - limite + deslocamento) % 26 + limite)
            resultado += novo_caractere
        else:
            resultado += caractere
    return resultado

def descriptografar_cesar(texto, deslocamento=1):
    """Descriptografa o texto revertendo o deslocamento."""
    return criptografar_cesar(texto, -deslocamento)
