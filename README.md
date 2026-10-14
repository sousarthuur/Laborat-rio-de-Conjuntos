# Laboratório de Conjuntos

Projeto acadêmico da disciplina de Desenvolvimento de Software Multiplataforma — Fatec Osasco. O programa aplica teoria dos conjuntos, classifica conjuntos numéricos e recomenda usuários por interesses.

## Requisitos identificados no enunciado

- Três partes, com exemplos de execução em todas elas.
- Parte 1: união, interseção, diferenças, diferença simétrica, pertinência, inclusão própria e não própria, cardinalidade e complemento. As operações são manuais e comparadas à solução nativa.
- Parte 2: classificar inteiros, frações, decimais, dízimas e raízes em N, Z, Q, I e R. Calcular fração geratriz. O crivo e os divisores são bônus.
- Parte 3: escolher um entre quatro mini-projetos. Foi escolhida a recomendação por interesses com índice de Jaccard.
- Pelo menos três execuções na Parte 1, oito números na Parte 2 e três cenários na Parte 3; casos esperados calculados e comparados à saída.
- Código em GitHub, README com logs/prints e relatório de uma página.

## Conceitos matemáticos

- **N (naturais):** adotamos `N = {0, 1, 2, ...}`; portanto, zero pertence a N.
- **Z (inteiros):** inteiros negativos, zero e positivos.
- **Q (racionais):** números escritos como `a/b`, com inteiros `a`, `b` e `b ≠ 0`.
- **I (irracionais):** reais que não podem ser escritos como razão de inteiros, como `√2`.
- **R (reais):** reúne racionais e irracionais. As inclusões são `N ⊂ Z ⊂ Q ⊂ R` e `I ⊂ R`.

Um número pode estar em vários conjuntos: `7` está em N, Z, Q e R, pois também é inteiro e pode ser escrito como `7/1`.

## Estrutura

```text
.
├── main.py                    # menu principal
├── parte1_conjuntos.py        # operações manuais e validação nativa
├── parte2_numeros.py          # classificador, geratrizes, raízes e bônus
├── parte3_recomendacao.py     # cadastro e índice de Jaccard
├── testes.py                  # testes automatizados
├── RESULTADOS_TESTES.md       # registro da execução real
├── RELATORIO.md               # relatório final de uma página
└── README.md
```

## Execução

É necessário Python 3.10 ou mais recente; não há dependências externas. No terminal do VS Code, abra esta pasta e execute:

```powershell
python main.py
```

Para executar os testes:

```powershell
python -m unittest -v testes.py
```

## Parte 1 — implementação e exemplos

Os elementos são lidos como textos separados por vírgula. Isso permite conjuntos de números, nomes ou palavras. A entrada vazia é `∅`. O submenu permite escolher cada operação ou executar todas. `pertence`, `remover_repetidos`, `uniao`, `intersecao`, `diferenca`, `diferenca_simetrica`, `esta_contido`, `inclusao_propria`, `cardinalidade` e `complemento` usam somente laços, comparações e condicionais. A implementação manual não usa `in`, `not in` nem operadores de `set`. A camada de validação usa os recursos nativos somente depois dos cálculos manuais.

Entradas e resultados esperados/obtidos nos testes:

| Cenário | Entrada | Resultado esperado e obtido |
|---|---|---|
| Geral/repetidos | A=1,2,2,3,4; B=3,4,5,6 | A sem repetição; união={1,2,3,4,5,6}; interseção={3,4}; Δ={1,2,5,6} |
| Vazio | A=∅; B={1,2} | A⊆B verdadeiro; união={1,2}; interseção=∅ |
| Iguais | A=B={1,2} | A⊆B verdadeiro; A⊂B falso; A−B=∅ |
| Disjuntos | A={1,2}; B={3,4} | interseção=∅; união={1,2,3,4} |
| Contido | A={1,2}; B={1,2,3} | A⊂B verdadeiro |
| Pertinência | A={1,2,3} | 3∈A verdadeiro; 5∈A falso |
| Complemento | A={1,2,3,4}; U={1,...,10} | Aᶜ={5,6,7,8,9,10} |

Trecho de uma execução real da opção **Mostrar e validar todas as operações**:

```text
A ∪ B
  Resultado manual: {1, 2, 3, 4, 5, 6}
  Resultado nativo: {1, 2, 3, 4, 5, 6}
  Resultados iguais? True

'3' ∈ A
  Resultado manual: True
  Resultado nativo: True
  Resultados iguais? True

Cardinalidade de A
  Resultado manual: 4
  Resultado nativo: 4
  Resultados iguais? True
```

As demais operações da mesma execução também produziram `Resultados iguais? True`, incluindo interseção, duas diferenças, diferença simétrica, quatro inclusões e complemento.

## Parte 2 — precisão, fórmulas e explicação

`Fraction` guarda frações exatamente e as simplifica pelo máximo divisor comum: `6/3` vira `2`, e não uma aproximação `2.0`. Um `float` tem quantidade limitada de bits e alguns decimais não são representados exatamente; por isso ele não é usado nas decisões matemáticas.

Para `1,2(5)`, juntam-se os algarismos até uma repetição (`125`) e os algarismos antes do período (`12`). Há um algarismo não periódico e um no período, então o denominador é `10 × 9 = 90`:

```text
(125 − 12) / 90 = 113/90
```

Em geral, há tantos noves quanto algarismos no período e tantos zeros quanto algarismos não periódicos. A função própria `calcular_fracao_geratriz` monta numerador e denominador; `Fraction` apenas simplifica o resultado.

