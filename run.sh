#!/bin/bash

# CMH1 Fusion - Run Script
# Quick launch script

echo "🚀 Starting CMH1 Fusion..."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed!"
    echo "Run ./setup.sh first to install dependencies"
    exit 1
fi

# Run the application
streamlit run app.py
