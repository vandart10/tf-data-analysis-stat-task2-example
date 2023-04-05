import pandas as pd
import numpy as np

import scipy.stats as stats


chat_id = 710820274 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    N = len(x)
    T_2 = 77*77 / 2
    mean = np.mean(x)
    g1 = stats.gamma(N, 1).ppf(p/2)/N
    g2 = stats.gamma(N, 1).ppf(1-p/2)/N

    l = (g1 + mean) / T_2
    r = (g2 + mean) / T_2
    return (l, r)
