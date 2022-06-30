import pandas as pd
import streamlit as st

st.title('new app test')

df = pd.read_csv('df_rf3.csv',sep=',')
st.dataframe(df)
