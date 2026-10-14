"""Parte 1: operações de conjuntos implementadas com listas e laços."""

import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def pertence(elemento_procurado, elementos):
    """Verifica pertinência somente com laço e comparação de igualdade."""
    for elemento_atual in elementos:
        if elemento_atual == elemento_procurado:
            return True
    return False


def remover_repetidos(elementos):
    """Cria uma lista sem repetições, mantendo a ordem digitada."""
    resultado = []
    for elemento in elementos:
        if not pertence(elemento, resultado):
            resultado.append(elemento)
    return resultado


def ler_conjunto(mensagem):
    """Lê elementos separados por vírgula; entrada vazia representa ∅."""
    texto = input(mensagem).strip()
    if not texto:
        return []
    elementos = [item.strip() for item in texto.split(",") if item.strip()]
    return remover_repetidos(elementos)


def uniao(a, b):
    """A ∪ B contém tudo o que aparece em A ou em B."""
    resultado = []
    for elemento in a:
        if not pertence(elemento, resultado):
            resultado.append(elemento)
    for elemento in b:
        if not pertence(elemento, resultado):
            resultado.append(elemento)
    return resultado


def intersecao(a, b):
    """A ∩ B contém somente os elementos comuns aos dois conjuntos."""
    resultado = []
    for elemento in a:
        if pertence(elemento, b) and not pertence(elemento, resultado):
            resultado.append(elemento)
    return resultado


def diferenca(a, b):
    """A − B contém os elementos de A que não aparecem em B."""
    resultado = []
    for elemento in a:
        if not pertence(elemento, b) and not pertence(elemento, resultado):
            resultado.append(elemento)
    return resultado


def diferenca_simetrica(a, b):
    """A Δ B contém o que pertence a apenas um dos conjuntos."""
    return uniao(diferenca(a, b), diferenca(b, a))


def esta_contido(a, b):
    """Testa A ⊆ B percorrendo os elementos de A."""
    for elemento in a:
        if not pertence(elemento, b):
            return False
    return True


def conjuntos_iguais(a, b):
    """Dois conjuntos são iguais quando cada um está contido no outro."""
    return esta_contido(a, b) and esta_contido(b, a)


def inclusao_propria(a, b):
    """Testa A ⊂ B: A está contido em B, mas A e B não são iguais."""
    return esta_contido(a, b) and not conjuntos_iguais(a, b)


def cardinalidade(a):
    """Conta os elementos distintos sem usar len como operação final."""
    total = 0
    for _ in remover_repetidos(a):
        total += 1
    return total


def complemento(a, universo):
    """O complemento de A em U é U − A."""
    return diferenca(universo, a)


def formatar_conjunto(elementos):
    return "∅" if not elementos else "{" + ", ".join(elementos) + "}"


def validacao_nativa(a, b, universo, elemento):
    """Usa recursos nativos somente depois dos cálculos manuais."""
    sa, sb, su = set(a), set(b), set(universo)
    return {
        "união": sa | sb,
        "interseção": sa & sb,
        "A - B": sa - sb,
        "B - A": sb - sa,
        "diferença simétrica": sa ^ sb,
        "pertinência em A": elemento in sa,
        "A subconjunto de B": sa <= sb,
        "A subconjunto próprio de B": sa < sb,
        "B subconjunto de A": sb <= sa,
        "B subconjunto próprio de A": sb < sa,
        "cardinalidade de A": len(sa),
        "cardinalidade de B": len(sb),
        "complemento": su - sa,
    }


def resultados_manuais(a, b, universo, elemento):
    """Calcula todas as operações antes de consultar a solução nativa."""
    return {
        "união": uniao(a, b),
        "interseção": intersecao(a, b),
        "A - B": diferenca(a, b),
        "B - A": diferenca(b, a),
        "diferença simétrica": diferenca_simetrica(a, b),
        "pertinência em A": pertence(elemento, a),
        "A subconjunto de B": esta_contido(a, b),
        "A subconjunto próprio de B": inclusao_propria(a, b),
        "B subconjunto de A": esta_contido(b, a),
        "B subconjunto próprio de A": inclusao_propria(b, a),
        "cardinalidade de A": cardinalidade(a),
        "cardinalidade de B": cardinalidade(b),
        "complemento": complemento(a, universo),
    }


