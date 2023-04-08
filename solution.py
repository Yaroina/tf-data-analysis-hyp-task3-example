import pandas as pd
import numpy as np


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

    def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.07
    
    pval = stats.ttest_ind(x, y).pvalue
    if pval < alpha:
      res = True
    else:
      res = False    
    return res 
