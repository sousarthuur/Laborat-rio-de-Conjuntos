# Resultados reais dos testes e execuções

Execução final realizada em 13/10/2026 com Python 3.13.16, no Windows.

## Testes automatizados

Comando executado:

```powershell
python -m unittest -v testes.py
```

Saída efetiva:

```text
test_caso_geral_e_repetidos ... ok
test_complemento_e_pertinencia ... ok
test_todas_as_validacoes_nativas ... ok
test_vazio_iguais_disjuntos_e_contido ... ok
test_bonus ... ok
test_classificacoes_obrigatorias ... ok
test_geratrizes ... ok
test_invalidos ... ok
test_empate ... ok
test_exemplo_do_pdf ... ok
test_sem_comuns_vazios_e_repetidos ... ok

----------------------------------------------------------------------
Ran 11 tests

OK
```

Cada método contém vários subcasos. `test_classificacoes_obrigatorias` verifica 14 entradas, `test_invalidos` verifica 7 entradas inválidas e `test_todas_as_validacoes_nativas` compara todas as operações manuais da Parte 1 com os recursos nativos do Python.

## Execução integrada das três partes

O `main.py` foi executado navegando pelas Partes 1, 2 e 3 e retornando ao menu principal sem reiniciar o programa.

### Parte 1 — operações e validação

Entradas:

```text
A = 1, 2, 2, 3, 4
B = 3, 4, 5, 6
U = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Elemento = 3
Opção = 8 (mostrar e validar todas)
```

Trechos da saída efetiva:

```text
A ∪ B
  Resultado manual: {1, 2, 3, 4, 5, 6}
  Resultado nativo: {1, 2, 3, 4, 5, 6}
  Resultados iguais? True

A ∩ B
  Resultado manual: {3, 4}
  Resultado nativo: {3, 4}
  Resultados iguais? True

A Δ B
  Resultado manual: {1, 2, 5, 6}
  Resultado nativo: {1, 2, 5, 6}
  Resultados iguais? True

'3' ∈ A
  Resultado manual: True
  Resultado nativo: True
  Resultados iguais? True

Cardinalidade de A
  Resultado manual: 4
  Resultado nativo: 4
  Resultados iguais? True

Complemento de A em U
  Resultado manual: {5, 6, 7, 8, 9, 10}
  Resultado nativo: {5, 6, 7, 8, 9, 10}
  Resultados iguais? True
```

As diferenças A−B e B−A e as quatro verificações de inclusão também apresentaram `Resultados iguais? True`.

### Parte 2 — classificador numérico

Entrada escolhida: `1,2(5)`.

```text
Entrada: 1,2(5)
Tipo: dízima periódica composta
Interpretação: dízima periódica composta; parte inteira=1,
parte não periódica=2, período=5; cálculo=(125 − 12)/90;
geratriz simplificada=113/90
Pertence a: Q, R
Justificativa: Toda dízima periódica possui fração geratriz e é racional.
```

Além dessa execução, os testes automatizados conferem inteiros negativos, zero, frações positivas e negativas, decimal exato, fração aparente, dízimas simples e compostas, raiz exata, raiz irracional e raiz fora dos reais.

### Parte 3 — recomendação por Jaccard

Usuária escolhida: `Ana`.

```text
Ana × Bia: comuns={cinema, jazz}; |interseção|=2; |união|=6; J=0.33 (33.3%)
Ana × Caio: comuns={cinema, games}; |interseção|=2; |união|=5; J=0.40 (40.0%)
Maior afinidade: Caio
```

Os valores coincidem com os cálculos feitos à mão: 2/6 para Ana e Bia e 2/5 para Ana e Caio.

## Validação de sintaxe e importações

Comando executado:

```powershell
python -m py_compile main.py parte1_conjuntos.py parte2_numeros.py parte3_recomendacao.py testes.py
```

Resultado: concluído sem erros. Todos os módulos foram importados pelos testes.
