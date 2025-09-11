import requests
from secret import secrets

url1 = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={secrets['API1_TOKEN']}'
url2 = 'https://catfact.ninja/fact'
url3 = 'https://api.agify.io/?name=vadim'

def bit(url:str):
    response = requests.get(url)
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']

def cats(url:str):
    response = requests.get(url)
    return response.json()['fact']

def name(url:str):
    response = requests.get(url)
    data  = response.json()
    return f'{data['name']} approximate age: {data['age']}'



def main():
    print(bit(url1))
    print(cats(url2))
    print(name(url3))

if __name__ == '__main__':
    main()
