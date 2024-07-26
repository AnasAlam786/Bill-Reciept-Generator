import streamlit as st
from CreatePDF import Reciept, FillCSV,getData
from datetime import datetime,timedelta
import pandas as pd
import base64
from pytz import timezone

#st.title("Reciept Generation")
AC = str(st.text_input("Account Number"))
name = st.text_input("Name")
amount = st.text_input("Amount")
time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
payed = st.text_input("Amount Recieved")

if payed=="":
  payed=amount


if st.button("Submit"):
  try:
    due=str(int(amount)-int(payed))
    Reciept(AC, name, amount,payed,due, str(time))

    with open("reciept1.pdf", "rb") as pdf_file:
      encoded_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')

    pdf_display = f'<iframe src="data:application/pdf;base64,{encoded_pdf}" width="710" height="480" type="application/pdf"></iframe>'

    # Display the PDF in Streamlit
    st.markdown(pdf_display, unsafe_allow_html=True)
    FillCSV(AC, name, amount,payed,due, str(time))

    
    #st.success("Reciept Generated")

  except Exception as e:
    st.error(f"Reciept Not Generated! Error = {e}",icon="🚨")

try:
  df = getData()
  df = df.iloc[::-1].reset_index(drop=True)
  df['Account Number'] = df['Account Number'].astype(str)
  df["Time"]=pd.to_datetime(df["Time"])
  
  today=datetime.now().date()
  yesterday=today-timedelta(days=1)
  before=today-timedelta(days=2)

  todayDF=df[df['Time'].dt.date==today]
  yesterdayDF=df[df['Time'].dt.date==yesterday]
  before=df[df['Time'].dt.date==before]
  

  st.dataframe(todayDF, use_container_width=True)
  st.dataframe(yesterdayDF, use_container_width=True)
  st.dataframe(before, use_container_width=True)
  
except Exception as e:
  st.error(f"Problem With Data File! Error = {e}",icon="🚨")
