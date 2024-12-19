from api_client import APIClient
from data_processor import DataProcessor
from excel_writer import ExcelWriter

def main():
    api_key = "IiB22hb2ZTm4Dtux7A2bMIpBTHzyCOgs"
    symbols = ["AAPL", "MSFT", "GOOG"]

    api_client = APIClient(api_key)
    data_processor = DataProcessor(api_client)
    excel_writer = ExcelWriter("financial_data.xlsx")

    headers = [
        "Symbol", "FCF Margin (%)", "5yr FCF CAGR (%)", "5yr FCF RSq",
        "5yr FCF Margin Exp (%)", "FCF ROC (%)", "5yr Min FCF ROC (%)",
        "Difference (%)", "Payout Ratio (%)", "FCF Yield (%)"
    ]
    excel_writer.write_headers(headers)

    for symbol in symbols:
        try:
            data = data_processor.process_company_data(symbol)
            excel_writer.add_row([data[header] for header in headers])
        except Exception as e:
            print(f"Error processing {symbol}: {e}")

    excel_writer.save()

if __name__ == "__main__":
    main()
