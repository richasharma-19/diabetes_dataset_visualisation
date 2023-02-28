import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data.csv")

st.subheader("Diabetes dataset")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.subheader("Box plot")
column = st.selectbox("Select column:", df.columns)


fig, ax = plt.subplots()
ax.boxplot(df[column])
ax.set_xlabel(column)
ax.set_ylabel("value")

st.pyplot(fig.figure)