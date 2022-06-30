import pandas as pd
import streamlit as st

st.title('new app test')

df = pd.read_csv('github.com/LBECFIT/streamlit_app/blob/main/streamlit_app_2/df_rf3.csv')
st.dataframe(df)
