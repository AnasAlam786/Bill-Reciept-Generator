import fitz

from random import randint
from num2words import num2words
import pandas as pd



def Reciept(AC, name, amount,payed,due,time):
    
  
  amount_word=f"({num2words(amount).title()} Only)"

  pdf_document = fitz.open("receipt.pdf")
  page = pdf_document[0]

  # Account Number
  page.insert_text((192, 159),
                   AC, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))
  #Name
  page.insert_text((445, 158), 
                    name, fontsize=11, 
                    fontname = "Times-Bold",
                    color=(0, 0, 0))
  #Date and Time
  page.insert_text((445, 140), 
                    time, fontsize=10, 
                    fontname = "Times-Bold",
                    color=(0, 0, 0))
                 
  #Amount
  page.insert_text((198, 177),
                   amount, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Saseed Sankhya last 3digit ramdom
  page.insert_text((237, 120), 
                   str(randint(100, 999)),                          fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount Due
  page.insert_text((198,235), 
                   due, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount Payed
  page.insert_text((198,190),        
                   payed, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Amount in words
  page.insert_text((192, 216), 
                   amount_word, fontsize=10, 
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

  #Date and Time
  page.insert_text((445, 251), 
                   time, fontsize=10,
                   fontname = "Times-Bold",
                   color=(0, 0, 0))
  #Sandarbh sankhya
  page.insert_text((445, 121), 
                   str(randint(10000, 99999)), fontsize=10,
                   fontname = "Times-Bold",
                   color=(0, 0, 0))

    # Save the updated PDF to a new file
  pdf_document.save("receipt1.pdf")
  pdf_document.close()


def FillCSV(AC, name, amount,payed,due,time,file):
  df = pd.read_csv(file)
  data={"Name":name,
     "Amount":amount,
     "Payed Amount":payed,
     "Due Amount":due,
     "Account Number":AC,
     "Time":time}

  df = df._append(data, ignore_index=True)
  df.to_csv('data.csv', index=False)

def ShowData(file):
  st.dataframe(fle, use_container_width=True)

"""with col2:
                   #if st.button("Reset Text"):
                     st.markdown('''

                             <div class="pdf-container">
                         <iframe src="https://online.publuu.com/572124/1284480" width="650" height=900></iframe>
                     </div>
                             ''' ,unsafe_allow_html=True)"""
