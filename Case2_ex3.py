import numpy as np
import time
from scipy.stats import norm

# 1. Використовуємо ОДНАКОВІ параметри для обох методів
kappa_test, mu_test, sigma_test = 1.0, 0.2, 0.5 # Параметри з умови вправи
x0_test = 0.3
K_test = 0.3
T_0=0  ## Врахувати
T_test = 1.0

# # 2. Calucate m (price option) for new T
# Evaluate for new T_horizon 1 year
E_XT = mu_test + (x0_test - mu_test) * np.exp(kappa_test * T_test)
Var_XT = (sigma_test**2 / (2 * kappa_test)) * (np.exp(2 * kappa_test * T_test) - 1)
Std_XT = np.sqrt(Var_XT)
d_test = (E_XT - K_test) / Std_XT
m_analytical_consistent = (E_XT - K_test) * norm.cdf(d_test) + Std_XT * norm.pdf(d_test)


def run_monte_carlo_fixed(n, m_true, k, m, s, x_init, strike, time_t):
    start_time = time.time()
    
    # Simulation
    epsilon = np.random.normal(0, 1, n)
    std_sim = s * np.sqrt((np.exp(2 * k * time_t)-1) / (2 * k))
    exp_sim = m + (x_init - m) * np.exp(k * time_t)
    XT = exp_sim + std_sim * epsilon
    
    m_i = np.maximum(0, XT - strike)
    m_hat = np.mean(m_i)
    
    # Standard deviation
    std_error = np.sqrt(np.sum((m_i - m_hat)**2) / (n * (n - 1)))
    
    ci = [m_hat - 1.96 * std_error, m_hat + 1.96 * std_error]
    is_inside = ci[0] <= m_true <= ci[1]
    
    print(f"n={n:7} | m_hat={m_hat:.5f} | CI=[{ci[0]:.5f}, {ci[1]:.5f}] | inside range? {is_inside}")

# Launch
print(f"Calculated m_analytical: {m_analytical_consistent:.5f}")
for n in [1000, 100000]:
    run_monte_carlo_fixed(n, m_analytical_consistent, kappa_test, mu_test, sigma_test, x0_test, K_test, T_test)

