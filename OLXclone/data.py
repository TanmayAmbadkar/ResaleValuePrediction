import json
import requests
import pandas
from bs4 import BeautifulSoup
import sys


querry_url = "https://www.olx.in/api/relevance/search?category=1725&location=4058732&page=1"
parameters=[]

# def get_data_from_url(url):
#     r = requests.get(url)
#     c = r.content
#
#     soup = BeautifulSoup(c, 'html.parser')
#     body = json.loads(soup.text)
#
#     allCars = []

    # Extracting Features
    # for car in body['data']:
    #     try:
    #         currentCar = {}
    #         currentCar['Price'] = car['price']['value']['raw']
    #         for meta_parameter in ['title','description','created_at']:
    #             if car[meta_parameter]:
    #                 currentCar[meta_parameter] = car[meta_parameter]
    #         for parameter in car['parameters']:
    #             if parameter['key'] == 'year':
    #                 currentCar["Year"] = parameter['value']
    #             elif parameter['key'] == 'petrol':
    #                 currentCar["fuel"] = parameter['value']
    #             elif parameter['key'] == 'mileage':
    #                 currentCar["Kms"] = parameter['value']
    #             elif parameter['key'] == 'model':
    #                 currentCar["model"] = parameter['value']
    #             elif parameter['key'] == 'make':
    #                 currentCar["make"] = parameter['value']
    #         currentCar["City"] = car['locations_resolved']['ADMIN_LEVEL_3_name']
    #         currentCar["Area"] = car['locations_resolved']['SUBLOCALITY_LEVEL_1_name']
    #         allCars.append(currentCar)
    #
    #     # Error Logging
    #     except:
    #         print("Unexpected error for post", sys.exc_info()[0])
    #
    # # Check if we have next page
    # nextPage = False
    # if len(body['data']) > 0 and ('next_page_url' in body['metadata']):
    #     nextPage = True
    # return [allCars, nextPage]


def get_data_from_url(url):
    r = requests.get(url)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    body = json.loads(soup.text)

    score=[]

    for h in body['data']:
        try:
            score.append(h['score'])
        except:
            print('error occured')
    return score


print(get_data_from_url(querry_url))
