import pandas as pd
import streamlit as st
import escritoras_latinas.utils.paths as path


"""
Function to convert columns into a list

df: dataframe
return: list of columns names
"""
def load_columns(df):
    cols = df.columns
    return cols

"""
Function to read css file into streamlit app
"""
def css(styles):
    with open(f'{styles}') as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Inputs
data_raw = path.data_raw_dir('escritoras.csv')
data_escritoras = path.data_processed_dir('escritoras_wiki.csv')

# Outputs
data_processed = path.data_processed_dir()
tables =  path.outputs_tables_dir()
figures = path.outputs_figures_dir()
assets = path.assets_dir()