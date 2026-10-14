# Resultados reais dos testes

Execução realizada em 13/10/2026 com Python 3.13.16, no Windows.

## Testes automatizados

Comando executado:

```powershell
python -m unittest -v testes.py
```

Saída efetiva:

```text
test_caso_geral_e_repetidos ... ok
test_complemento_e_pertinencia ... ok
test_vazio_iguais_disjuntos_e_contido ... ok
test_bonus ... ok
test_classificacoes_obrigatorias ... ok
test_geratrizes ... ok
test_invalidos ... ok
test_empate ... ok
test_exemplo_do_pdf ... ok
test_sem_comuns_vazios_e_repetidos ... ok

----------------------------------------------------------------------
Ran 10 tests

OK
```

Cada método pode conter vários subcasos. Por exemplo, `test_classificacoes_obrigatorias` verificou separadamente 14 entradas, e `test_invalidos` verificou 7 entradas inválidas.

## Teste integrado do menu

O `main.py` também foi executado com navegação pelas Partes 1, 2 e 3 e retorno ao menu principal. Na Parte 1 foram usados:

```text
A = 1, 2, 2
B = 2, 3
U = 1, 2, 3
elemento = 1
```

Trecho da saída efetiva:

```text
A = {1, 2}; |A| = 2
B = {2, 3}; |B| = 2
A ∪ B = {1, 2, 3}
A ∩ B = {2}
A − B = {1}
B − A = {3}
A Δ B = {1, 3}
Complemento de A em U = {3}
'1' ∈ A? True

Conferência com as operações nativas do Python:
- união: OK
- interseção: OK
- A - B: OK
- B - A: OK
- diferença simétrica: OK
- complemento: OK
```

O teste inicialmente detectou incompatibilidade do terminal CP-1252 com símbolos matemáticos. A saída dos módulos foi configurada como UTF-8 e a execução integrada seguinte terminou normalmente.

## Validação de sintaxe/importações

Comando executado:

```powershell
python -m py_compile main.py parte1_conjuntos.py parte2_numeros.py parte3_recomendacao.py testes.py
```

Resultado: concluído sem erros. Todos os módulos foram importados pelos testes.
