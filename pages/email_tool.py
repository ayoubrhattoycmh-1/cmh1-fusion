"""
IMAP Email Tool Page
Advanced email extraction and processing tool with duplicate detection
"""
import streamlit as st
import email
import imaplib
import zipfile
import io
from utils.email_utils import (
    decode_header_text, 
    clean_filename, 
    get_email_body_text,
    detect_duplicates
)
from components.email_processor import (
    process_text_extraction,
    process_original_emails
)


def render():
    """Render the IMAP Email Tool page"""
    
    # Page header with emoji and description
    st.markdown("### 📧 IMAP Email Extraction Tool")
    st.markdown("Connect to your email account and extract emails with advanced options")
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### 🔐 Connection Settings")
        imap_server = st.text_input(
            "IMAP Server", 
            value="imap.gmail.com",
            help="Enter your IMAP server address (e.g., imap.gmail.com)"
        )
        
        imap_user = st.text_input(
            "Email Address",
            placeholder="your.email@example.com",
            help="Your email address for authentication"
        )
        
        imap_pass = st.text_input(
            "Password", 
            type="password",
            help="Your email password or app-specific password"
        )
        
        folder_name = st.text_input(
            "Folder Name", 
            value="INBOX",
            help="Email folder to extract from (e.g., INBOX, Sent, Drafts)"
        )
    
    with col2:
        st.markdown("#### ⚙️ Extraction Options")
        
        # Email range selection
        st.markdown("**Email Range:**")
        col_range1, col_range2 = st.columns(2)
        with col_range1:
            start_num = st.number_input(
                "Start Email #", 
                min_value=1, 
                value=1,
                help="First email number to extract"
            )
        with col_range2:
            end_num = st.number_input(
                "End Email #", 
                min_value=1, 
                value=20,
                help="Last email number to extract"
            )
        
        # Processing mode
        extract_plain_only = st.checkbox(
            "📄 Extract Plain Text Only",
            value=False,
            help="Extract only email body text without headers"
        )
        
        # Export format (only shown for text extraction)
        if extract_plain_only:
            export_format = st.radio(
                "Export Format:",
                ["Separate Files (ZIP)", "Merged Single File"],
                help="Choose how to organize extracted text"
            )
        
        # Duplicate detection
        remove_duplicates = st.checkbox(
            "🔍 Remove Duplicates",
            value=True,
            help="Automatically detect and remove duplicate emails"
        )
    
    # Advanced options in an expander
    with st.expander("🛠️ Advanced Options (For Original Email Format)"):
        st.markdown("*These options only apply when NOT extracting plain text*")
        
        col_adv1, col_adv2 = st.columns(2)
        
        with col_adv1:
            name_by_subj = st.checkbox(
                "Name files by Subject",
                value=True,
                help="Use email subject as filename instead of numbers"
            )
            
            rep_dom = st.checkbox(
                "Replace Domain in From",
                value=False,
                help="Replace the domain part of sender email"
            )
            
            if rep_dom:
                p_from = st.text_input(
                    "New Domain", 
                    value="yourdomain.com",
                    help="New domain to replace in From header"
                )
            
            std_headers = st.checkbox(
                "Standardize To/Date Headers",
                value=False,
                help="Replace To and Date with placeholders"
            )
        
        with col_adv2:
            mod_eid = st.checkbox(
                "Modify Message-ID",
                value=False,
                help="Add [EID] marker to Message-ID"
            )
            
            clean_auth = st.checkbox(
                "Remove Auth Headers",
                value=False,
                help="Remove DKIM, SPF, and authentication headers"
            )
            
            custom_headers_text = st.text_area(
                "Custom Headers (key:value per line)",
                placeholder="X-Custom-Header: value\nX-Another: data",
                help="Add custom headers to emails (one per line)"
            )
    
    # Process button
    st.markdown("---")
    if st.button("🚀 Start Processing", type="primary", use_container_width=True):
        process_emails(
            imap_server=imap_server,
            imap_user=imap_user,
            imap_pass=imap_pass,
            folder_name=folder_name,
            start_num=start_num,
            end_num=end_num,
            extract_plain_only=extract_plain_only,
            export_format=export_format if extract_plain_only else None,
            remove_duplicates=remove_duplicates,
            name_by_subj=name_by_subj,
            rep_dom=rep_dom,
            p_from=p_from if rep_dom else None,
            std_headers=std_headers,
            mod_eid=mod_eid,
            clean_auth=clean_auth,
            custom_headers_text=custom_headers_text
        )


