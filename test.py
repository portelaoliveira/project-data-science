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

from functions import *

# Importar base de dados
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

    year = file.name[-11:]
    year = int(year.replace(".csv.xz", ""))

    df = pd.read_csv(path_dataset / file.name, low_memory=False)
    df["ano"] = year
    df["mes"] = month

    data_base_airbnb = pd.concat([data_base_airbnb, df], ignore_index=True)

# Listar todas as colunas
# print(list(data_base_airbnb.columns))

# Tratamento dos dados
columns = [
    "host_response_time",
    "host_response_rate",
    "host_is_superhost",
    "host_listings_count",
    "latitude",
    "longitude",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "bed_type",
    "amenities",
    "price",
    "security_deposit",
    "cleaning_fee",
    "guests_included",
    "extra_people",
    "minimum_nights",
    "maximum_nights",
    "number_of_reviews",
    "review_scores_rating",
    "review_scores_accuracy",
    "review_scores_cleanliness",
    "review_scores_checkin",
    "review_scores_communication",
    "review_scores_location",
    "review_scores_value",
    "instant_bookable",
    "is_business_travel_ready",
    "cancellation_policy",
    "ano",
    "mes",
]

data_base_airbnb = data_base_airbnb.loc[:, columns]
# print(list(data_base_airbnb.columns))

# Tratar valores faltantes
for columns in data_base_airbnb:
    if data_base_airbnb[columns].isnull().sum() > 300000:
        data_base_airbnb = data_base_airbnb.drop(columns, axis=1)
# print(data_base_airbnb.isnull().sum())

# Excluir linhas vazias
# data_base_airbnb = data_base_airbnb.dropna()
# print(data_base_airbnb.shape)
# print(data_base_airbnb.isnull().sum())

# Verificar tipos de dados em cada coluna
# print(data_base_airbnb.dtypes)
# print("-" * 60)
# print(data_base_airbnb.iloc[0])

# Como preço e extra people estão sendo reconhecidos como objeto (ao invés de ser um float) temos que mudar o tipo de variável da coluna.
# price
data_base_airbnb["price"] = data_base_airbnb["price"].str.replace("$", "")
data_base_airbnb["price"] = data_base_airbnb["price"].str.replace(",", "")
data_base_airbnb["price"] = data_base_airbnb["price"].astype(
    np.float32, copy=False
)
# extra people
data_base_airbnb["extra_people"] = data_base_airbnb[
    "extra_people"
].str.replace("$", "")
data_base_airbnb["extra_people"] = data_base_airbnb[
    "extra_people"
].str.replace(",", "")
data_base_airbnb["extra_people"] = data_base_airbnb["extra_people"].astype(
    np.float32, copy=False
)
# verificando os tipos
# print(data_base_airbnb.dtypes)

# Analisar correlação entre as colunas

heatmap_corr(data_base_airbnb)

# Outliers das colunas

# Price
box_diagram(data_base_airbnb["price"], "box_diagram_price")
histogram(data_base_airbnb["price"], "histogram_price")

data_base_airbnb, excludes_lines = exclude_outliers(data_base_airbnb, "price")
print("{} linhas removidas".format(excludes_lines))

histogram(data_base_airbnb["price"], "histogram_price_exclude_outliers")
print(data_base_airbnb.shape)

# Extra People
box_diagram(data_base_airbnb["extra_people"], "box_diagram_extra_people")
histogram(data_base_airbnb["extra_people"], "histogram_extra_people")

data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "extra_people"
)
print("{} linhas removidas".format(excludes_lines))

histogram(
    data_base_airbnb["extra_people"], "histogram_extra_people_exclude_outliers"
)
print(data_base_airbnb.shape)

# Host Listings Count
box_diagram(
    data_base_airbnb["host_listings_count"], "box_diagram_host_listings_count"
)
bar_graph(
    data_base_airbnb["host_listings_count"], "bar_graph_host_listings_count"
)

data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "host_listings_count"
)
print("{} linhas removidas".format(excludes_lines))

# Accommodates
box_diagram(data_base_airbnb["accommodates"], "box_diagram_accommodates")
bar_graph(data_base_airbnb["accommodates"], "bar_graph_accommodates")

