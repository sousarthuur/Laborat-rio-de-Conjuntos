"""Parte 2: classificador exato de inteiros, frações, decimais, dízimas e raízes."""

import math
import re
import sys
from fractions import Fraction


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def nomes_conjuntos(conjuntos):
    ordem = ["N", "Z", "Q", "I", "R"]
    return ", ".join(nome for nome in ordem if nome in conjuntos)


def classificar_racional(valor):
    """Classifica uma Fraction sem conversão para float. Adotamos 0 ∈ N."""
    conjuntos = ["Q", "R"]
    if valor.denominator == 1:
        conjuntos.insert(0, "Z")
        if valor.numerator >= 0:
            conjuntos.insert(0, "N")
    return conjuntos


def converter_fracao(texto):
    """Converte a/b exatamente; Fraction também faz a simplificação."""
    partes = texto.split("/")
    if len(partes) != 2:
        raise ValueError("use o formato a/b, com uma única barra")
    try:
        numerador = int(partes[0].strip())
        denominador = int(partes[1].strip())
    except ValueError as erro:
        raise ValueError("numerador e denominador devem ser inteiros") from erro
    if denominador == 0:
        raise ValueError("o denominador não pode ser zero")
    return Fraction(numerador, denominador)


def converter_decimal(texto):
    """Converte decimal finito em fração exata, aceitando ponto ou vírgula."""
    normalizado = texto.replace(",", ".")
    if not re.fullmatch(r"[+-]?(?:\d+\.\d+|\d+)", normalizado):
        raise ValueError("decimal malformado")
    return Fraction(normalizado)


def calcular_fracao_geratriz(texto):
    """Calcula a geratriz pela subtração dos blocos com e sem o período."""
    padrao = r"([+-]?)(\d+)[,.](\d*)\((\d+)\)"
    resultado = re.fullmatch(padrao, texto.strip())
    if not resultado:
        raise ValueError("use, por exemplo, 0,(3) ou 1,2(5)")

    sinal, inteira, nao_periodica, periodo = resultado.groups()
    quantidade_nao_periodica = len(nao_periodica)
    quantidade_periodo = len(periodo)

    # Ex.: 1,2(5): 125 - 12, dividido por 10 × 9.
    bloco_com_periodo = int(inteira + nao_periodica + periodo)
    bloco_sem_periodo = int(inteira + nao_periodica)
    numerador = bloco_com_periodo - bloco_sem_periodo
    denominador = (10 ** quantidade_nao_periodica) * (10 ** quantidade_periodo - 1)
    if sinal == "-":
        numerador = -numerador
    fracao = Fraction(numerador, denominador)

    etapas = (
        f"parte inteira={inteira}, parte não periódica="
        f"{nao_periodica or 'vazia'}, período={periodo}; "
        f"cálculo=({bloco_com_periodo} − {bloco_sem_periodo})/{denominador}"
    )
    if sinal == "-":
        etapas += ", com sinal negativo"
    return fracao, etapas


def classificar_raiz(texto):
    """Classifica √n para n inteiro; não usa aproximação como prova."""
    limpo = texto.strip().lower().replace(" ", "")
    if limpo.startswith("√"):
        radicando_texto = limpo[1:]
    elif limpo.startswith("sqrt"):
        radicando_texto = limpo[4:]
    else:
        raise ValueError("a raiz deve começar com √ ou sqrt")
    if radicando_texto.startswith("(") and radicando_texto.endswith(")"):
        radicando_texto = radicando_texto[1:-1]
    try:
        radicando = int(radicando_texto)
    except ValueError as erro:
        raise ValueError("esta versão aceita raiz apenas de número inteiro") from erro

    if radicando < 0:
        return {
            "valor": None,
            "interpretacao": f"raiz quadrada de {radicando}",
            "conjuntos": [],
            "justificativa": "Raiz de número negativo não pertence aos números reais.",
        }

    raiz = math.isqrt(radicando)
    if raiz * raiz == radicando:
        valor = Fraction(raiz, 1)
        return {
            "valor": valor,
            "interpretacao": f"raiz exata: √{radicando} = {raiz}",
            "conjuntos": classificar_racional(valor),
            "justificativa": f"{raiz} × {raiz} = {radicando}; portanto, a raiz é inteira.",
        }
    return {
        "valor": f"√{radicando}",
        "interpretacao": f"raiz não exata de inteiro não negativo: √{radicando}",
        "conjuntos": ["I", "R"],
        "justificativa": (
            f"{radicando} não é quadrado perfeito; a raiz de um inteiro não negativo "
            "que não é quadrado perfeito é irracional."
        ),
    }


