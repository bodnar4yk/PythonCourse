import numpy as np
import scipy.stats as stats
import time

# Exercise 3
kappa = 1.0
mu = 0.2
sigma = 0.5
x0 = 0.3
K = 0.3  # from condition K = x0
t0 = 0 # t0 = 0 
T = 1.0  # T = 1 
E = mu + (x0 - mu) * np.exp(kappa * (T - t0))
V = (sigma**2 / (2 * kappa)) * (np.exp(2 * kappa * (T - t0)) - 1)

print(f"E={E}",f"Var={V}")

d=(E - K) / np.sqrt(V)
m = (E - K) * stats.norm.cdf(d) + np.sqrt(V) * stats.norm.pdf(d)

print(f"m={m}")

start_time = time.time()

def run_monte_carlo(n, K, E, V):
    """Monte Carlo simulation and calculate a standard error of the estimate"""
    start_time = time.time()
        
    # Generation n values XT from normal distribution
    XT = np.random.normal(E, np.sqrt(V), n)
    end_time = time.time()
    
    # Calculate m_i = max(0, XT - K)
    mi = np.maximum(0, XT - K)
    
    m_hat = np.mean(mi)
    end_time = time.time()
    elapsed_m_hat = end_time - start_time
    # Calculate a standard error of the estimate as:
    # s(n) = sqrt( 1/(n*(n-1)) * sum( (mi - m_hat)^2 ) )
    sum_sq_diff = np.sum((mi - m_hat)**2)
    s_n = np.sqrt(sum_sq_diff / (n * (n - 1)))
    
    end_time = time.time()
    elapsed_s_n = end_time - start_time
    
    # 95% Confident level
    ci_low = m_hat - 1.96 * s_n
    ci_high = m_hat + 1.96 * s_n
    
    return m_hat, s_n, (ci_low, ci_high), elapsed_m_hat, elapsed_s_n


n_values = [1000, 1000000]

print(f"m (from ex.2): {m:.6f}\n")
print(f"{'n':>7} | {'m_hat':>10} | {'Std Error':>10} | {'95% CI':>25} | {'Time (m_hat)':>8}| {'Time (s_n)':>8}")
print("-" * 80)

for n in n_values:
    m_hat, s_n, ci, duration_m_hat, duration_s_n = run_monte_carlo(n, K, E, V)
    
    if ci[0] <= m <= ci[1]:
        is_inside = "True"
    else:
        is_inside = "False"

    
    if n==n_values[-1]:
        print(f"{n:7d} | {m_hat:10.6f} | {s_n:10.6f} | ({ci[0]:.5f}, {ci[1]:.5f}) | {duration_m_hat:8.4f}| {duration_s_n:8.4f}")
    else:
        print(f"{n:7d} | {m_hat:10.6f} | {s_n:10.6f} | ({ci[0]:.5f}, {ci[1]:.5f}) | {'-':8.4}| {'-':8.4}")
    
    print(f"   --> Does the 95% confidence interval include m? {is_inside}\n")

