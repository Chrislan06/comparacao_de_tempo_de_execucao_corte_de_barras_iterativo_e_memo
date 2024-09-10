import time
import random
import matplotlib.pyplot as plt
import sys
from iterative import rod_cut_iterative
from memoization import rod_cut_memoization

# Função para medir o tempo de execução
def measure_time(func, prices, n):
    start_time = time.perf_counter_ns()
    max_profit, cuts = func(prices, n)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    return elapsed_time, max_profit, cuts

# Salva os dos cortes de barras em um arquivo
def save_results_to_file(filename, size, max_profit, cuts, execution_time):
    with open(filename, 'a') as file:
        file.write('=====================================\n')
        file.write(f"Tamanho da barra: {size}\n")
        file.write(f"Lucro máximo: {max_profit}\n")
        file.write(f'Tempo de execução: {execution_time} ns\n')
        file.write("Cortes: " + ", ".join(map(str, cuts)) + "\n")
        file.write('=====================================\n')

# Função para gerar vetores de preços aleatórios
def generate_random_prices(size, min=1, max=100):
    prices = [0] * size
    prices[0] = random.randint(1, max)
    for i in  range(1, size):
        prices[i] = prices[i-1] + random.randint(min, max)
    return prices

# Função para realizar os experimentos e medir os tempos de execução
def run_experiments(size, num_experiments):
    memoized_times = []
    iterative_times = []
    # Tamanho inicial de corte de barra e intervalos para cada corte
    interval = int(size / num_experiments)
    inicial_size = interval
    # Geração de preços aleatórios
    prices = generate_random_prices(size=size)
    lengths = [] # Vetor para pegar o tamanho de barras testados
    for rod_size in range(inicial_size, size+1, interval):
        lengths.append(rod_size)
        # Medição do tempo de execução para a solução com memoização
        time_memo, max_profit, cuts = measure_time(rod_cut_memoization, prices, rod_size)
        # Salvando resultados
        save_results_to_file(f'results_memo/rod_{size}.txt', rod_size, max_profit, cuts, time_memo)

        # Medição do tempo de execução para a solução iterativa
        time_iter, max_profit, cuts = measure_time(rod_cut_iterative, prices, rod_size)
        # Salvando resultados
        save_results_to_file(f'results_iter/rod_{size}.txt', rod_size, max_profit, cuts, time_iter)


        # Calculando Média do tempo de execução de tamanho n para m interações diferentes
        memoized_times.append(time_memo)
        iterative_times.append(time_iter)

    return lengths, memoized_times, iterative_times

# Parâmetros para os experimentos
sizes = [10, 20, 50, 100, 1000, 2500, 5000, 10000]  # Comprimentos máximo de barras para cada teste
num_experiments = 10  # Número de experimentos por tamanho de barra

# Aumentado o número de chamadas recursivas para o máximo possível
n = len(sizes)
sys.setrecursionlimit((sizes[n-1]**2))

# Executar os experimentos
for size in sizes:
    with open(f'results_memo/rod_{size}.txt', 'w') as file:
        pass
    with open(f'results_iter/rod_{size}.txt', 'w') as file:
        pass
    lengths, memoized_times, iterative_times = run_experiments(size, num_experiments)
    # Plota os resultados
    plt.plot(lengths, memoized_times, label='Recursiva com Memoização')
    plt.plot(lengths, iterative_times, label='Iterativa')
    plt.xlabel('Comprimento da Barra')
    plt.ylabel('Tempo de Execução (em nanossegundos)')
    plt.title('Comparação de Tempo de Execução para o Problema de Corte de Barras')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'graphic/rod_size_max_{size}')
    plt.clf()