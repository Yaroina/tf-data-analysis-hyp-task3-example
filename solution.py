import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

    def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.07
    from scipy.stats import mannwhitneyu
    p = mannwhitneyu(x, y, alternative='greater')[1]
    return p < alpha
