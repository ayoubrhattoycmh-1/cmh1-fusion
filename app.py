"""
CMH1 Fusion - Professional Streamlit Application
Main entry point with modular architecture
"""
import streamlit as st
from utils.config import setup_page
from utils.styles import load_custom_css
from pages import html_editor, email_tool, cmh1_pro

def main():
    """Main application entry point"""
    # Setup page configuration
    setup_page()
    
    # Load custom styles
    load_custom_css()
    
    # Create navigation tabs
    tab1, tab2, tab3 = st.tabs([
        "💻 HTML FUSION EDITOR", 
        "📧 IMAP EMAIL TOOL", 
        "⚡ CMH-1 PRO"
    ])
    
    # Render each page in its respective tab
    with tab1:
        html_editor.render()
    
    with tab2:
        email_tool.render()
    
    with tab3:
        cmh1_pro.render()

if __name__ == "__main__":
    main()
