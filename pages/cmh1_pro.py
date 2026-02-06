"""
CMH-1 Pro Page
Renders the cmh1-pro.html interface
"""
import streamlit as st
import streamlit.components.v1 as components
import os

def render():
    """Render the CMH-1 Pro page"""
    cmh1_html_path = "cmh1-pro.html"
    
    if os.path.exists(cmh1_html_path):
        with open(cmh1_html_path, "r", encoding="utf-8") as f:
            cmh1_html_code = f.read()
        
        # Render HTML component with scrolling enabled
        components.html(cmh1_html_code, height=920, scrolling=True)
    else:
        st.error("⚠️ Fichier 'cmh1-pro.html' ma kaynch!")
        st.info("Assurez-vous que le fichier cmh1-pro.html se trouve dans le répertoire principal.")
