import pandas as pd
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split

months = {
    "jan": 1,
    "fev": 2,
    "mar": 3,
    "abr": 4,
    "mai": 5,
    "jun": 6,
    "jul": 7,
    "ago": 8,
    "set": 9,
    "out": 10,
    "nov": 11,
    "dez": 12,
}

path_dataset = Path("dataset")

data_base_airbnb = pd.DataFrame()

for file in path_dataset.iterdir():
    month_name = file.name[:3]
    month = months[month_name]

    year = file.name[-8:]
    year = int(year.replace(".csv.xz", ""))

    df = pd.read_csv(path_dataset / file.name, low_memory=False)
    df["ano"] = year
    df["mes"] = month

    data_base_airbnb = pd.concat([df, data_base_airbnb], ignore_index=True)


print(data_base_airbnb)
