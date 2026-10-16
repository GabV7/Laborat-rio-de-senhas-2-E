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
            print("O sistema gerou um hash seguro para uma senha oculta.")
            
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
