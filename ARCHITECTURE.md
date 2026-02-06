# 🏗️ Architecture Diagram

## Project Structure Visual

```
cmh1_refactored/
│
├── 🚀 ENTRY POINT
│   └── app.py (35 lines)
│       ├── Imports modules
│       ├── Sets up page config
│       ├── Loads custom styles
│       ├── Creates 3 tabs
│       └── Delegates to pages
│
├── 📱 PAGES (User Interface)
│   ├── html_editor.py
│   │   └── Renders V6.html interface
│   │
│   ├── email_tool.py
│   │   ├── Connection settings UI
│   │   ├── Extraction options UI
│   │   ├── Advanced options UI
│   │   └── Orchestrates processing
│   │
│   └── cmh1_pro.py
│       └── Renders cmh1-pro.html interface
│
├── 🧩 COMPONENTS (Business Logic)
│   └── email_processor.py
│       ├── process_text_extraction()
│       │   ├── Merged file mode
│       │   └── Separate files mode
│       │
│       └── process_original_emails()
│           ├── Header modifications
│           ├── Domain replacement
│           └── Custom transformations
│
├── 🛠️ UTILS (Helpers & Config)
│   ├── config.py
│   │   ├── setup_page()
│   │   └── App constants
│   │
│   ├── styles.py
│   │   └── load_custom_css()
│   │       ├── Global styles
│   │       ├── Tab styling
│   │       ├── Input fields
│   │       └── Animations
│   │
│   └── email_utils.py
│       ├── decode_header_text()
│       ├── clean_filename()
│       ├── clean_html_to_plain()
│       ├── get_email_body_text()
│       └── detect_duplicates()
│
├── 📄 TEMPLATES
│   ├── V6.html (HTML editor)
│   └── cmh1-pro.html (CMH1 Pro)
│
├── 📚 DOCUMENTATION
│   ├── README.md (Full guide)
│   ├── QUICKSTART.md (5-min start)
│   ├── COMPARISON.md (Before/After)
│   ├── CHANGELOG.md (History)
│   └── PROJECT_SUMMARY.md (Overview)
│
└── 🔧 UTILITIES
    ├── setup.sh (Installation)
    ├── run.sh (Launch)
    ├── requirements.txt (Dependencies)
    └── .gitignore (Git config)
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         USER                                │
│                           ↓                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      app.py                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  1. setup_page() → config.py                         │  │
│  │  2. load_custom_css() → styles.py                    │  │
│  │  3. Create tabs                                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
          ↓                    ↓                    ↓
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   TAB 1         │  │   TAB 2         │  │   TAB 3         │
│                 │  │                 │  │                 │
│ html_editor.py  │  │ email_tool.py   │  │ cmh1_pro.py     │
│                 │  │                 │  │                 │
│ ┌─────────────┐ │  │ ┌─────────────┐ │  │ ┌─────────────┐ │
│ │ Load V6.html│ │  │ │ Show UI     │ │  │ │Load cmh1-pro│ │
│ │ Render      │ │  │ │ Get inputs  │ │  │ │Render       │ │
│ └─────────────┘ │  │ │ Validate    │ │  │ └─────────────┘ │
│                 │  │ └──────┬──────┘ │  │                 │
└─────────────────┘  └────────┼────────┘  └─────────────────┘
                              ↓
                    ┌─────────────────┐
                    │ Process Emails  │
                    └────────┬────────┘
                             ↓
            ┌────────────────┴────────────────┐
            ↓                                 ↓
  ┌─────────────────────┐        ┌──────────────────────┐
  │ Text Extraction     │        │ Original Format      │
  │                     │        │                      │
  │ email_processor.py  │        │ email_processor.py   │
  │                     │        │                      │
  │ Uses:               │        │ Uses:                │
  │ └→ email_utils.py   │        │ └→ email_utils.py    │
  │    - get_body()     │        │    - clean_filename()│
  │    - detect_dups()  │        │    - decode_header() │
  └─────────┬───────────┘        └──────────┬───────────┘
            ↓                               ↓
  ┌─────────────────────┐        ┌──────────────────────┐
  │ Merged or Separate  │        │ Modified Headers     │
  │ Text Files          │        │ ZIP with Emails      │
  └─────────────────────┘        └──────────────────────┘
```

## Module Dependencies

