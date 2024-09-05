def rod_cut_iterative(prices, n):
    """
    Solução Iterativa para o problema de corte de barras.
    :param prices: Lista de preços para cada comprimento de barra.
    :param n: Comprimento da barra.
    :return: Valor máximo obtido.
    """
    values = [0] * n
    best_cuts = [0] * n
    values[0] = prices[0]
    best_cuts[0] = 1
    for i in range(1, n):
        max_value = prices[i]
        best_cut = i+1
        for j in range(i):
            value = prices[j] + values[i - j - 1]
            if value > max_value:
                max_value = value
                best_cut = j+1
        best_cuts[i] = best_cut
        values[i] = max_value
    
    max_profit = values[n-1]
    k = n 
    cuts = []
    while k > 0:
        cuts.append(best_cuts[k-1])
        k = k - best_cuts[k-1]
    
    return max_profit, cuts