def comparar_resultado(nome, manual, nativo):
    """Mostra lado a lado o cálculo manual e a validação nativa."""
    if isinstance(manual, list):
        manual_para_comparar = set(manual)
        manual_exibido = formatar_conjunto(manual)
        nativo_exibido = formatar_conjunto(sorted(nativo))
    else:
        manual_para_comparar = manual
        manual_exibido = str(manual)
        nativo_exibido = str(nativo)
    print(f"\n{nome}")
    print(f"  Resultado manual: {manual_exibido}")
    print(f"  Resultado nativo: {nativo_exibido}")
    print(f"  Resultados iguais? {manual_para_comparar == nativo}")


def executar_parte1():
    """Interface interativa com menu para escolher cada operação."""
    print("\nPARTE 1 — TEORIA DOS CONJUNTOS")
    print("Separe os elementos por vírgulas. Enter sozinho representa ∅.")
    a = ler_conjunto("Conjunto A: ")
    b = ler_conjunto("Conjunto B: ")
    universo = ler_conjunto("Universo U (inclua A e B): ")

    if not esta_contido(a, universo) or not esta_contido(b, universo):
        print("Aviso: matematicamente, U deve conter todos os elementos de A e B.")

    while True:
        print("""
1 - União
2 - Interseção
3 - Diferenças A-B e B-A
4 - Diferença simétrica
5 - Pertinência em A
6 - Inclusões
7 - Cardinalidades e complemento
8 - Mostrar e validar todas as operações
0 - Voltar ao menu principal
""")
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            return
        opcao_valida = (
            opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4"
            or opcao == "5" or opcao == "6" or opcao == "7" or opcao == "8"
        )
        if not opcao_valida:
            print("Opção inválida.")
            continue

        elemento = ""
        if opcao == "5" or opcao == "8":
            elemento = input("Elemento para testar pertinência em A: ").strip()

        manual = resultados_manuais(a, b, universo, elemento)
        nativo = validacao_nativa(a, b, universo, elemento)

        if opcao == "1" or opcao == "8":
            comparar_resultado("A ∪ B", manual["união"], nativo["união"])
        if opcao == "2" or opcao == "8":
            comparar_resultado("A ∩ B", manual["interseção"], nativo["interseção"])
        if opcao == "3" or opcao == "8":
            comparar_resultado("A − B", manual["A - B"], nativo["A - B"])
            comparar_resultado("B − A", manual["B - A"], nativo["B - A"])
        if opcao == "4" or opcao == "8":
            comparar_resultado(
                "A Δ B", manual["diferença simétrica"], nativo["diferença simétrica"]
            )
        if opcao == "5" or opcao == "8":
            comparar_resultado(
                f"{elemento!r} ∈ A", manual["pertinência em A"], nativo["pertinência em A"]
            )
        if opcao == "6" or opcao == "8":
            for nome in (
                "A subconjunto de B", "A subconjunto próprio de B",
                "B subconjunto de A", "B subconjunto próprio de A",
            ):
                comparar_resultado(nome, manual[nome], nativo[nome])
        if opcao == "7" or opcao == "8":
            comparar_resultado(
                "Cardinalidade de A", manual["cardinalidade de A"], nativo["cardinalidade de A"]
            )
            comparar_resultado(
                "Cardinalidade de B", manual["cardinalidade de B"], nativo["cardinalidade de B"]
            )
            comparar_resultado(
                "Complemento de A em U", manual["complemento"], nativo["complemento"]
            )


if __name__ == "__main__":
    executar_parte1()
