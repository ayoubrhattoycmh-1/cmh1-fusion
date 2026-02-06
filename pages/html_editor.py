"""
HTML Fusion Editor Page
Renders the V6.html HTML editor interface
"""
import streamlit as st
import streamlit.components.v1 as components
import os

def render():
    """Render the HTML Fusion Editor page"""
    html_file_path = "V6.html"
    
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
        
        # Render HTML component with scrolling enabled
        components.html(html_code, height=920, scrolling=True)
    else:
        st.error("⚠️ Fichier 'V6.html' ma kaynch!")
        st.info("Assurez-vous que le fichier V6.html se trouve dans le répertoire principal.")
