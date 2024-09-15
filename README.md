# Comparação de Algoritmos: Corte de Barras (Iterativo vs. Memoização)
## Descrição
Este projeto visa comparar duas abordagens diferentes para resolver o problema do corte de barras: um algoritmo iterativo e um algoritmo recursivo com memoização. O objetivo principal é avaliar o desempenho de ambos em termos de tempo de execução enquanto maximizam o lucro obtido com o corte de uma barra em diferentes comprimentos.

O problema do corte de barras consiste em determinar a melhor forma de cortar uma barra de comprimento n, de modo que o lucro seja maximizado. Cada corte tem um preço associado, e a barra pode ser cortada em pedaços de tamanhos variados.

## Algoritmos Implementados
- Algoritmo Iterativo: Resolve o problema de corte de barras utilizando uma abordagem bottom-up. Ele calcula o valor máximo possível para cada tamanho de barra de forma iterativa, começando pelos tamanhos menores.

- Algoritmo com Memoização: Este é um algoritmo recursivo que utiliza a técnica de memoização para armazenar soluções de subproblemas já resolvidos, evitando recomputações desnecessárias. Isso melhora a eficiência em relação à solução recursiva pura.

## Estrutura dos Arquivos
- comparation.py: Arquivo principal que executa os experimentos e mede o tempo de execução dos algoritmos iterativo e de memoização para barras de tamanhos diferentes.
- iterative.py: Contém a implementação da solução iterativa.
- memoization.py: Contém a implementação da solução recursiva com memoização.
- inputs/: Diretório onde são armazenados os vetores de preços gerados aleatoriamente.
- results_memo/: Resultados da execução do algoritmo com memoização.
- results_iter/: Resultados da execução do algoritmo iterativo.
- graphic/: Diretório para salvar os gráficos de comparação de tempo de execução.

## Resultados
Os resultados mostram o tempo de execução para barras de tamanhos diferentes, permitindo uma análise comparativa entre os dois algoritmos. O gráfico gerado ilustra a eficiência de cada abordagem à medida que o tamanho da barra aumenta. Abaixo segue alguns exemplos
- Barra com o tamanho máximo de 10.
- Vetor de preços: [24, 24, 60, 99, 128, 148, 240, 320, 384, 637]
  ![image](https://github.com/user-attachments/assets/889c5e7e-daac-41f3-ba4d-ce4ac842e374)

- Barra com o tamanho máximo de 20.
- Vetor de preços: [32, 36, 84, 130, 136, 192, 208, 225, 296, 336, 352, 420, 527, 630, 860, 936, 945, 1273, 1584, 1800]
![image](https://github.com/user-attachments/assets/d0ba9771-7fa2-4637-9d64-da6949aceeec)
