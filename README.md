# Laborat-rio-de-senhas-2-E
Laboratório de senhas
# cifrador.py

def criptografar_cesar(texto, deslocamento=1):
    """Criptografa o texto deslocando os caracteres com base no deslocamento fornecido."""
    resultado = ""
    for caractere in texto:
        if caractere.isdigit():
            # Desloca números de forma cíclica (0-9)
            novo_digito = (int(caractere) + deslocamento) % 10
            resultado += str(novo_digito)
        elif caractere.isalpha():
            # Desloca letras mantendo maiúsculas e minúsculas
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
# main.py
from cifrador import criptografar_cesar, descriptografar_cesar
from hash_sistema import gerar_hash_senha, verificar_senha, ataque_forca_bruta

def exibir_menu():
    print("\n==============================================")
    print("🔒 SISTEMA DE CRIPTOGRAFIA E HASH COM PYTHON")
    print("==============================================")
    print("1. Criptografar texto (Cifra simples)")
    print("2. Descriptografar texto")
    print("3. Gerar Hash SHA-256 de uma senha")
    print("4. Simular Autenticação Segura")
    print("5. Simular Ataque de Força Bruta")
    print("6. Sair")
    print("----------------------------------------------")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            texto = input("Digite a senha ou texto original (ex: 123456): ")
            try:
                deslocamento = int(input("Digite o valor de deslocamento (padrão 1): ") or 1)
            except ValueError:
                deslocamento = 1
            criptografado = criptografar_cesar(texto, deslocamento)
            print(f"\n[SUCESSO] Texto Criptografado: {criptografado}")

        elif opcao == "2":
            texto = input("Digite o texto criptografado: ")
            try:
                deslocamento = int(input("Digite o valor de deslocamento utilizado: ") or 1)
            except ValueError:
                deslocamento = 1
            descriptografado = descriptografar_cesar(texto, deslocamento)
            print(f"\n[SUCESSO] Texto Original: {descriptografado}")

        elif opcao == "3":
            senha = input("Digite a senha para gerar o hash: ")
            h = gerar_hash_senha(senha)
            print(f"\n[SUCESSO] Hash SHA-256: {h}")

        elif opcao == "4":
            print("\n--- Simulação de Autenticação ---")
            cadastrada = input("Defina a senha do usuário: ")
            hash_cadastrado = gerar_hash_senha(cadastrada)
            
            tentativa = input("Digite a senha para fazer login: ")
            if verificar_senha(tentativa, hash_cadastrado):
                print("\n✅ Acesso Permitido! Senha correta.")
            else:
                print("\n❌ Acesso Negado! Senha incorreta.")

        elif opcao == "5":
            print("\n--- Simulação de Ataque de Força Bruta ---")
            senha_secreta = "senha123"
            hash_alvo = gerar_hash_senha(senha_secreta)
            print(f"O sistema gerou um hash seguro para uma senha oculta.")
            
            # Lista simulada de senhas comuns
            dicionario = ["123456", "admin", "senha123", "password", "python2026"]
            print("Testando senhas do dicionário...")
            
            encontrada = ataque_forca_bruta(hash_alvo, dicionario)
            if encontrada:
                print(f"\n⚠️ Alerta de Segurança: Senha descoberta por força bruta -> '{encontrada}'")
            else:
                print("\n🛡️ A senha não foi encontrada na lista de teste.")

        elif opcao == "6":
            print("\nEncerrando o programa. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()
# Projeto: Proteção de Informações - Criptografia e Hash com Python

Projeto desenvolvido com base nos conceitos de segurança da informação, criptografia básica de substituição e funções de hash em Python.

## Funcionalidades
1. **Cifra de Substituição:** Permite ocultar números e caracteres aplicando regras de deslocamento (ex: proteger senhas anotadas de forma inteligente).
2. **Hash SHA-256:** Conversão irreversível de senhas para armazenamento seguro.
3. **Autenticação:** Validação de credenciais comparando hashes.
4. **Simulação de Força Bruta:** Demonstração prática de como senhas fracas podem ser vulneráveis a ataques de dicionário.

## Como Executar
Certifique-se de ter o Python instalado em sua máquina. No terminal, execute:

```bash
python main.py
