import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


# Set page width
st.set_page_config(layout="wide")

# Read dataset (CSV)
df = pd.read_csv('data/raw/data.csv')

# Set container
st.markdown(
        """
<style>
    .appview-container .main {
        color: white;
        background-color: #151515;
    }
    .reportview-container .markdown-text-container { 
        font-family: monospace; 
    } 
    .Widget>label { 
        color: white; font-family: monospace; 
    } 
    .st-bb { 
        background-color: transparent; 
    } 
    .st-at {
         background-color: #0c0080; 
    }
    [class^="st-b"] { 
        color: white; 
        font-family: monospace;
        background-color: #2a2a2b; 
    }
</style>
""",
        unsafe_allow_html=True,
    )

# Set header title
st.markdown("<h1 style='text-align: center; color: #23DC5F;'>Escritoras Latinoamericanas</h1>", unsafe_allow_html=True)

# Define list of selection options and sort alphabetically
countries = df['País'].drop_duplicates().to_list()
countries.sort()
countries.insert(0, '')

# Implement select dropdown menu for option selection (returns a list)
selected_country = st.selectbox('', countries, format_func=lambda x: 'Selecciona un país' if x == '' else x)

if selected_country:
    # Create network graph with user selection
    df_select = df.loc[df['País'] == selected_country]

    # Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(df_select, source='País', target='Escritora', edge_attr=True)

    # Initiate PyVis network object
    net = Network(height='500px', width='100%', notebook=True, bgcolor='#222222', font_color='white')

    # Take Networkx graph and translate it to a PyVis graph format
    net.from_nx(G)

    # Generate network with specific layout settings
    net.repulsion(
                        node_distance=400,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
                        )

    # Save and read graph as HTML file (on Streamlit Sharing)
    try:
        path = '/tmp'
        net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
    except:
        path = '/html_files'
        net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=600, scrolling=True)

# Footer
st.markdown(
"""
<br>
<h5 style='text-align: center; color: #DC23A0;'>¿Conoces alguna escritora que falte en esta red?</h5>
<h5 style='text-align: center;'><a href="https://www.datacritica.org" target="_blank">Llena este formulario para que podamos incluirla</a></h5>
""", unsafe_allow_html=True
)

# Hide streamlit menu and footer message
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