def process_emails(**kwargs):
    """
    Main email processing function
    Handles IMAP connection, email fetching, and processing
    """
    # Extract parameters
    imap_server = kwargs.get('imap_server')
    imap_user = kwargs.get('imap_user')
    imap_pass = kwargs.get('imap_pass')
    folder_name = kwargs.get('folder_name')
    start_num = kwargs.get('start_num')
    end_num = kwargs.get('end_num')
    extract_plain_only = kwargs.get('extract_plain_only')
    export_format = kwargs.get('export_format')
    remove_duplicates = kwargs.get('remove_duplicates')
    
    # Validation
    if not all([imap_server, imap_user, imap_pass]):
        st.error("⚠️ Please fill in all connection fields!")
        return
    
    if start_num > end_num:
        st.error("⚠️ Start number must be less than or equal to end number!")
        return
    
    # Progress indicators
    status_msg = st.empty()
    prog_bar = st.progress(0)
    
    try:
        # Connect to IMAP server
        status_msg.info("🔌 Connecting to IMAP server...")
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(imap_user, imap_pass)
        
        status_msg.info(f"📂 Selecting folder: {folder_name}")
        mail.select(folder_name)
        
        # Search for emails
        status_msg.info("🔍 Searching for emails...")
        _, data = mail.search(None, 'ALL')
        all_ids = data[0].split()
        
        if not all_ids:
            status_msg.error("📭 No emails found in this folder!")
            mail.logout()
            return
        
        # Calculate range
        total_emails = len(all_ids)
        actual_start = max(1, min(start_num, total_emails))
        actual_end = max(1, min(end_num, total_emails))
        
        # Get IDs for the range
        id_list = all_ids[actual_start-1:actual_end]
        
        status_msg.info(f"📊 Found {total_emails} emails. Processing {len(id_list)} emails (#{actual_start} to #{actual_end})")
        
        # Duplicate detection if enabled
        if remove_duplicates and len(id_list) > 1:
            status_msg.info("🔍 Checking for duplicates...")
            email_data_list = []
            
            # Fetch basic info for duplicate detection
            for i, eid in enumerate(id_list):
                try:
                    _, msg_data = mail.fetch(eid, '(RFC822)')
                    raw_bytes = msg_data[0][1]
                    email_message = email.message_from_bytes(raw_bytes)
                    
                    email_data_list.append({
                        'id': eid,
                        'message_id': email_message.get('Message-ID', ''),
                        'subject': email_message.get('Subject', ''),
                        'from': email_message.get('From', '')
                    })
                    prog_bar.progress((i + 1) / len(id_list) * 0.3)  # 30% for duplicate check
                except:
                    continue
            
            # Detect duplicates
            unique_emails, duplicates = detect_duplicates(email_data_list)
            
            if duplicates:
                status_msg.warning(
                    f"⚠️ Found {len(duplicates)} duplicate(s). "
                    f"Processing {len(unique_emails)} unique emails."
                )
                
                # Show duplicate details
                with st.expander(f"📋 View {len(duplicates)} Duplicates"):
                    for dup in duplicates[:20]:
                        st.caption(
                            f"Email #{dup['index']}: {dup['subject'][:50]} - {dup['reason']}"
                        )
                    if len(duplicates) > 20:
                        st.caption(f"... and {len(duplicates)-20} more")
            else:
                status_msg.success("✅ No duplicates found!")
            
            # Update id_list to only unique emails
            id_list = [item['id'] for item in unique_emails]
            
            if not id_list:
                st.error("📭 All emails were duplicates!")
                mail.logout()
                return
        
        # Process based on extraction mode
        if extract_plain_only:
            process_text_extraction(
                mail=mail,
                id_list=id_list,
                export_format=export_format,
                name_by_subj=kwargs.get('name_by_subj'),
                status_msg=status_msg,
                prog_bar=prog_bar
            )
        else:
            process_original_emails(
                mail=mail,
                id_list=id_list,
                kwargs=kwargs,
                status_msg=status_msg,
                prog_bar=prog_bar
            )
        
        # Cleanup
        mail.logout()
        
    except imaplib.IMAP4.error as e:
        status_msg.error(f"❌ IMAP Error: {str(e)}")
        st.error("Check your credentials and server settings")
    except Exception as e:
        status_msg.error(f"❌ Error: {str(e)}")
        st.exception(e)
