# 🚀 CMH1 Fusion - Professional Edition

Modern, lightweight, and professional Streamlit application with modular architecture.

## ✨ Features

- **💻 HTML Fusion Editor** - Advanced HTML editor interface
- **📧 IMAP Email Tool** - Extract and process emails with advanced options
- **⚡ CMH-1 Pro** - Professional tool interface
- **🎨 Modern UI** - Dark theme with smooth animations
- **📦 Modular Architecture** - Clean, maintainable code structure

## 🏗️ Project Structure

```
cmh1_refactored/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── V6.html                     # HTML editor template
├── cmh1-pro.html              # CMH1 Pro template
│
├── pages/                      # Application pages
│   ├── __init__.py
│   ├── html_editor.py         # HTML Fusion Editor page
│   ├── email_tool.py          # IMAP Email Tool page
│   └── cmh1_pro.py            # CMH-1 Pro page
│
├── components/                 # Reusable components
│   ├── __init__.py
│   └── email_processor.py     # Email processing logic
│
├── utils/                      # Utility modules
│   ├── __init__.py
│   ├── config.py              # App configuration
│   ├── styles.py              # CSS styles
│   └── email_utils.py         # Email helper functions
│
└── assets/                     # Static assets (images, etc.)
```

## 🚀 Quick Start

### Installation

```bash
# Clone or extract the project
cd cmh1_refactored

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### HTML Fusion Editor
- Access through the first tab
- Edit and preview HTML code
- All features from original V6.html preserved

### IMAP Email Tool
1. **Connection Settings**
   - Enter your IMAP server (e.g., mail.amorstechhost.com)
   - Provide email credentials
   - Select folder (default: INBOX)

2. **Extraction Options**
   - Set email range (start/end numbers)
   - Choose plain text extraction or original format
   - Enable duplicate detection (recommended)

3. **Advanced Options**
   - Name files by subject
   - Modify email headers
   - Replace domains
   - Clean authentication headers
   - Add custom headers

4. **Processing**
   - Click "Start Processing"
   - Monitor progress
   - Download results (ZIP or TXT)

### CMH-1 Pro
- Access through the third tab
- All original features preserved

## 🎯 Key Improvements

### Architecture
- ✅ **Modular Design** - Separated concerns into pages, components, and utils
- ✅ **Clean Code** - Well-documented and easy to maintain
- ✅ **Scalable** - Easy to add new features or pages

### Performance
- ✅ **Lightweight** - Minimal dependencies
- ✅ **Optimized** - Efficient email processing
- ✅ **Fast Loading** - Modular imports

### User Experience
- ✅ **Modern UI** - Professional dark theme
- ✅ **Smooth Animations** - Enhanced interactions
- ✅ **Better Layout** - Improved organization
- ✅ **Clear Feedback** - Progress indicators and status messages

### Code Quality
- ✅ **Type Hints** - Better code documentation
- ✅ **Error Handling** - Robust error management
- ✅ **Comments** - Clear explanations
- ✅ **Best Practices** - Following Python/Streamlit conventions

## 🔧 Configuration

### Customizing Styles
Edit `utils/styles.py` to modify colors, fonts, and layout.

### Adding New Pages
1. Create new file in `pages/` directory
2. Define `render()` function
3. Import in `pages/__init__.py`
4. Add tab in `app.py`

### Adding New Features
- Create components in `components/` directory
- Add utilities in `utils/` directory
- Keep code modular and reusable

## 📝 Development Notes

### Code Organization
- **Pages**: Main UI components (one per tab)
- **Components**: Reusable logic and processing
- **Utils**: Helper functions and configuration
- **Assets**: Static files (images, etc.)

### Best Practices
- Keep functions small and focused
- Use meaningful variable names
- Document complex logic
- Handle errors gracefully
- Test before deploying

## 🐛 Troubleshooting

### IMAP Connection Issues
- Check server address and port
- Verify credentials
- Enable IMAP in email settings
- Check firewall/antivirus

### HTML Files Not Found
- Ensure V6.html and cmh1-pro.html are in root directory
- Check file paths in code
- Verify file permissions

### Styling Issues
- Clear browser cache
- Check CSS in utils/styles.py
- Verify Streamlit version compatibility

## 📦 Dependencies

- **streamlit** - Web application framework
- Built-in Python libraries only (no external dependencies)

## 🔄 Migration from Original

All features from the original app.py are preserved:
- ✅ HTML Fusion Editor (V6.html)
- ✅ IMAP Email Tool with all options
- ✅ CMH-1 Pro interface
- ✅ Custom styling and theme
- ✅ Duplicate detection
- ✅ All email processing features

**Nothing was removed - only reorganized for better maintainability!**

## 🎨 Customization

### Change Theme Colors
Edit the CSS in `utils/styles.py`:
- Background: `#1a1b26`
- Primary: `#00f5c3`
- Secondary: `#565F89`

### Modify Layout
Edit page configurations in respective files in `pages/` directory.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review code comments
3. Check Streamlit documentation

## 📄 License

Same license as original project.

---

**Built with ❤️ using Streamlit**

*Professional Edition - Optimized for Production*
