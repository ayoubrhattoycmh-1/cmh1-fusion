"""
Email Processor Component
Handles the actual processing of emails in different formats
"""
import streamlit as st
import email
import zipfile
import io
import re
from utils.email_utils import get_email_body_text, clean_filename


def process_text_extraction(mail, id_list, export_format, name_by_subj, status_msg, prog_bar):
    """
    Process emails and extract only plain text bodies
    
    Args:
        mail: IMAP connection object
        id_list: List of email IDs to process
        export_format: "Separate Files (ZIP)" or "Merged Single File"
        name_by_subj: Boolean to name files by subject
        status_msg: Streamlit message placeholder
        prog_bar: Streamlit progress bar
    """
    if "Merged" in export_format:
        # Extract to merged single file
        full_extracted_text = []
        
        for i, eid in enumerate(id_list):
            try:
                _, msg_data = mail.fetch(eid, '(RFC822)')
                raw_bytes = msg_data[0][1]
                email_message = email.message_from_bytes(raw_bytes)
                
                # Get clean body text
                body_content = get_email_body_text(email_message)
                
                if body_content:
                    full_extracted_text.append(body_content)
                
                prog_bar.progress((i + 1) / len(id_list))
            except:
                continue
        
        # Merge with separator
        final_output = "\n__SEP__\n".join(full_extracted_text)
        
        prog_bar.empty()
        status_msg.success(f"🎉 Extracted {len(full_extracted_text)} emails into 1 merged file!")
        
        st.download_button(
            label="📥 Download Merged Text File (.txt)",
            data=final_output,
            file_name="emails_bodies_merged.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    else:
        # Extract to separate files in ZIP
        zip_buf = io.BytesIO()
        
        with zipfile.ZipFile(zip_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
            for i, eid in enumerate(id_list):
                try:
                    _, msg_data = mail.fetch(eid, '(RFC822)')
                    raw_bytes = msg_data[0][1]
                    email_message = email.message_from_bytes(raw_bytes)
                    
                    # Get clean body text
                    body_content = get_email_body_text(email_message)
                    
                    if body_content:
                        # Create filename
                        if name_by_subj:
                            original_subj = email_message.get('Subject', 'no_subject')
                            subj = clean_filename(original_subj)
                            fname = f"{i+1}_{subj}.txt"
                        else:
                            fname = f"email_{i+1}.txt"
                        
                        # Write to zip
                        zf.writestr(fname, body_content.encode('utf-8'))
                    
                    prog_bar.progress((i + 1) / len(id_list))
                except:
                    continue
        
        prog_bar.empty()
        status_msg.success(f"🎉 Extracted {len(id_list)} emails into separate files!")
        
        st.download_button(
            label="📥 Download ZIP File (Separate Text Files)",
            data=zip_buf.getvalue(),
            file_name="emails_bodies_separate.zip",
            mime="application/zip",
            use_container_width=True
        )


def process_original_emails(mail, id_list, kwargs, status_msg, prog_bar):
    """
    Process emails in original format with header modifications
    
    Args:
        mail: IMAP connection object
        id_list: List of email IDs to process
        kwargs: Dictionary containing all processing options
        status_msg: Streamlit message placeholder
        prog_bar: Streamlit progress bar
    """
    # Extract parameters
    name_by_subj = kwargs.get('name_by_subj', True)
    rep_dom = kwargs.get('rep_dom', False)
    p_from = kwargs.get('p_from', '')
    std_headers = kwargs.get('std_headers', False)
    custom_headers_text = kwargs.get('custom_headers_text', '')
    mod_eid = kwargs.get('mod_eid', False)
    clean_auth = kwargs.get('clean_auth', False)
    
    zip_buf = io.BytesIO()
    
    with zipfile.ZipFile(zip_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for i, eid in enumerate(id_list):
            try:
                _, msg = mail.fetch(eid, '(RFC822)')
                raw = msg[0][1]
                
                # Split headers and body
                sep = b'\r\n\r\n'
                idx = raw.find(sep)
                if idx == -1:
                    sep = b'\n\n'
                    idx = raw.find(sep)
                
                head = raw[:idx] if idx != -1 else raw
                body = raw[idx+len(sep):] if idx != -1 else b""
                
                # Parse headers
                mime = email.message_from_bytes(head)
                original_subj = mime.get('Subject', 'no_subject')
                
                # Apply transformations
                if rep_dom and mime.get('From'):
                    n_from = re.sub(r'@[a-zA-Z0-9.-]+', f'@{p_from}', mime['From'])
                    del mime['From']
                    mime['From'] = n_from
                
                if std_headers:
                    if 'To' in mime:
                        del mime['To']
                    mime['To'] = '[*to]'
                    
                    if 'Date' in mime:
                        del mime['Date']
                    mime['Date'] = '[*date]'
                
                if custom_headers_text:
                    for line in custom_headers_text.split('\n'):
                        if ":" in line:
                            k, v = line.split(":", 1)
                            if k.strip() in mime:
                                del mime[k.strip()]
                            mime[k.strip()] = v.strip()
                
                if mod_eid and mime.get('Message-ID') and '@' in mime['Message-ID']:
                    new_mid = mime['Message-ID'].replace('@', '[EID]@', 1)
                    del mime['Message-ID']
                    mime['Message-ID'] = new_mid
                
                if clean_auth:
                    auth_headers = [
                        'DKIM-Signature', 
                        'Authentication-Results', 
                        'Received', 
                        'Received-SPF',
                        'ARC-Authentication-Results', 
                        'ARC-Message-Signature', 
                        'ARC-Seal'
                    ]
                    for h in auth_headers:
                        while h in mime:
                            del mime[h]
                
                # Reconstruct email
                fin = mime.as_bytes() + b'\r\n\r\n' + body
                
                # Create filename
                fname = f"email_{i+1}.txt"
                if name_by_subj:
                    subj = clean_filename(original_subj)
                    fname = f"{i+1}_{subj}.txt"
                
                zf.writestr(fname, fin)
                prog_bar.progress((i + 1) / len(id_list))
            
            except Exception as e:
                # Log error but continue processing
                continue
    
    prog_bar.empty()
    status_msg.success("🎉 Download Complete!")
    
    st.download_button(
        label="📥 Download ZIP File",
        data=zip_buf.getvalue(),
        file_name="emails_raw_pack.zip",
        mime="application/zip",
        use_container_width=True
    )
