"""Parte 1: operações de conjuntos implementadas com listas e laços."""

import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def remover_repetidos(elementos):
    """Cria uma lista sem repetições, mantendo a ordem digitada."""
    resultado = []
    for elemento in elementos:
        if elemento not in resultado:
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
        if elemento not in resultado:
            resultado.append(elemento)
    for elemento in b:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def intersecao(a, b):
    """A ∩ B contém somente os elementos comuns aos dois conjuntos."""
    resultado = []
    for elemento in a:
        if elemento in b and elemento not in resultado:
            resultado.append(elemento)
    return resultado


def diferenca(a, b):
    """A − B contém os elementos de A que não aparecem em B."""
    resultado = []
    for elemento in a:
        if elemento not in b and elemento not in resultado:
            resultado.append(elemento)
    return resultado


def diferenca_simetrica(a, b):
    """A Δ B contém o que pertence a apenas um dos conjuntos."""
    return uniao(diferenca(a, b), diferenca(b, a))


def esta_contido(a, b):
    """Testa A ⊆ B percorrendo os elementos de A."""
    for elemento in a:
        if elemento not in b:
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


def validacao_nativa(a, b, universo):
    """Usa set somente para conferir os resultados manuais."""
    sa, sb, su = set(a), set(b), set(universo)
    return {
        "união": sa | sb,
        "interseção": sa & sb,
        "A - B": sa - sb,
        "B - A": sb - sa,
        "diferença simétrica": sa ^ sb,
        "complemento": su - sa,
    }


def executar_parte1():
    """Interface interativa da Parte 1."""
    print("\nPARTE 1 — TEORIA DOS CONJUNTOS")
    print("Separe os elementos por vírgulas. Enter sozinho representa ∅.")
    a = ler_conjunto("Conjunto A: ")
    b = ler_conjunto("Conjunto B: ")
    universo = ler_conjunto("Universo U (inclua A e B): ")

    if not esta_contido(a, universo) or not esta_contido(b, universo):
        print("Aviso: matematicamente, U deve conter todos os elementos de A e B.")

    print(f"\nA = {formatar_conjunto(a)}; |A| = {cardinalidade(a)}")
    print(f"B = {formatar_conjunto(b)}; |B| = {cardinalidade(b)}")
    print(f"A ∪ B = {formatar_conjunto(uniao(a, b))}")
    print(f"A ∩ B = {formatar_conjunto(intersecao(a, b))}")
    print(f"A − B = {formatar_conjunto(diferenca(a, b))}")
    print(f"B − A = {formatar_conjunto(diferenca(b, a))}")
    print(f"A Δ B = {formatar_conjunto(diferenca_simetrica(a, b))}")
    print(f"A ⊆ B? {esta_contido(a, b)}; A ⊂ B? {inclusao_propria(a, b)}")
    print(f"B ⊆ A? {esta_contido(b, a)}; B ⊂ A? {inclusao_propria(b, a)}")
    print(f"Complemento de A em U = {formatar_conjunto(complemento(a, universo))}")

    elemento = input("Elemento para testar pertinência em A: ").strip()
    print(f"{elemento!r} ∈ A? {elemento in a}")

    manual = {
        "união": set(uniao(a, b)),
        "interseção": set(intersecao(a, b)),
        "A - B": set(diferenca(a, b)),
        "B - A": set(diferenca(b, a)),
        "diferença simétrica": set(diferenca_simetrica(a, b)),
        "complemento": set(complemento(a, universo)),
    }
    nativo = validacao_nativa(a, b, universo)
    print("\nConferência com as operações nativas do Python:")
    for nome in manual:
        estado = "OK" if manual[nome] == nativo[nome] else "DIVERGENTE"
        print(f"- {nome}: {estado}")


if __name__ == "__main__":
    executar_parte1()
