import pandas as pd
import numpy as np

import scipy.stats as stats


chat_id = 710820274 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    N = len(x)
    T_2 = 77*77 / 2
    mean = np.mean(x)

    g1 = stats.erlang.ppf(p / 2, N, loc=0, scale=1/N)
    g2 = stats.erlang.ppf(1 - p / 2, N, loc=0, scale=1/N)

    l = (g1 + mean - 1/2) / T_2
    r = (g2 + mean - 1/2) / T_2
    return l, r
