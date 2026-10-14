# Laboratório de Conjuntos

Este é um trabalho em Python sobre teoria dos conjuntos e conjuntos numéricos. Nós dividimos o programa em três partes para deixar o código organizado e fácil de entender.

- Na **Parte 1**, fazemos operações com conjuntos.
- Na **Parte 2**, classificamos números em N, Z, Q, I e R.
- Na **Parte 3**, recomendamos pessoas com interesses parecidos.

## Como executar

É necessário ter Python 3.10 ou mais recente. Não é preciso instalar bibliotecas.

No terminal, dentro da pasta do projeto, execute:

```powershell
python main.py
```

O programa abrirá um menu para escolher uma das três partes.

Para executar os testes:

```powershell
python -m unittest -v testes.py
```

## Arquivos do projeto

| Arquivo | Para que serve |
|---|---|
| `main.py` | Abre o menu principal. |
| `parte1_conjuntos.py` | Faz as operações de conjuntos. |
| `parte2_numeros.py` | Classifica números e contém os bônus. |
| `parte3_recomendacao.py` | Calcula a afinidade entre usuários. |
| `testes.py` | Testa automaticamente as três partes. |
| `RESULTADOS_TESTES.md` | Guarda exemplos reais de execução. |
| `RELATORIO.pdf` | Relatório final do trabalho. |

## Parte 1 — Operações com conjuntos

O usuário informa os conjuntos A, B e o universo U. Depois, pode escolher união, interseção, diferenças, diferença simétrica, pertinência, inclusão, cardinalidade ou complemento.

Primeiro fazemos cada operação manualmente, usando laços e condições. Depois usamos os recursos nativos do Python apenas para conferir se o resultado ficou correto.

Exemplo real:

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ∪ B
  Resultado manual: {1, 2, 3, 4, 5, 6}
  Resultado nativo: {1, 2, 3, 4, 5, 6}
  Resultados iguais? True

A ∩ B
  Resultado manual: {3, 4}
  Resultado nativo: {3, 4}
  Resultados iguais? True
```

Também testamos:

- conjunto vazio;
- conjuntos iguais;
- conjuntos disjuntos;
- um conjunto contido no outro;
- elementos repetidos;
- pertinência e complemento.

## Parte 2 — Classificação de números

O programa aceita inteiros, frações, decimais, dízimas e raízes. Ele informa os conjuntos numéricos aos quais o valor pertence e explica o motivo.

Neste trabalho consideramos que **zero pertence aos naturais**:

```text
N = {0, 1, 2, 3, ...}
```

Usamos `Fraction` para manter os cálculos exatos. Assim, `6/3` vira `2`, e `1,2(5)` vira exatamente `113/90`, sem arredondamento.

Alguns resultados testados:

| Entrada | Resultado |
|---|---|
| `-3` | Z, Q e R |
| `0` | N, Z, Q e R |
| `3/4` | Q e R |
| `-5/2` | Q e R |
| `6/3` | N, Z, Q e R |
| `0,(3)` | Q e R — dízima simples, geratriz 1/3 |
| `1,2(5)` | Q e R — dízima composta, geratriz 113/90 |
| `√9` | N, Z, Q e R |
| `√2` | I e R |

Exemplo real:

```text
Entrada: 1,2(5)
Tipo: dízima periódica composta
Interpretação: parte inteira=1, parte não periódica=2, período=5;
cálculo=(125 − 12)/90; geratriz simplificada=113/90
Pertence a: Q, R
```

Os bônus também estão prontos: geração de números primos pelo crivo de Eratóstenes e listagem dos divisores de um número.

## Parte 3 — Recomendação por interesses

Cada pessoa possui um conjunto de interesses. Para comparar duas pessoas, usamos o índice de Jaccard:

```text
J(A, B) = quantidade de interesses em comum / quantidade total de interesses diferentes
```

Quanto mais próximo de 1, maior é a afinidade.

Exemplo real:

```text
Ana × Bia: comuns={cinema, jazz}; união=6; J=0.33
Ana × Caio: comuns={cinema, games}; união=5; J=0.40
Maior afinidade: Caio
```

O programa também permite cadastrar novos usuários e trata empates.

## Testes

Foram executados 11 testes automatizados, todos aprovados. Eles verificam as operações manuais, as comparações nativas, os casos de borda, as classificações numéricas, entradas inválidas e as recomendações.

O registro completo está em [RESULTADOS_TESTES.md](RESULTADOS_TESTES.md).

## Relatório

O relatório final está em [RELATORIO.pdf](RELATORIO.pdf).

## Repositório

<https://github.com/sousarthuur/Laborat-rio-de-Conjuntos>
