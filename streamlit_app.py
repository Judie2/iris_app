import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


#Charger le fichier iris.csv dans un DataFrame
df = pd.read_csv('iris.csv', delimiter=";")

# Afficher les premières lignes du jeu de données
print(df.head())


