import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')

ECOMMERCE_PATH = os.path.join(DATA_DIR, 'eCommerce_Dataset.csv')
EVENTS_PATH = os.path.join(DATA_DIR, 'events.csv')
AMAZON_PATH = os.path.join(DATA_DIR, 'Musical_instruments_reviews.csv')
INSTACART_DIR = os.path.join(DATA_DIR, 'Instacart')

# Estilo global de plots 
def set_plot_style():
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams['figure.figsize'] = (12, 5)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12

# Guardar figuras 
def save_fig(filename):
    path = os.path.join(OUTPUTS_DIR, filename)
    plt.savefig(path, bbox_inches='tight', dpi=150)
    print(f"Figura guardada: {path}")