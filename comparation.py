import time
import random
import matplotlib.pyplot as plt

# Definição dos algoritmos

def rod_cut_memoization(prices, n):
    """
    Solução Recursiva com Memoização para o problema de corte de barras.
    :param prices: Lista de preços para cada comprimento de barra.
    :param n: Comprimento da barra.
    :return: Valor máximo obtido.
    """
    
    memo = [0] * n 

    def _cut_rod_recursive(n):
        if memo[n-1]:
            return memo[n-1]
        
        if n == 1:
            memo[0] = prices[0]
            return memo[0]
        
        max_value = prices[n-1]
        for i in range(1,n):
            max_value = max(max_value, prices[i-1] + _cut_rod_recursive(n - i))
        
        memo[n-1] = max_value
        print(memo)
        return max_value

    return _cut_rod_recursive(n)

def rod_cut_iterative(prices, n):
    """
    Solução Iterativa para o problema de corte de barras.
    :param prices: Lista de preços para cada comprimento de barra.
    :param n: Comprimento da barra.
    :return: Valor máximo obtido.
    """
    values = [0] * n
    values[0] = prices[0]
    for i in range(1, n):
        max_value = prices[i]
        for j in range(i):
            max_value = max(max_value, prices[j] + values[i - j - 1])
        values[i] = max_value
    
    return values[n-1]


# Função para gerar vetores de preços aleatórios
def generate_random_prices(size, min=1, max=100):
    prices = [0] * size
    prices[0] = random.randint(min, max)
    for i in  range(1, size):
        prices[i] = prices[i-1] + random.randint(min, max)
    return prices

# Função para realizar os experimentos e medir os tempos de execução
def run_experiments(max_length, num_experiments):
    memoized_times = []
    iterative_times = []
    lengths = list(range(1, max_length + 1))
    
    for length in lengths:
        # Geração de preços aleatórios
        prices = [random.randint(1, 100) for _ in range(length)]
        
        # Medição do tempo de execução para a solução com memoização
        memoized_start = time.time()
        for _ in range(num_experiments):
            rod_cut_memoization(prices, length)
        memoized_end = time.time()
        memoized_avg_time = (memoized_end - memoized_start) / num_experiments
        memoized_times.append(memoized_avg_time)
        
        # Medição do tempo de execução para a solução iterativa
        iterative_start = time.time()
        for _ in range(num_experiments):
            rod_cut_iterative(prices, length)
        iterative_end = time.time()
        iterative_avg_time = (iterative_end - iterative_start) / num_experiments
        iterative_times.append(iterative_avg_time)
    
    return lengths, memoized_times, iterative_times

# Parâmetros para os experimentos
max_length = 20  # Comprimento máximo da barra
num_experiments = 100  # Número de experimentos por tamanho de barra

# Executar os experimentos
lengths, memoized_times, iterative_times = run_experiments(max_length, num_experiments)

# Plotar os resultados
plt.plot(lengths, memoized_times, label='Recursiva com Memoização')
plt.plot(lengths, iterative_times, label='Iterativa')
plt.xlabel('Comprimento da Barra')
plt.ylabel('Tempo Médio de Execução (segundos)')
plt.title('Comparação de Tempo de Execução para o Problema de Corte de Barras')
plt.legend()
plt.grid(True)
plt.show()
# Comentario