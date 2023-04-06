import pandas as pd
import numpy as np

import scipy.stats as stats


chat_id = 710820274 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    N = len(x)
    T_2 = 77*77 / 2
    mean = np.mean(x)
    er = stats.erlang(N, 1)
    g1 = er.ppf((1-p)/2)/N
    g2 = er.ppf((1+p)/2)/N
    l = (1*g1+g1 + mean-1/2) / T_2
    r = (1*g1+g2 + mean-1/2) / T_2
    return l, r
