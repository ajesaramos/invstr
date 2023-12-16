import cleo
import json
import requests

## not sure this should be like this.
# sources = {'Wise': 'https://wise.com/', 'Yfinance': '', 'Google': '', 'Dividend': ''}

def do_currency():
    q = input("Enter currency query: ")
    q_values = q.split()

    f = q_values[0]
    t = q_values[1]
    amm = q_values[2]

    r = requests.get(f'https://wise.com/rates/live?source={f}&target={t}')
    
    r_dict = json.loads(r.text)
    query_value_ammount = float(amm) * r_dict['value']
    print(f"{amm} {r_dict['source']} = {query_value_ammount} {r_dict['target']}")

