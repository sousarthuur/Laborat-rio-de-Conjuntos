# Modelo de relatório acadêmico — Laboratório de Conjuntos

> Revise, inclua os nomes da equipe e adapte este texto antes da entrega. Ele é um modelo e não atribui experiências pessoais aos integrantes.

## Objetivo e tecnologias

O projeto teve como objetivo aplicar a teoria dos conjuntos e dos conjuntos numéricos em problemas de programação. Foi utilizada a linguagem Python 3 e apenas módulos da biblioteca padrão, como `fractions`, `math`, `re` e `unittest`.

## Desenvolvimento

Na Parte 1, foram implementadas manualmente união, interseção, diferenças, diferença simétrica, pertinência, inclusão, cardinalidade e complemento. Laços e condicionais fazem as operações, enquanto o tipo `set` aparece depois apenas para conferir os resultados.

Na Parte 2, o classificador interpreta inteiros, frações, decimais exatos, dízimas periódicas e raízes quadradas de inteiros. Frações são mantidas de forma exata. Na dízima, os blocos numéricos são subtraídos e divididos por um denominador formado por noves e zeros; depois a fração é simplificada. Nas raízes, `isqrt` verifica quadrados perfeitos sem depender de aproximações. O bônus implementa o crivo de Eratóstenes e a listagem de divisores.

Na Parte 3, a teoria aparece nos conjuntos de interesses. Para cada par de usuários, a afinidade é calculada pelo índice de Jaccard: tamanho da interseção dividido pelo tamanho da união. A maior pontuação gera a recomendação e pontuações iguais são tratadas como empate.

## Desafio e testes

Uma possível resposta para “qual foi a operação mais difícil?” é a fração geratriz, pois é necessário separar parte inteira, trecho não periódico e período, construir corretamente numerador e denominador e ainda tratar sinais e entradas inválidas. A equipe deve substituir esta sugestão pela própria avaliação.

Os testes automatizados cobrem casos gerais e de borda: conjuntos vazios, iguais e disjuntos, repetições, classificações fornecidas no enunciado, entradas inválidas, recomendações com e sem interesses comuns e empate. O comando e o resultado real da execução estão registrados no README.
