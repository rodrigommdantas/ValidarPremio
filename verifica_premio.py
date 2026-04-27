# Programa para verificar se você ganhou um prêmio


def parse_user_numbers(numeros_usuario: str):
    if not numeros_usuario.strip():
        raise ValueError("Nenhum número informado")
    try:
        return list(map(int, numeros_usuario.split()))
    except ValueError as e:
        raise ValueError("Entrada inválida para números do usuário, digite novamente") from e


def check_number_in_list(lista_numeros, numero_sorteado):
    return numero_sorteado in lista_numeros


def main():
    numeros_usuario = input("Digite seus números separados por espaço: ")
    lista_numeros = parse_user_numbers(numeros_usuario)
    print(lista_numeros)
    while True:
        try:
            numero_sorteado = int(input("Digite o número sorteado: "))
            if check_number_in_list(lista_numeros, numero_sorteado):
                print("Parabéns! Você ganhou!")
                break
            else:
                print("Infelizmente, você não ganhou dessa vez. Tente outro número.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro...")


if __name__ == "__main__":
    main()
