import streamlit as st

def local_css(styles):
    with open(f'{styles}') as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)