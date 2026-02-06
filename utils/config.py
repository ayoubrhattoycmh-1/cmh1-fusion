"""
Configuration module for page setup and constants
"""
import streamlit as st

def setup_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="CMH1 Fusion",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

# Application constants
APP_NAME = "CMH1 Fusion"
APP_VERSION = "2.0"
