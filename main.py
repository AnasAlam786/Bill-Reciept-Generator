import streamlit as st
from CreatePDF import Reciept, FillCSV
from datetime import datetime
import pandas as pd

st.title("Reciept Generation")
AC = st.text_input("Account Number")
name = st.text_input("Name")
amount = st.text_input("Amount")
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

check=st.checkbox("Is There Any Due Payment?")
if check:
  payed = st.text_input("Amount Recieved")
elif check==False:
  payed=amount


#st.markdown(html_string, unsafe_allow_html=True)

if st.button("Submit"):
  try:
    due=str(int(amount)-int(payed))
    Reciept(AC, name, amount,payed,due, str(time))
    FillCSV(AC, name, amount,payed,due, str(time),"data.csv")
    st.success("Reciept Generated")

  except Exception as e:
    st.error(f"Reciept Not Generated! Error = {e}",icon="🚨")

df = pd.read_csv('data.csv')
st.dataframe(df, use_container_width=True)
