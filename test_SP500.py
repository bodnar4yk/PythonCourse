import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm #for ex2.ex3
import time #fot ex.3

 
# 1. Download data S&P 500
ticker = "^GSPC"
start_date="1988-04-04"
end_date="2005-04-04"
data = yf.download(ticker, start=start_date,end=end_date)['Close']
close_values = data.to_numpy().flatten()
dt = 1/252  # Step time - 1 work day of year

# file_name = "SP500_Model_Results_Article.xlsx"

# with pd.ExcelWriter(file_name) as writer:
#     data.to_excel(writer, sheet_name='Historical_Data', index=False)

# print(f"Дані успішно збережено у файл: {file_name}")

# kappa=0.1
# mu=close_values.mean()
# sigma=close_values.std()

# expected_diff = kappa * (close_values[:-1] - mu) * dt

actual_diff = np.diff(close_values)


# file_name = "Diff_Article.xlsx"

# with pd.ExcelWriter(file_name) as writer:
#     actual_diff.to_excel(writer, sheet_name='diff', index=False)

# print(f"Дані успішно збережено у файл: {file_name}")

#     # Errors need to have distribution as N(0, sigma^2 * dt)
# residuals = actual_diff - expected_diff
# variance = (sigma**2) * dt
    
#     # Negative log likelihood
# ll = -0.5 * len(residuals) * np.log(2 * np.pi * variance) - 0.5 * np.sum(residuals**2) / variance
# print(ll)