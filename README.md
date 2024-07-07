# Receipt Generation App

This is a Streamlit-based application that generates receipts in PDF format and keeps a log of transactions in a CSV file. The application allows users to input account details, generate receipts, and view transaction logs.

## Features

- Input account number, name, and amount to generate a receipt.
- Option to specify if there is any due payment.
- Automatically calculates due amount if applicable.
- Generates a PDF receipt and displays it within the app.
- Logs transaction details in a CSV file.
- Displays a table of all logged transactions.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd receipt-generation-app
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501` to access the app.

3. Enter the required details:
    - Account Number
    - Name
    - Amount

4. If there is any due payment, check the box and enter the amount received.

5. Click the "Submit" button to generate the receipt.

6. The generated receipt will be displayed within the app, and the transaction details will be logged in `data.csv`.

7. You can view the table of all logged transactions at the bottom of the app.

## File Structure

- `app.py`: The main Streamlit application script.
- `CreatePDF.py`: Module containing functions `Reciept` and `FillCSV` for PDF generation and CSV logging.
- `data.csv`: CSV file to store transaction logs.
- `README.md`: This readme file.

## Dependencies

- streamlit
- pandas
- base64
- pytz

Make sure to include `CreatePDF.py` in the same directory as `app.py`. The `CreatePDF.py` file should contain the implementation for `Reciept` and `FillCSV` functions used in the app.
