"""
Custom CSS styles for the application
"""
import streamlit as st

def load_custom_css():
    """Load custom CSS styles for the application"""
    st.markdown("""
    <style>
        /* ==================== GLOBAL STYLES ==================== */
        .stApp {
            background-color: #1a1b26;
        }
        
        /* ==================== SIDEBAR ==================== */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* ==================== TABS STYLING ==================== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: #565F89;
            padding: 10px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            background-color: transparent;
            border-radius: 8px;
            color: #919499;
            font-weight: 600;
            border: none;
            padding: 0 20px;
            transition: all 0.3s ease;
        }

        /* Selected Tab */
        .stTabs [aria-selected="true"] {
            background-color: #00f5c3 !important;
            color: #1a1b26 !important;
            font-weight: bold;
        }
        
        /* Hover Effect */
        .stTabs [data-baseweb="tab"]:hover {
            color: #00f5c3;
            transform: translateY(-2px);
        }
        
        /* ==================== LABELS & TEXT ==================== */
        label {
            color: #D3D6E4 !important;
        }

        [data-testid="stWidgetLabel"] p {
            color: #c0caf5 !important;
        }

        .stMarkdown p {
            color: #c0caf5 !important;
        }
        
        /* ==================== INPUT FIELDS ==================== */
        .stTextInput input, 
        .stNumberInput input, 
        .stTextArea textarea {
            background-color: #24283b !important;
            color: #c0caf5 !important;
            border: 1px solid #414868 !important;
            border-radius: 8px;
            transition: border-color 0.3s ease;
        }
        
        .stTextInput input:focus,
        .stNumberInput input:focus,
        .stTextArea textarea:focus {
            border-color: #00f5c3 !important;
            box-shadow: 0 0 0 1px #00f5c3;
        }
        
        /* ==================== BUTTONS ==================== */
        .stButton button {
            font-weight: bold;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 245, 195, 0.3);
        }
        
        /* ==================== LAYOUT ==================== */
        [data-testid="stDecoration"] {
            display: none;
        }
        
        header {
            visibility: hidden;
        }
        
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* ==================== SCROLLBAR ==================== */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1b26;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #565F89;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #00f5c3;
        }
    </style>
    """, unsafe_allow_html=True)
