"""Menu principal do Laboratório de Conjuntos."""

import sys

from parte1_conjuntos import executar_parte1
from parte2_numeros import executar_parte2
from parte3_recomendacao import executar_parte3


# Garante que acentos e símbolos matemáticos funcionem também no Windows.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    """Exibe o menu e chama o módulo escolhido até o usuário encerrar."""
    while True:
        print("\n" + "=" * 40)
        print("     LABORATÓRIO DE CONJUNTOS")
        print("=" * 40)
        print("1 - Parte 1: Teoria dos Conjuntos")
        print("2 - Parte 2: Conjuntos Numéricos")
        print("3 - Parte 3: Sistema de Recomendação")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            executar_parte1()
        elif opcao == "2":
            executar_parte2()
        elif opcao == "3":
            executar_parte3()
        elif opcao == "0":
            print("Programa encerrado. Até a próxima!")
            break
        else:
            print("Opção inválida. Digite 0, 1, 2 ou 3.")


if __name__ == "__main__":
    main()
