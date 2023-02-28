import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data.csv")

st.title("Dashboard for Diabetes Dataset")
img = image.imread(IMAGE_PATH)
st.image(img)

st.header("About the dataset:")
st.text("This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. ")
st.text(" The objective of the dataset is to diagnostically predict whether a patient has diabetes,based on certain diagnostic measurements included in the dataset. ")
st.text("All patients here are females at least 21 years old of Pima Indian heritage.2")

st.subheader("Diabetes dataset")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.markdown("To better understand the dataset, please continue to the following pages where you will find various plots and visualizations.")