data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "accommodates"
)
print("{} linhas removidas".format(excludes_lines))

# Bathrooms
box_diagram(data_base_airbnb["bathrooms"], "box_diagram_bathrooms")
# bar_graph(data_base_airbnb["bathrooms"], "bar_graph_bathrooms")

plt.figure(figsize=(15, 5))
sns.barplot(
    x=data_base_airbnb["bathrooms"].value_counts().index,
    y=data_base_airbnb["bathrooms"].value_counts(),
)
plt.savefig(f"imgs/bar_graph_bathrooms.png")
data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "bathrooms"
)
print("{} linhas removidas".format(excludes_lines))

# Bedrooms
box_diagram(data_base_airbnb["bedrooms"], "box_diagram_bedrooms")
bar_graph(data_base_airbnb["bedrooms"], "bar_graph_bedrooms")

data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "bedrooms"
)
print("{} linhas removidas".format(excludes_lines))

# Beds
box_diagram(data_base_airbnb["beds"], "box_diagram_beds")
bar_graph(data_base_airbnb["beds"], "bar_graph_beds")

data_base_airbnb, excludes_lines = exclude_outliers(data_base_airbnb, "beds")
print("{} linhas removidas".format(excludes_lines))

# Guests Included
plt.figure(figsize=(15, 5))
sns.barplot(
    x=data_base_airbnb["guests_included"].value_counts().index,
    y=data_base_airbnb["guests_included"].value_counts(),
)
plt.savefig(f"imgs/guests_included.png")
data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "guests_included"
)
print("{} linhas removidas".format(excludes_lines))

data_base_airbnb = data_base_airbnb.drop("guests_included", axis=1)
print(data_base_airbnb.shape)

# Minimum Nights
box_diagram(data_base_airbnb["minimum_nights"], "box_diagram_minimum_nights")
bar_graph(data_base_airbnb["minimum_nights"], "bar_graph_minimum_nights")

data_base_airbnb, excludes_lines = exclude_outliers(
    data_base_airbnb, "minimum_nights"
)
print("{} linhas removidas".format(excludes_lines))

# Maximum Nights
box_diagram(data_base_airbnb["maximum_nights"], "box_diagram_maximum_nights")
bar_graph(data_base_airbnb["maximum_nights"], "bar_graph_maximum_nights")

data_base_airbnb = data_base_airbnb.drop("maximum_nights", axis=1)
print(data_base_airbnb.shape)

# Number of Reviews
box_diagram(
    data_base_airbnb["number_of_reviews"], "box_diagram_number_of_reviews"
)
bar_graph(data_base_airbnb["number_of_reviews"], "bar_graph_number_of_reviews")

data_base_airbnb = data_base_airbnb.drop("number_of_reviews", axis=1)
print(data_base_airbnb.shape)

# Tratamento de Colunas de Valores de Texto
# Property Type

print(data_base_airbnb["property_type"].value_counts())

plt.figure(figsize=(20, 18))
graph = sns.countplot(x=data_base_airbnb["property_type"])
graph.tick_params(axis="x", rotation=90)
plt.savefig(f"imgs/bar_graph_property_type.png")

table_types_house = data_base_airbnb["property_type"].value_counts()
columns_groupy = []

for type in table_types_house.index:
    if table_types_house[type] < 2000:
        columns_groupy.append(type)
print(columns_groupy)

for type in columns_groupy:
    data_base_airbnb.loc[
        data_base_airbnb["property_type"] == type, "property_type"
    ] = "Outros"

print(data_base_airbnb["property_type"].value_counts())
plt.figure(figsize=(20, 16))
graph_filt = sns.countplot(x=data_base_airbnb["property_type"])
graph_filt.tick_params(axis="x", rotation=90)
plt.savefig(f"imgs/bar_filt_graph_property_type.png")

# Room Type
print(data_base_airbnb["room_type"].value_counts())
plt.figure(figsize=(18, 16))
graph_filt = sns.countplot(x=data_base_airbnb["room_type"])
graph_filt.tick_params(axis="x", rotation=90)
plt.savefig(f"imgs/bar_graph_room_type.png")
