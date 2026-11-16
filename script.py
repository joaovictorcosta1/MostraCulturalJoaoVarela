"""Calculadora de Média Escolar.

Lê as notas de um aluno, calcula a média e informa a situação final
(Aprovado, Recuperação ou Reprovado).
"""

MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0


def ler_nota(mensagem):
    """Pede uma nota ao usuário até receber um valor válido entre 0 e 10."""
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 7.5).")
            continue
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")


def calcular_media(notas):
    """Retorna a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)


def classificar(media):
    """Retorna a situação do aluno de acordo com a média."""
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    if media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    return "Reprovado"


def main():
    print("=== Calculadora de Média Escolar ===")
    nome = input("Nome do aluno: ").strip() or "Aluno"

    while True:
        try:
            quantidade = int(input("Quantidade de notas: "))
            if quantidade > 0:
                break
            print("Informe um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    notas = [ler_nota(f"Nota {i}: ") for i in range(1, quantidade + 1)]

    media = calcular_media(notas)
    situacao = classificar(media)

    print("\n--- Resultado ---")
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()
