# Relatório — Laboratório de Conjuntos

## Objetivo e aplicação da teoria

O projeto aplica a Teoria dos Conjuntos e os Conjuntos Numéricos em três programas integrados por um menu principal. Foi utilizada a linguagem Python 3 e somente módulos da biblioteca padrão. A organização em arquivos separados deixa cada parte independente, facilita os testes e torna o código mais simples de explicar.

Na Parte 1, cada operação de conjuntos foi transformada em um algoritmo. A pertinência percorre uma lista e compara seus elementos um por um. A união reúne os elementos de A e B sem repetições; a interseção guarda somente elementos presentes nos dois conjuntos; a diferença seleciona elementos do primeiro conjunto ausentes do segundo; e a diferença simétrica reúne as duas diferenças. A inclusão verifica se todos os elementos do primeiro conjunto aparecem no segundo. A cardinalidade é obtida por contagem e o complemento corresponde a U − A. Todas essas operações são calculadas com laços e condicionais, sem operadores prontos de conjuntos. Somente depois do resultado manual, o programa usa `set` e operadores nativos para conferir união, interseção, diferenças, pertinência, inclusões, cardinalidades e complemento.

Na Parte 2, a inclusão entre conjuntos numéricos fundamenta a classificação. Foi adotada a convenção N = {0, 1, 2, ...}; assim, todo natural também é inteiro, racional e real. Frações e decimais são representados por `Fraction`, evitando aproximações. Nas dízimas periódicas, o programa separa parte inteira, trecho não periódico e período, identifica se a dízima é simples ou composta e calcula a fração geratriz. Por exemplo, em 1,2(5), o cálculo é (125 − 12)/90 = 113/90. Nas raízes, `isqrt` verifica se o radicando é quadrado perfeito: √9 é natural, inteiro, racional e real, enquanto √2 é irracional e real. O bônus implementa o crivo de Eratóstenes e a listagem de divisores.

Na Parte 3, os interesses dos usuários são representados por conjuntos. A afinidade é calculada pelo índice de Jaccard, J(A,B) = |A ∩ B| / |A ∪ B|. A interseção representa interesses comuns e a união representa todos os interesses diferentes do par. O maior índice determina a recomendação, e o programa preserva empates.

## Maior desafio e justificativa

O conceito mais difícil foi a fração geratriz de dízimas periódicas compostas. Foi necessário interpretar corretamente o texto, distinguir o trecho que não se repete do período, construir numerador e denominador, tratar números negativos e simplificar o resultado sem usar aproximações. Casos como 0,(9), cujo resultado é exatamente 1, também exigiram cuidado para que a classificação final fosse feita pelo valor simplificado.

## Validação

Os testes automatizados cobrem conjuntos vazios, iguais, disjuntos, contidos e entradas repetidas; classificações de inteiros, frações, decimais, dízimas e raízes; entradas inválidas; primos, divisores e cenários de recomendação com afinidade, ausência de interesses comuns e empate. Além dos testes unitários, as três interfaces foram executadas e seus logs foram registrados no repositório.
