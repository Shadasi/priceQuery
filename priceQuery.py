import xml.etree.ElementTree as ET
import requests
import sys, getopt
import csv

eve_central_base_url = 'http://api.eve-central.com/api/marketstat'

#jita_id = 30000142      # Jita's solar system ID

def get_system():
    sys_name = input("Please enter Jita, Hek, Amarr, Rens, Dodixe, or All:  ")
    if sys_name == 'Hek':
        return 30002053
    elif sys_name == 'Amarr':
        return 30002187
    elif sys_name == 'Rens':
        return 30002510
    elif sys_name == 'Dodixe':
        return 30002659
    elif sys_name == 'All':
        print('This Feature is not Available yet.')
        sys.exit()
    else:
        return 30000142



def query(item_id, system_id):
    payload = {
        'typeid': item_id,
        'usesystem': system_id,
    }

    req = requests.post(eve_central_base_url, data=payload)
    response = req.text

    tree = ET.fromstring(response)
    marketstat = tree.find('marketstat')
    type_ = marketstat.find('type')
    buy = type_.find('buy')
    buy_max = buy.findtext('max')
    sell = type_.find('sell')
    sell_vol = sell.findtext('volume')
    sell_median = sell.findtext('median')

    print('Item ID:            ', item_id)
    print('Median Sell Price:  ', sell_median)
    print('Sell Volume:        ', sell_vol, '\n')
    


def find_id(item_name):
    with open('typeids.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if item_name == row[1]:
                return row[2]
        print('Not Found')
        sys.exit()



def main():

    s_id = get_system()

    input_id = input("Enter an item Name:  ")

    while(input_id != 'quit'):
        found_id = find_id(input_id)
        query(found_id, s_id)
        input_id = input("Enter an item Name:  ")

    sys.exit()



if __name__ == "__main__":
    main()