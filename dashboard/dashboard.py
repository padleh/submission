import numpy as np
import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_dataframe(region):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, f"{region.lower()}_df.csv")
    return pd.read_csv(filename)

# Fungsi piechart
def piechart(dataframe, title):
    pollutant = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    counts = dataframe[pollutant].sum()

    st.subheader("Polutan Terbanyak di Distrik " + title) 
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(counts, labels=pollutant, autopct='%1.1f%%', startangle=90, pctdistance=0.80,
            explode=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05], colors=sns.color_palette("Set2"))
    ax.set_title('Sebaran polutan di distrik ' + title + ", Beijing, China", weight='bold')
    st.pyplot(fig)

# Fungsi heatmap
def heatmap(dataframe, title):
    correlation_data = dataframe[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP",
                                   "PRES", "DEWP", "RAIN", "WSPM"]]

    st.subheader("Korelasi antara Polutan dengan Faktor Lingkungan Lainnya di " + title)
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(correlation_data.corr(), cmap="crest", annot=True, ax=ax)
    ax.set_title('Korelasi polutan dengan faktor lainnya di ' + title + ", Beijing, China", weight='bold')
    st.pyplot(fig)

# List region
regions = ['Aotizhongxin', 'Changping', 'Dingling', 'Dongsi', 'Guanyuan',
           'Gucheng', 'Huairou', 'Nongzhanguan', 'Shunyi', 'Tiantan',
           'Wanliu', 'Wanshouxigong']

st.title("Kualitas Udara di Beberap Distrik di Beijing, China")
st.write("Beijing merupakan kota metropolitan yang juga ibukota dari Cina, banyaknya kendaraan dan pabrik batu bara di sana menyebabkan tingkat polusi di beijing sangat tinggi.")
st.sidebar.title("Selamat datang di dashboard")
selected_region = st.sidebar.selectbox("Silahkan pilih distrik yang ingin Anda lihat", regions)

df = load_dataframe(selected_region)

# Visualisasi
piechart(df, selected_region)
heatmap(df, selected_region)

