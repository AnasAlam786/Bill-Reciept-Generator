import fitz
import gspread
from google.oauth2.service_account import Credentials
from random import randint
from num2words import num2words
import pandas as pd

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1i44CXmnsL5WApTnS9QRhM4ZVOU9OngeFL9yJ-GIHY14"
sheet = client.open_by_key(sheet_id).sheet1

def Reciept(AC, name, amount,payed,due,time):

  payed_word=f"({num2words(payed).title()} Only)"

  pdf_document = fitz.open("reciept.pdf")
  page = pdf_document[0]

  # Account Number
  page.insert_text((209, 180),
                   AC, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount
  page.insert_text((215, 195),
                   amount, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount Payed
  page.insert_text((215,211),        
                   payed, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount Due
  page.insert_text((215,244.5), 
                   due, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount in words
  page.insert_text((209, 228), 
                   payed_word, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Saseed Sankhya last 3digit ramdom
  page.insert_text((254, 146), 
                   str(randint(100, 999)), fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))


  #Name
  page.insert_text((430, 179), 
                   name, fontsize=11, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))
  #Date and Time
  page.insert_text((430, 163), 
                   time, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Date and Time
  page.insert_text((430, 277), 
                   time, fontsize=10,
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Sandarbh sankhya
  page.insert_text((430, 146), 
                   str(randint(10000, 99999)), fontsize=10,
                   fontname = "Times-Bold",
                   color=(0, 0, 0))



  # Save the updated PDF to a new file
  pdf_document.save("reciept1.pdf")
  pdf_document.close()


def FillCSV(AC, name, amount,payed,due,time):
  sheet.append_row( [name,amount, payed, due, AC, time])

def getData():
  data = sheet.get_all_records()

  return pd.DataFrame(data)
