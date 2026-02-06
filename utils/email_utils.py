"""
Email processing utilities for IMAP tool
"""
import re
from email.header import decode_header

def decode_header_text(header_value):
    """
    Decode email header text handling various encodings
    
    Args:
        header_value: Raw header value to decode
        
    Returns:
        Decoded string or 'no_subject' if empty
    """
    if not header_value:
        return "no_subject"
    
    try:
        decoded_list = decode_header(header_value)
        text_parts = []
        
        for content, encoding in decoded_list:
            if isinstance(content, bytes):
                if encoding:
                    try:
                        content = content.decode(encoding)
                    except:
                        content = content.decode('utf-8', 'ignore')
                else:
                    content = content.decode('utf-8', 'ignore')
            text_parts.append(str(content))
        
        return "".join(text_parts)
    except:
        return header_value


def clean_filename(subject):
    """
    Clean email subject to create valid filename
    
    Args:
        subject: Email subject string
        
    Returns:
        Cleaned filename string
    """
    if not subject:
        return "no_subject"
    
    decoded_subj = decode_header_text(subject)
    # Remove special characters but keep accented letters
    clean = re.sub(r'[^a-zA-Z0-9\s_\-\u00C0-\u017F]', '', decoded_subj)
    # Limit length and replace spaces
    return clean.strip().replace(' ', '_')[:60]


def clean_html_to_plain(html_content):
    """
    Strip HTML tags and convert to plain text using regex
    
    Args:
        html_content: HTML string to clean
        
    Returns:
        Plain text string
    """
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', ' ', html_content)
    # Collapse whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean


def get_email_body_text(msg_obj):
    """
    Extract plain text body from email message, preferring plain text over HTML
    
    Args:
        msg_obj: email.message.Message object
        
    Returns:
        Extracted body text as string
    """
    body_text = ""
    
    if msg_obj.is_multipart():
        # Walk through message parts
        for part in msg_obj.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            
            # Skip attachments
            if 'attachment' in cdispo:
                continue
            
            try:
                payload = part.get_payload(decode=True)
                if not payload:
                    continue
                
                decoded_payload = payload.decode('utf-8', 'ignore')
                
                if ctype == 'text/plain':
                    return decoded_payload  # Best case, return immediately
                elif ctype == 'text/html' and not body_text:
                    # Store HTML as fallback
                    body_text = clean_html_to_plain(decoded_payload)
            except:
                continue
    else:
        # Single part message
        try:
            payload = msg_obj.get_payload(decode=True)
            if payload:
                decoded = payload.decode('utf-8', 'ignore')
                
                if msg_obj.get_content_type() == 'text/plain':
                    body_text = decoded
                elif msg_obj.get_content_type() == 'text/html':
                    body_text = clean_html_to_plain(decoded)
        except:
            pass
    
    return body_text


def detect_duplicates(email_list):
    """
    Detect duplicate emails based on Message-ID or Subject+From combination
    
    Args:
        email_list: List of email data dictionaries
        
    Returns:
        Tuple of (unique_emails, duplicates)
    """
    seen_ids = set()
    seen_combos = set()
    unique_emails = []
    duplicates = []
    
    for idx, email_data in enumerate(email_list):
        msg_id = email_data.get('message_id', '')
        subject = email_data.get('subject', '')
        from_addr = email_data.get('from', '')
        
        # Create unique identifier
        combo = f"{subject}|{from_addr}"
        
        is_duplicate = False
        reason = ""
        
        # Check Message-ID if available
        if msg_id and msg_id in seen_ids:
            is_duplicate = True
            reason = "Duplicate Message-ID"
        # Check Subject+From combination
        elif combo in seen_combos:
            is_duplicate = True
            reason = "Duplicate Subject+From"
        
        if is_duplicate:
            duplicates.append({
                'index': idx + 1,
                'subject': subject,
                'reason': reason
            })
        else:
            unique_emails.append(email_data)
            if msg_id:
                seen_ids.add(msg_id)
            seen_combos.add(combo)
    
    return unique_emails, duplicates
