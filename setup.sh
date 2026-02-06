#!/bin/bash

# CMH1 Fusion - Setup Script
# Simple installation and launch script

echo "🚀 CMH1 Fusion - Professional Edition Setup"
echo "==========================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed!"
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Install requirements
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "==========================================="
echo "✅ Setup completed successfully!"
echo ""
echo "To run the application:"
echo "  streamlit run app.py"
echo ""
echo "Or use: ./run.sh"
echo "==========================================="
