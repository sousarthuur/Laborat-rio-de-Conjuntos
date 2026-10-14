# Resultados dos testes

Testamos as três partes do programa no Windows com Python 3.13.16. Todos os testes passaram.

## Testes automáticos

Comando usado:

```powershell
python -m unittest -v testes.py
```

Resultado:

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
test_recomendacao_principal ... ok
test_sem_comuns_vazios_e_repetidos ... ok

Ran 11 tests
OK
```

## Parte 1

Usamos os conjuntos:

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

Trecho da saída:

```text
A ∪ B
  Resultado manual: {1, 2, 3, 4, 5, 6}
  Resultado nativo: {1, 2, 3, 4, 5, 6}
  Resultados iguais? True

A ∩ B
  Resultado manual: {3, 4}
  Resultado nativo: {3, 4}
  Resultados iguais? True

Complemento de A em U
  Resultado manual: {5, 6, 7, 8, 9, 10}
  Resultado nativo: {5, 6, 7, 8, 9, 10}
  Resultados iguais? True
```

As outras operações também deram o mesmo resultado nas versões manual e nativa.

## Parte 2

Entrada escolhida: `1,2(5)`.

```text
Tipo: dízima periódica composta
Fração geratriz: 113/90
Pertence a: Q, R
```

Também testamos inteiros, zero, frações positivas e negativas, decimal exato, dízima simples, raiz exata, raiz irracional e entradas inválidas.

## Parte 3

```text
Ana × Bia: J=0.33
Ana × Caio: J=0.40
Maior afinidade: Caio
```

Também testamos pessoas sem interesses em comum, conjuntos vazios, interesses repetidos e empate.

## Conferência final

Todos os arquivos Python foram verificados e não apresentaram erros de sintaxe ou importação.
