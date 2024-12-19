import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://financialmodelingprep.com/api/v3"

    def fetch_data(self, endpoint, symbol):
        url = f"{self.base_url}/{endpoint}/{symbol}?apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_financial_data(self, endpoint, symbol, key):
        data = self.fetch_data(endpoint, symbol)
        return [item[key] for item in data[:5]]