def classificar_numero(entrada):
    """Interpreta a entrada e devolve tipo, valor, conjuntos e justificativa."""
    texto = entrada.strip()
    if not texto:
        raise ValueError("a entrada não pode ficar vazia")
    if texto.startswith("√") or texto.lower().startswith("sqrt"):
        resultado = classificar_raiz(texto)
        resultado["entrada"] = entrada
        resultado["tipo"] = "raiz quadrada"
        return resultado

    if "(" in texto or ")" in texto:
        valor, etapas = calcular_fracao_geratriz(texto)
        return {
            "entrada": entrada,
            "tipo": "dízima periódica",
            "valor": valor,
            "interpretacao": f"{etapas}; geratriz simplificada={valor}",
            "conjuntos": classificar_racional(valor),
            "justificativa": "Toda dízima periódica possui fração geratriz e é racional.",
        }

    if "/" in texto:
        valor = converter_fracao(texto)
        tipo = "fração"
        interpretacao = f"fração simplificada: {valor}"
    else:
        valor = converter_decimal(texto)
        tipo = "inteiro" if valor.denominator == 1 and not any(c in texto for c in ",.") else "decimal exato"
        interpretacao = f"valor exato representado por {valor}"

    conjuntos = classificar_racional(valor)
    if valor.denominator == 1:
        justificativa = "O valor é inteiro, pode ser escrito sobre 1 e também é racional e real."
        if valor >= 0:
            justificativa += " Pela convenção N = {0, 1, 2, ...}, também é natural."
    else:
        justificativa = "É uma razão entre inteiros com denominador não nulo; logo, é racional e real."
    return {
        "entrada": entrada,
        "tipo": tipo,
        "valor": valor,
        "interpretacao": interpretacao,
        "conjuntos": conjuntos,
        "justificativa": justificativa,
    }


def exibir_classificacao(resultado):
    print(f"Entrada: {resultado['entrada']}")
    print(f"Tipo: {resultado['tipo']}")
    print(f"Interpretação: {resultado['interpretacao']}")
    print(f"Pertence a: {nomes_conjuntos(resultado['conjuntos']) or 'nenhum entre N, Z, Q, I e R'}")
    print(f"Justificativa: {resultado['justificativa']}")


def gerar_primos(limite):
    """Crivo de Eratóstenes: elimina múltiplos de cada primo encontrado."""
    if limite < 2:
        return []
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = eh_primo[1] = False
    candidato = 2
    while candidato * candidato <= limite:
        if eh_primo[candidato]:
            multiplo = candidato * candidato
            while multiplo <= limite:
                eh_primo[multiplo] = False
                multiplo += candidato
        candidato += 1
    return [numero for numero in range(2, limite + 1) if eh_primo[numero]]


def listar_divisores(numero):
    """Lista divisores positivos; zero não possui uma lista finita deles."""
    if numero == 0:
        raise ValueError("zero possui infinitos divisores; não é possível listá-los")
    numero = abs(numero)
    return [divisor for divisor in range(1, numero + 1) if numero % divisor == 0]


def ler_inteiro(mensagem):
    try:
        return int(input(mensagem).strip())
    except ValueError:
        print("Entrada inválida: digite um número inteiro.")
        return None


def executar_parte2():
    while True:
        print("\nPARTE 2 — CONJUNTOS NUMÉRICOS (0 pertence a N)")
        print("1 - Classificar número\n2 - Bônus: gerar primos\n3 - Bônus: listar divisores\n0 - Voltar")
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            entrada = input("Número (ex.: -3, 3/4, 0,(3), √2): ")
            try:
                exibir_classificacao(classificar_numero(entrada))
            except ValueError as erro:
                print(f"Entrada inválida: {erro}.")
        elif opcao == "2":
            limite = ler_inteiro("Gerar primos de 2 até: ")
            if limite is not None:
                print("Primos:", gerar_primos(limite))
        elif opcao == "3":
            numero = ler_inteiro("Número inteiro: ")
            if numero is not None:
                try:
                    print("Divisores positivos:", listar_divisores(numero))
                except ValueError as erro:
                    print(f"Entrada inválida: {erro}.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar_parte2()
