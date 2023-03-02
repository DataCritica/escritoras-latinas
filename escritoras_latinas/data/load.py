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
data_processed = path.data_processed_dir('escritoras_wiki.csv')
escritores_destacados = path.data_processed_dir('escritores_destacados.csv')
data_entries = path.data_processed_dir('entries.csv')

# Outputs
processed = path.data_processed_dir()
tables =  path.outputs_tables_dir()
figures = path.outputs_figures_dir()
networks = path.outputs_networks_dir()
assets = path.assets_dir()
imgs = path.assets_imgs_dir()
imgs_processed = path.assets_imgs_processed_dir()
targets = path.assets_targets_dir()
targets_processed = path.assets_targets_processed_dir()