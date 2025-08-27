import streamlit as st
import PyPDF2
import re
import pandas as pd
from io import StringIO
#PyPDF2==3.0.1
#openpyxl==3.1.5
st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
        }
    </style>
    """
)



def extract_customer_name(pdf_path,para1):
    match = re.search(f"{para1}\s*(.*)", text, re.IGNORECASE).group(1).strip()   
    return match


# Usage
with st.expander("Your PDF"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        reader = PyPDF2.PdfReader(uploaded_file)
        page = reader.pages[0]
        text = page.extract_text()
        mfa1 = st.text_input("Invoice Number", value=extract_customer_name('','Invoice Number'))
