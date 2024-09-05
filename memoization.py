def rod_cut_memoization(prices, n):
    """
    Solução Recursiva com Memoização para o problema de corte de barras.
    :param prices: Lista de preços para cada comprimento de barra.
    :param n: Comprimento da barra.
    :return: Valor máximo obtido.
    """
    
    memo = [0] * n 
    best_cuts = [0] * n
    
    def _cut_rod_recursive(n):
        if memo[n-1]:
            return memo[n-1]
        
        if n == 1:
            best_cuts[0] = 1
            memo[0] = prices[0]
            return memo[0]
        
        max_value = prices[n-1]
        best_cut = n 
        for i in range(1,n):
            value = prices[i-1] + _cut_rod_recursive(n - i)
            if value > max_value:
                max_value = value
                best_cut = i
        best_cuts[n-1] = best_cut
        memo[n-1] = max_value
        return max_value

    max_profit = _cut_rod_recursive(n)
    i = n 
    cuts = []
    while i > 0:
        cuts.append(best_cuts[i-1])
        i -= best_cuts[i-1]
    
    return max_profit, cuts