Para `√n`, com `n` inteiro não negativo, `math.isqrt` encontra a parte inteira da raiz. Se `raiz × raiz == n`, ela é exata e classificada como inteiro. Caso contrário, o teorema sobre raízes de inteiros não quadrados perfeitos garante que ela é irracional. Radicando negativo não pertence a R.

| Entrada | Interpretação/valor exato | Esperado | Obtido |
|---|---|---|---|
| 7 | 7 | N, Z, Q, R | N, Z, Q, R |
| -3 | -3 | Z, Q, R | Z, Q, R |
| 0 | 0 | N, Z, Q, R | N, Z, Q, R |
| 3/4 | 3/4 | Q, R | Q, R |
| -5/2 | -5/2 | Q, R | Q, R |
| 6/3 | 2 | N, Z, Q, R | N, Z, Q, R |
| 0,75 | 3/4 | Q, R | Q, R |
| 0,(3) | geratriz 1/3 | Q, R | Q, R |
| 2,(7) | geratriz 25/9 | Q, R | Q, R |
| 1,2(5) | geratriz 113/90 | Q, R | Q, R |
| 0,(9) | geratriz 1 | N, Z, Q, R | N, Z, Q, R |
| √9 | raiz exata 3 | N, Z, Q, R | N, Z, Q, R |
| √2 | raiz não exata | I, R | I, R |
| √(-4) | não é real | nenhum entre N,Z,Q,I,R | nenhum |

Também foram realmente testados: denominador zero, duas barras, decimal malformado, período vazio, parêntese incompleto, texto e entrada vazia; todos geram `ValueError` tratado pela interface. O bônus devolve os primos até 30 e os divisores de 36 indicados no PDF.

Trecho de execução real de uma dízima composta:

```text
Entrada: 1,2(5)
Tipo: dízima periódica composta
Interpretação: parte inteira=1, parte não periódica=2, período=5;
cálculo=(125 − 12)/90; geratriz simplificada=113/90
Pertence a: Q, R
Justificativa: Toda dízima periódica possui fração geratriz e é racional.
```

O programa apresenta `dízima periódica simples` quando não existe trecho não periódico, como em `0,(3)`, e `dízima periódica composta` quando esse trecho existe, como em `1,2(5)`.

### Como explicar a Parte 2 ao professor

O programa identifica primeiro o formato da entrada, em vez de classificá-la apenas pela aparência. Inteiros, decimais finitos, frações e dízimas tornam-se `Fraction`, que preserva o valor exato. Se o denominador simplificado é 1, o valor está em Z e, se não negativo, também em N. Todo `Fraction` está em Q e R. Uma dízima é racional porque sua repetição permite montar uma fração geratriz. Nas raízes inteiras, a igualdade `isqrt(n)² == n` separa raízes exatas de raízes irracionais. Os testes comparam cada conjunto identificado ao gabarito e verificam erros.

Limitações: a raiz aceita somente radicando inteiro; o programa não interpreta expressões algébricas, constantes como π, notação científica nem números complexos. Isso evita classificações sem prova dentro do escopo do enunciado.

## Parte 3 — recomendação por Jaccard

Para interesses A e B:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

Quanto mais próximo de 1, maior a afinidade. Se ambos forem vazios, adotamos afinidade 0 para evitar divisão por zero e não recomendar alguém sem evidência de interesse comum.

No exemplo do PDF: Ana×Bia tem `2/6 ≈ 0,33`; Ana×Caio, `2/5 = 0,40`; Bia×Caio, `1/6 ≈ 0,17`. Para Ana, Caio é recomendado.

| Cenário | Entrada | Cálculo esperado e obtido |
|---|---|---|
| Vários em comum | Ana e Caio | comuns={games,cinema}; união=5; J=0,40 |
| Nenhum em comum | {a} e {b} | interseção=∅; união=2; J=0 |
| Vazios/repetidos | ∅ e ∅; `rock,rock,ROCK` | J=0; interesses normalizados={rock} |
| Empate | alvo={a}; B={a,b}; C={a,c} | J=0,5 para B e C; ambos recomendados |

Conclusão dos cenários: as saídas efetivas coincidiram com os resultados esperados. O detalhamento da execução automatizada e do teste integrado está em `RESULTADOS_TESTES.md`.

Trecho da execução real para Ana:

```text
Ana × Bia: comuns={cinema, jazz}; |interseção|=2; |união|=6; J=0.33 (33.3%)
Ana × Caio: comuns={cinema, games}; |interseção|=2; |união|=5; J=0.40 (40.0%)
Maior afinidade: Caio
```

## Publicação no GitHub

Repositório do projeto: <https://github.com/sousarthuur/Laborat-rio-de-Conjuntos>

Para publicar novas alterações, use:

```powershell
git add .
git commit -m "Descrição da alteração"
git push
```

Não publique dados pessoais ou credenciais. A equipe deve gerar os próprios prints, se o professor preferir imagens aos logs registrados.

## Checklist final

- [x] Três partes e menu com retorno sem reiniciar.
- [x] Operações manuais da Parte 1 e conferência nativa separada.
- [x] Casos vazio, iguais, disjuntos, contido e repetidos.
- [x] Classificação exata de inteiros, frações, decimais, dízimas e raízes.
- [x] Geratrizes, inclusive 0,(9), períodos maiores, trecho não periódico e sinal negativo.
- [x] Crivo e divisores do bônus.
- [x] Recomendação Jaccard, cadastro, múltiplos usuários, empate e vazio.
- [x] Testes automatizados e resultado real registrado.
- [x] Relatório final de uma página.
- [x] Publicação no GitHub e logs finais registrados.
