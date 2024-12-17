import numpy as np
import pandas as pd

def generate_synthetic_data(data, n_samples=500):
    synthetic_data = data.sample(n=n_samples, replace=True).reset_index(drop=True)
    noise = np.random.normal(0, 0.1, synthetic_data.shape[0]) * synthetic_data['sales']
    synthetic_data['sales'] += noise
    return synthetic_data
