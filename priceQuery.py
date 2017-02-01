import xml.etree.ElementTree as ET
import requests
import sys, getopt

eve_central_base_url = 'http://api.eve-central.com/api/marketstat'

#tritanium_id = str(sys.argv[1])    # Type ID for Tritanium 
jita_id = 30000142      # Jita's solar system ID

filename = 'output.txt'
target = open(filename, 'w')

target.write("JITA PRICES:  \n\n")
for x in range(34, 41):
    result = ''
    if x == 34:
        result = 'Tritatnium'
    elif x == 35:
        result = 'Pyerite'
    elif x == 36:
        result = 'Mexallon'
    elif x == 37:
        result = 'Isogen'
    elif x == 38:
        result = 'Nocxium'
    elif x == 39:
        result = 'Zydrine'
    else:
        result = 'Megacyte'
    
    target.write(result)
    target.write("\n")

    payload = {
    'typeid': x,
    'usesystem': jita_id,
    }

    r = requests.post(eve_central_base_url, data=payload)

    response = r.text

    tree = ET.fromstring(response)
    marketstat = tree.find('marketstat')
    type_ = marketstat.find('type')
    buy = type_.find('buy')
    buy_max = buy.findtext('max')
    sell = type_.find('sell')
    sell_vol = sell.findtext('volume')
    sell_median = sell.findtext('median')

    target.write("Max Unit Price (Buy Order):  ")
    target.write(buy_max)
    target.write("\nMedian Unit Price (Sell Order):  ")
    target.write(sell_median)
    target.write ("\nVolume in System:  ")
    target.write(sell_vol)
    target.write("\n\n")

target.close()