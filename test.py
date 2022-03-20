import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
from load_css import local_css

# Read styles file
local_css("styles.css")

# Set sidebar
st.sidebar.title("Escritoras latinoamericanas")

# Read dataset (CSV)
df = pd.read_csv('data/raw/data.csv')

# Define list of selection options and sort alphabetically
countries = df['País'].drop_duplicates().to_list()
countries.sort()
countries.insert(0, '')

# Implement select dropdown menu for option selection (returns a list)
selected_country = st.sidebar.selectbox('', countries, format_func=lambda x: 'Selecciona un país' if x == '' else x)

if selected_country:
    # Create network graph with user selection
    df_select = df.loc[df['País'] == selected_country]

    # Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(df_select, source='País', target='Escritora', edge_attr=True)

    # Initiate PyVis network object
    net = Network(height='700px', width='100%', notebook=True, bgcolor='#222222', font_color='white')

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
    components.html(HtmlFile.read(), height=700, scrolling=True)


# Set footer
st.sidebar.write("Puedes interactuar con la red")

st.sidebar.write("¿Conoces alguna escritora que falte en esta red?")


# Hide streamlit menu and footer message
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
