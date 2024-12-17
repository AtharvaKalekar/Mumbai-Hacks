import numpy as np
import pandas as pd

def optimize_inventory(predictions, safety_stock=0.2):
    # Calculate reorder point based on forecasted demand and safety stock
    reorder_points = predictions + (safety_stock * np.std(predictions))
    return reorder_points
