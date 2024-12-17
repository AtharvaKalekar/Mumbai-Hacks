import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.demand_forecast import build_linear_regression_model
from src.synthetic_data import generate_synthetic_data
from src.inventory_optimization import optimize_inventory

def load_data():
    # Load preprocessed data or generated data here
    data = pd.read_csv('data/sales_data.csv')
    return data

def display_dashboard(data):
    st.title("Inventory Management Dashboard")

    # Forecast demand
    model, predictions = build_linear_regression_model(data)
    data['predicted_demand'] = predictions

    # Generate synthetic data
    synthetic_data = generate_synthetic_data(data)
    st.write("Synthetic Data Sample", synthetic_data.head())

    # Inventory Optimization
    reorder_points = optimize_inventory(predictions)
    data['reorder_points'] = reorder_points

    # Visualizations
    st.line_chart(data['predicted_demand'])
    st.write("Reorder Points", data[['date', 'reorder_points']])

    plt.hist(synthetic_data['sales'], bins=30, alpha=0.7, label="Synthetic Sales")
    plt.legend()
    st.pyplot(plt)

if __name__ == "__main__":
    data = load_data()
    display_dashboard(data)
