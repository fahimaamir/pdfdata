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


mdata = pd.DataFrame({
        'Title': [],
        'Value': [],
        
    })


mdata2 = pd.DataFrame({
        'Title': [],
        'Value': [],
        
    })



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
        
        mfa1 = st.text_input("Landlord Name", value=extract_customer_name('','Landlord Name:'))
        mfa2 = st.text_input("Passport/Emirates ID Number ", value=extract_customer_name('','Passport/Emirates ID Number:'))
        mfa3 = st.text_input("Expiry: ", value=extract_customer_name('','Expiry:'))
        mfa4 = st.text_input("Property Type:", value=extract_customer_name('','Property Type'))
        mfa5 = st.text_input("Property Current Status", value=extract_customer_name('','Property Current Status'))
        mfa6 = st.text_input("Vacating Date", value=extract_customer_name('','Vacating Date:'))
        mfa7 = st.text_input("Building Name ", value=extract_customer_name('','Building Name'))
        mfa8 = st.text_input("Property No ", value=extract_customer_name('',' Property No:'))
        mfa9 = st.text_input("Street Name:: ", value=extract_customer_name('','Street Name:'))
        mfa10 = st.text_input("Community", value=extract_customer_name('','Community:'))
        mfa11 = st.text_input("Plot Number", value=extract_customer_name('','Plot Number'))
        mfa12 = st.text_input("Apt (Sq Ft)", value= 'Input Value')
        mfa13 = st.text_input("Bedrooms:", value=extract_customer_name('','Bedrooms:'))
        mfa14 = st.text_input("Parking:", value=extract_customer_name('','Parking:'))
        mfa15 = st.text_input("Rental Amount/Sale #Amount:", value=extract_customer_name('','Amount:'))
        mfa16 = st.text_input("Other", value= 'Input Value')
        mdata.loc[len(mdata)] = ['Landlord Name', mfa1]
        mdata.loc[len(mdata)] = ['Passport/Emirates ID Number', mfa2]
        mdata.loc[len(mdata)] = ['Expiry', mfa3]
        mdata.loc[len(mdata)] = ['Property Type', mfa4]
        mdata.loc[len(mdata)] = ['Property Current Status', mfa5]
        mdata.loc[len(mdata)] = ['Vacating Date', mfa6]
        mdata.loc[len(mdata)] = ['Building Name', mfa7]
        mdata.loc[len(mdata)] = ['Property No', mfa8]
        mdata.loc[len(mdata)] = ['Street Name', mfa9]
        mdata.loc[len(mdata)] = ['Community', mfa10]
        mdata.loc[len(mdata)] = ['Plot Number', mfa11]
        mdata.loc[len(mdata)] = ['Apt (Sq Ft)', mfa12]
        mdata.loc[len(mdata)] = ['Bedrooms', mfa13]
        mdata.loc[len(mdata)] = ['Parking', mfa14]
        mdata.loc[len(mdata)] = ['Rental Amount/Sale #Amount', mfa15]
        mdata.loc[len(mdata)] = ['Other ', mfa16]
        
        st.write(mdata)

with st.expander("Sample PDF"):
    uploaded_file = st.file_uploader("Choose a file2")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        reader = PyPDF2.PdfReader(uploaded_file)
        page = reader.pages[0]
        text = page.extract_text()
        mfa1 = st.text_input("Invoice Number", value=extract_customer_name('','Invoice Number'))
        mfa2 = st.text_input("Order Number", value=extract_customer_name('','Order Number'))
        mfa3 = st.text_input("Invoice Date", value=extract_customer_name('','Invoice Date'))
        mfa4 = st.text_input("Due Date", value=extract_customer_name('','Due Date'))
        mfa5 = st.text_input("Total Due", value=extract_customer_name('','Total Due'))
        mfa6 = st.text_input("Sub Total", value=extract_customer_name('','Sub Total'))
        mfa7 = st.text_input("Tax", value=extract_customer_name('','Tax'))
        mfa8 = st.text_input("Total", value=extract_customer_name('','Total'))
        
        mdata2.loc[len(mdata2)] = ['Invoice Number', mfa1]
        mdata2.loc[len(mdata2)] = ['Order Number', mfa2]
        mdata2.loc[len(mdata2)] = ['Invoice Date', mfa3]
        mdata2.loc[len(mdata2)] = ['Due Date', mfa4]
        mdata2.loc[len(mdata2)] = ['Total Due', mfa5]
        mdata2.loc[len(mdata2)] = ['Sub Total', mfa6]
        mdata2.loc[len(mdata2)] = ['Tax', mfa7]
        mdata2.loc[len(mdata2)] = ['Total', mfa8]
        
        st.write(mdata2)
