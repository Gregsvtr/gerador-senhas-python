# Importa as bibliotecas necessárias
import random
import string

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    # Começamos com letras minúsculas (sempre incluídas)
    caracteres = string.ascii_lowercase
    
    # Adiciona as outras opções conforme a escolha do usuário
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
        
    # Gera a senha escolhendo caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    
    # Pede o tamanho da senha
    try:
        tamanho = int(input("Digite o tamanho da senha (ex: 12): "))
        if tamanho < 4:
            print("O tamanho mínimo deve ser 4 para garantir um pouco de segurança.")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    # Pergunta sobre os tipos de caracteres
    usar_maiusculas = input("Incluir letras MAIÚSCULAS? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir NÚMEROS? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir SÍMBOLOS (ex: @, #, $)? (s/n): ").lower() == 's'

    # Gera e exibe a senha
    senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
    
    print("\n" + "="*30)
    print(f"Sua senha segura é: {senha_gerada}")
    print("="*30)

if __name__ == "__main__":
    main()

