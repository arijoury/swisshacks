import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

"""Ari und Söhne"""

st.title("""
         UBS financial data 2020-2023
         """)

df = pd.read_json('data_ubs.json')

def make_fig(var):
    fig, ax = plt.subplots()
    sns.barplot(df,x='year',y=var)
    ax.set(xlabel='year', ylabel=f'{var} [in million Euros]', title=f'{var}')
    #fig.savefig('ubs_profit.png')
    st.pyplot(fig)
    st.caption(f'UBS {var} soared in 2023 due to buying Credit Suisse')

df_vars = list(df) #get the headers
tabs = st.tabs(df_vars[1:])
for f, ind in enumerate(df_vars[1:]):
    with tabs[f]: make_fig(ind)



