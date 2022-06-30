import pandas as pd
import streamlit as st

st.title('new app test')

df = pd.read_csv('df_missings.csv')
st.dataframe(df)
