import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data.csv")

st.subheader("Diabetes dataset")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.subheader("Scatter Plot")
x_axis= st.selectbox("Select the x axix variable:", df.columns)
y_axis = st.selectbox("Select y-axis column:", df.columns)
hue_column = st.selectbox("Select hue column:", df.columns)

fig, ax = plt.subplots()
scatter = ax.scatter(df[x_axis], df[y_axis], c=df[hue_column])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title("Scatter Plot")
legend1 = ax.legend(*scatter.legend_elements(), title=hue_column)
ax.add_artist(legend1)
st.pyplot(fig)

