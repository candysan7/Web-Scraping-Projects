import os
from twilio.rest import Client
import time
from pprint import pprint
import cloudscraper
import requests
from bs4 import BeautifulSoup
import sys 


def sendtext(url): 
    while True:
        # url='https://owlandgoosegifts.com/products/squishmallow-nightmare-before-christmas-zero-12-inch...?fbclid=IwAR2Rmqfy8bdZEdZ58FWEuVm9GmSkjwfos1aD_Cd0SdOpJsJOhcZkDXbRiV0'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser') #shows format 
        # pprint(soup)

        searcher  = soup.findAll('option', None)
        # print(searcher)
        if 'Check Back Soon!' in str(searcher): 
            print('Still Not In Stock')

        elif 'Check Back Soon!' not in str(searcher): 
            print('In stock!')

            client = Client('id', 'id')

            client.api.account.messages.create(
            to="+16266352542",
            from_="+18438656822",
            body=" 'IN STOCK NOW'"+ str(url))

        time.sleep(60) # runs a loop every 60 secs

if __name__ == "__main__":
    sendtext(str(sys.argv[1]))  ### command line: python3 url 
