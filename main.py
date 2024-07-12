import streamlit as st
from CreatePDF import Reciept, FillCSV, getData
from datetime import datetime
import pandas as pd
import base64
from pytz import timezone

#st.title("Reciept Generation")
AC = str(st.text_input("Account Number"))
name = st.text_input("Name")
amount = st.text_input("Amount")
time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')

check=st.checkbox("Is There Any Due Payment?")
if check:
  payed = st.text_input("Amount Recieved")
elif check==False:
  payed=amount


#st.markdown(html_string, unsafe_allow_html=True)

if st.button("Submit"):
  try:
    due=str(int(amount)-int(payed))
    FillCSV(AC, name, amount,payed,due, str(time))
    Reciept(AC, name, amount,payed,due, str(time))

    with open("receipt1.pdf", "rb") as pdf_file:
      encoded_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{encoded_pdf}" width="710" height="480" type="application/pdf"></iframe>'

    # Display the PDF in Streamlit
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    #st.success("Reciept Generated")

  except Exception as e:
    st.error(f"Reciept Not Generated! Error = {e}",icon="🚨")

try:
  df = getData()
  df['Account Number'] = df['Account Number'].astype(str)
  st.dataframe(df, use_container_width=True)
  
except Exception as e:
  st.error(f"Problem With Data File! Error = {e}",icon="🚨")
