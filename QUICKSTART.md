# 🚀 Quick Start Guide

Get up and running with CMH1 Fusion in 5 minutes!

## ⚡ Fast Track

```bash
# 1. Navigate to project
cd cmh1_refactored

# 2. Install dependencies
./setup.sh

# 3. Run application
./run.sh
```

That's it! Your browser will open automatically at `http://localhost:8501`

---

## 📋 Prerequisites

- **Python 3.8+** installed
- **pip** package manager
- Internet connection (for initial setup)

### Check Python Version
```bash
python3 --version
# Should show: Python 3.8.x or higher
```

---

## 🔧 Manual Installation

If the scripts don't work, follow these steps:

### Step 1: Install Dependencies
```bash
pip3 install streamlit
```

Or use requirements file:
```bash
pip3 install -r requirements.txt
```

### Step 2: Run Application
```bash
streamlit run app.py
```

---

## 🎯 First Use

### 1. HTML Fusion Editor (Tab 1)
- Click first tab "💻 HTML FUSION EDITOR"
- The V6.html editor will load automatically
- Start editing!

### 2. IMAP Email Tool (Tab 2)
**Quick Test:**
```
Server: mail.amorstechhost.com
Email: your_email@domain.com
Password: your_password
Folder: INBOX
Start: 1
End: 5
```

Click "🚀 Start Processing" → Download emails

### 3. CMH-1 Pro (Tab 3)
- Click third tab "⚡ CMH-1 PRO"
- Interface loads automatically

---

## 🐛 Troubleshooting

### "Command not found: streamlit"
**Solution:**
```bash
pip3 install streamlit
# Or
python3 -m pip install streamlit
```

### "Permission denied: ./setup.sh"
**Solution:**
```bash
chmod +x setup.sh run.sh
./setup.sh
```

### "Port 8501 already in use"
**Solution:**
```bash
# Kill existing Streamlit process
pkill -f streamlit

# Or use different port
streamlit run app.py --server.port 8502
```

### IMAP Connection Failed
**Check:**
1. ✅ Correct server address
2. ✅ Valid credentials
3. ✅ IMAP enabled in email settings
4. ✅ No firewall blocking

---

## 📱 Browser Issues

### Browser doesn't open automatically
**Manual access:**
```
http://localhost:8501
```

### Page looks broken
**Solutions:**
1. Clear browser cache (Ctrl+Shift+R)
2. Try different browser
3. Check console for errors

---

## 🎨 Customization

### Change Colors
Edit `utils/styles.py`:
```python
# Line 23: Background
background-color: #1a1b26;

# Line 56: Primary color
background-color: #00f5c3;
```

### Change Port
```bash
streamlit run app.py --server.port 9000
```

### Disable Auto-open Browser
```bash
streamlit run app.py --server.headless true
```

---

## 📚 Common Tasks

### Extract Emails
1. Go to Tab 2 (📧 IMAP EMAIL TOOL)
2. Enter IMAP credentials
3. Set email range
4. Choose options
5. Click "Start Processing"
6. Download ZIP file

### Edit HTML
1. Go to Tab 1 (💻 HTML FUSION EDITOR)
2. Use the interface
3. Make changes
4. Preview/download

---

## 🔄 Updating

To update to a new version:
```bash
# Backup your HTML files
cp V6.html V6.html.backup
cp cmh1-pro.html cmh1-pro.html.backup

# Replace all files except HTML files
# Restore your HTML files
```

---

## 📞 Getting Help

### Check Documentation
1. `README.md` - Full documentation
2. `COMPARISON.md` - Original vs Refactored
3. `CHANGELOG.md` - What's new

### Common Solutions
- **IMAP issues**: Check credentials and server
- **UI issues**: Clear cache, refresh browser
- **Install issues**: Update pip: `pip3 install --upgrade pip`

---

## 💡 Pro Tips

### Speed Up Development
```bash
# Auto-reload on file changes (default in Streamlit)
streamlit run app.py
# Edit files → Changes auto-reflect
```

### Run in Background
```bash
nohup streamlit run app.py &
# Application runs even after closing terminal
```

### Share Locally
```bash
# Find your local IP
ifconfig | grep inet

# Access from other devices on same network
http://YOUR_IP:8501
```

---

## ✅ Verification

Test everything works:

### ✅ Installation
```bash
streamlit --version
# Should show version number
```

### ✅ App Loads
- Browser opens automatically
- Three tabs visible
- No errors in console

### ✅ HTML Editor
- Tab 1 shows editor
- No error messages

### ✅ Email Tool
- Tab 2 shows form
- All fields present

### ✅ CMH-1 Pro
- Tab 3 loads
- Interface visible

---

## 🎯 Next Steps

After installation:
1. ✅ Read `README.md` for full features
2. ✅ Check `COMPARISON.md` to see improvements
3. ✅ Explore all three tabs
4. ✅ Try extracting sample emails
5. ✅ Customize colors/settings

---

**You're all set! Enjoy using CMH1 Fusion! 🎉**

For detailed documentation, see `README.md`
