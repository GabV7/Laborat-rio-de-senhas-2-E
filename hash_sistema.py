# hash_sistema.py
import hashlib

def gerar_hash_senha(senha):
    """Gera o hash SHA-256 de uma senha."""
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def verificar_senha(senha_digitada, hash_salvo):
    """Verifica se a senha digitada confere com o hash armazenado."""
    return gerar_hash_senha(senha_digitada) == hash_salvo

def ataque_forca_bruta(hash_alvo, lista_senhas):
    """Simula um ataque de força bruta testando senhas de uma lista."""
    for senha in lista_senhas:
        if gerar_hash_senha(senha) == hash_alvo:
            return senha
    return None
