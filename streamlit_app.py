import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


#Charger le fichier iris.csv dans un DataFrame
df = pd.read_csv('iris.csv', delimiter=";")

# Afficher les premières lignes du jeu de données
print(df.head())


