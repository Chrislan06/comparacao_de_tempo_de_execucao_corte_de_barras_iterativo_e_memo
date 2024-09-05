import time
import random
import matplotlib.pyplot as plt
import sys
from iterative import rod_cut_iterative
from memoization import rod_cut_memoization
import os

# Função para medir o tempo de execução
def measure_time(func, prices, n):
    start_time = time.time()
    max_profit, cuts = func(prices, n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, max_profit, cuts

# Salva os dos cortes de barras em um arquivo
def save_results_to_file(filename, length, i, max_profit, cuts):
    with open(filename, 'a') as file:
        file.write(f"Tamanho da barra:{length}\n")
        file.write(f"Interação: {i+1}\n")
        file.write(f"Lucro máximo: {max_profit}\n")
        file.write("Cortes: " + ", ".join(map(str, cuts)) + "\n")

# Função para gerar vetores de preços aleatórios
def generate_random_prices(size, min=1, max=100):
    prices = [0] * size
    prices[0] = random.randint(min, max)
    for i in  range(1, size):
        prices[i] = prices[i-1] + random.randint(min, max)
    return prices

# Função para realizar os experimentos e medir os tempos de execução
def run_experiments(lengths, num_experiments):
    memoized_times = []
    iterative_times = []
    os.remove('results_iterative.txt')
    os.remove('results_memo.txt')
    for length in lengths:
        time_memo_total = 0
        time_iterative_total = 0

        for i in range(num_experiments):
            # Geração de preços aleatórios
            prices = generate_random_prices(size=length)
            
            # Medição do tempo de execução para a solução com memoização
            time_memo, max_profit, cuts = measure_time(rod_cut_memoization, prices, length)
            time_memo_total += time_memo
            # Salvando resultados
            save_results_to_file('results_memo.txt', length, i, max_profit, cuts)


            # Medição do tempo de execução para a solução iterativa
            time_iterative, max_profit, cuts = measure_time(rod_cut_iterative, prices, length)
            time_iterative_total += time_iterative
            # Salvando resultados
            save_results_to_file('results_iterative.txt', length, i, max_profit, cuts)



        # Calculando Média do tempo de execução de tamanho n para m interações diferentes
        memoized_times.append(time_memo_total / num_experiments)
        iterative_times.append(time_iterative_total / num_experiments)

    return memoized_times, iterative_times

# Parâmetros para os experimentos
lengths = [10, 20, 50, 100, 1000, 2500, 5000, 10000]  # Comprimentos máximo de barras para cada teste
num_experiments = 10  # Número de experimentos por tamanho de barra

# Aumentado o número de chamadas recursivas para o máximo possível
n = len(lengths)
sys.setrecursionlimit(lengths[n-1]**2)

# Executar os experimentos
memoized_times, iterative_times = run_experiments(lengths, num_experiments)

# Plotar os resultados
# plt.plot(lengths, memoized_times, label='Recursiva com Memoização')
# plt.plot(lengths, iterative_times, label='Iterativa')
# plt.xlabel('Comprimento da Barra')
# plt.ylabel('Tempo Médio de Execução (segundos)')
# plt.title('Comparação de Tempo de Execução para o Problema de Corte de Barras')
# plt.legend()
# plt.grid(True)
# plt.show()