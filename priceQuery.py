import xml.etree.ElementTree as ET
import requests
import sys, getopt
import csv

eve_central_base_url = 'http://api.eve-central.com/api/marketstat'

#tritanium_id = str(sys.argv[1])    # Type ID for Tritanium 
jita_id = 30000142      # Jita's solar system ID

#filename = 'output.txt'
#target = open(filename, 'w')
#target.write("JITA PRICES:  \n\n")

#for x in range(34, 41):
    #result = ''
    #if x == 34:
    #    result = 'Tritatnium'
    #elif x == 35:
    #    result = 'Pyerite'
    #elif x == 36:
    #    result = 'Mexallon'
    #elif x == 37:
    #    result = 'Isogen'
    #elif x == 38:
    #    result = 'Nocxium'
    #elif x == 39:
    #    result = 'Zydrine'
    #else:
    #    result = 'Megacyte'
    
    #target.write(result)
    #target.write("\n")

    #target.write("Max Unit Price (Buy Order):  ")
    #target.write(buy_max)
    #target.write("\nMedian Unit Price (Sell Order):  ")
    #target.write(sell_median)
    #target.write ("\nVolume in System:  ")
    #target.write(sell_vol)
    #target.write("\n\n")

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
                print(row[1], row[2])
                return row[2]
        print('Not Found')
        sys.exit()


input_id = input("Enter an item Name:  ")


while(input_id != 'quit'):
    found_id = find_id(input_id)
    query(found_id, jita_id)
    input_id = input("Enter an item Name:  ")

#find_id('Tritanium')

#target.close()