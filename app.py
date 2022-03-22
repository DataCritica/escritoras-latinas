import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from pyvis.network import Network
from load_css import local_css


# Open image with PIL
favicon = Image.open("./data/assets/favicon.ico")
# Set title page and favicon
st.set_page_config(
    page_title='Escritoras latinoamericanas - DataCrítica', 
    page_icon = favicon, 
    layout = 'wide', 
    initial_sidebar_state = 'expanded',)

# Read styles file
local_css("styles.css")

# Set sidebar
st.sidebar.title("Escritoras latinoamericanas")

# Read dataset (CSV)
df = pd.read_csv('./data/processed/escritoras_wiki.csv')

# Define list of selection options and sort alphabetically
countries = df['País'].drop_duplicates().to_list()
countries.sort()
countries.insert(0, '')

# Implement select dropdown menu for option selection (returns a list)
selected_country = st.sidebar.selectbox('', countries, format_func=lambda x: 'Selecciona un país' if x == '' else x)

if selected_country:
    # Create network graph with user selection
    df_select = df.loc[df['País'] == selected_country]
    count = df_select['País'].count()
    source = df_select['País']
    target = df_select['Nombre']
    bio = df_select['Biografía']
    url = df_select['Url']

    # Create an interator with the selected data
    edge_data = zip(source, target, bio, url)

    # Initiate PyVis network object
    net = Network(height='600px', width='100%', notebook=True, bgcolor='#222222', font_color='white')

    # Create a node for each element on the iterator
    for e in edge_data:
        src = e[0]
        tgt = e[1]
        bio = e[2]
        url = e[3]
        net.add_node(src, src, size=15, title=f'{src}:<br>{count} escritoras', color='#0200ff')
        net.add_node(tgt, tgt, size=15, title=f'{bio}<br><br><a href="{url}" target="_blank">Leer más</a>', color='#23DC5F')
        net.add_edge(src, tgt, color='#DC23A0')

    # Generate network with specific layout settings
    net.repulsion(
                        node_distance=400,
                        central_gravity=0.9,
                        spring_length=150,
                        spring_strength=0.05,
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


# Show message on the sidebar
with st.sidebar:
    st.markdown(
"""
<br>
<br>
<br>
<h5 style='text-align: center; color: #DC23A0; font-size: 14px;'>
    ¿Conoces alguna escritora que falte en esta red?
</h5>
<h5 style='text-align: center; font-size: 14px;'>
<a href="https://ee.humanitarianresponse.info/x/DPNAGl9g" target="_blank">
    Añádela aquí
</a>
</h5>
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