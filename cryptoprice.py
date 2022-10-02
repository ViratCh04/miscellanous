from requests import Session
import json
import pprint

def getInfo (currency):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url

    parameters = { 'slug': currency, 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '2fee0f1e-7e12-440c-8d15-aea2c6026889'
    } # My API key is used here

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    info = json.loads(response.text)
    id = list(json.loads(response.text)['data'].keys())[0]
    info = info['data'][id]['quote']['USD']['price']

    pprint.pprint(info)
        

query = input("Input the currency: ")
currency = query.replace(' ', '-')
getInfo(currency.lower()) # Calling the function to get the statistics

# Going to add more features once free