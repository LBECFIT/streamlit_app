import pandas as pd
import streamlit as st
!pip install plotly_express
import plotly_express as px

st.title('new app test')

df = pd.read_csv('df_rf3.csv')
st.dataframe(df)
