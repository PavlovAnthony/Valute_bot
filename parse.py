import requests
def parse_exchange(name_valute):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
     
    quote= res['Valute'][name_valute]['Nominal'], res['Valute'][name_valute]['Name'], res['Valute'] [name_valute]['Value']
    
    return ( ' '.join(str(x) for x in quote))