```
app.py
  │
  ├─→ utils/config.py
  │     └─→ streamlit
  │
  ├─→ utils/styles.py
  │     └─→ streamlit
  │
  └─→ pages/
        │
        ├─→ html_editor.py
        │     ├─→ streamlit
        │     └─→ streamlit.components
        │
        ├─→ email_tool.py
        │     ├─→ streamlit
        │     ├─→ utils/email_utils.py
        │     │     ├─→ email
        │     │     └─→ re
        │     │
        │     └─→ components/email_processor.py
        │           ├─→ streamlit
        │           ├─→ email
        │           ├─→ zipfile
        │           ├─→ io
        │           ├─→ re
        │           └─→ utils/email_utils.py
        │
        └─→ cmh1_pro.py
              ├─→ streamlit
              └─→ streamlit.components
```

## Execution Flow

```
1. User runs: streamlit run app.py
   ↓
2. app.py imports all modules
   ↓
3. setup_page() configures Streamlit
   ↓
4. load_custom_css() applies styles
   ↓
5. Three tabs created
   ↓
6. User clicks tab
   ↓
7. Corresponding page.render() executes
   ↓
8. [If Tab 2 - Email Tool]:
   ├─→ User fills form
   ├─→ Clicks "Start Processing"
   ├─→ email_tool.process_emails() called
   ├─→ Connects to IMAP
   ├─→ Fetches email IDs
   ├─→ [If duplicate detection]:
   │   ├─→ Calls detect_duplicates()
   │   └─→ Filters unique emails
   ├─→ [If text extraction]:
   │   └─→ Calls process_text_extraction()
   │       ├─→ Uses get_email_body_text()
   │       ├─→ Creates ZIP or merged file
   │       └─→ Returns download button
   └─→ [If original format]:
       └─→ Calls process_original_emails()
           ├─→ Modifies headers
           ├─→ Creates ZIP
           └─→ Returns download button
```

## Styling Flow

```
User loads page
     ↓
app.py calls load_custom_css()
     ↓
styles.py injects CSS
     ↓
CSS sections applied:
  ├─→ Global background
  ├─→ Hide sidebar
  ├─→ Tab styling
  ├─→ Label colors
  ├─→ Input fields
  ├─→ Buttons
  ├─→ Scrollbars
  └─→ Animations
     ↓
Professional UI rendered!
```

## Component Interaction

```
┌─────────────────────────────────────────────────────┐
│                   USER INTERFACE                    │
│  (pages/email_tool.py - shows forms & buttons)      │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────┐
│               ORCHESTRATION LAYER                   │
│  (pages/email_tool.py - validates & coordinates)    │
└────────────┬──────────────────────┬─────────────────┘
             │                      │
             ↓                      ↓
┌────────────────────┐    ┌─────────────────────────┐
│  HELPER FUNCTIONS  │    │  PROCESSING LOGIC       │
│  (utils/email_     │    │  (components/email_     │
│   utils.py)        │    │   processor.py)         │
│                    │    │                         │
│  - Decode headers  │◄───│  - Extract text         │
│  - Clean filenames │    │  - Modify headers       │
│  - Parse HTML      │    │  - Create archives      │
│  - Detect dupes    │    │  - Handle errors        │
└────────────────────┘    └─────────────────────────┘
```

## File Size Distribution

```
Original app.py: ████████████████████████████ 700 lines

Refactored:
├─ app.py:                █ 35 lines
├─ pages/email_tool.py:   ████████ 250 lines
├─ components/email_pr:   ██████ 170 lines
├─ utils/email_utils.py:  ██████ 170 lines
├─ utils/styles.py:       ████ 110 lines
├─ pages/html_editor.py:  █ 28 lines
├─ pages/cmh1_pro.py:     █ 26 lines
├─ utils/config.py:       █ 15 lines
└─ Total:                 ████████████████████ 600 lines
                          (But organized & documented!)
```

---

## Key Takeaways

### Modularity
```
Before: Everything in one place
After:  Clear separation of concerns
```

### Maintainability
```
Before: Find needle in 700-line haystack
After:  Go directly to the right module
```

### Scalability
```
Before: Hard to add features
After:  Just create new module
```

### Readability
```
Before: Scroll, scroll, scroll...
After:  Small, focused files
```

---

**This architecture enables:**
- ✅ Fast development
- ✅ Easy debugging
- ✅ Simple testing
- ✅ Team collaboration
- ✅ Professional quality
