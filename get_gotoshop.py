import json
import requests
from config import TOKEN, MASTER
from telegram.ext import Updater
from telegram import ParseMode

token = TOKEN
admin_id = MASTER

updater = Updater(token)

def dairyProducts():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '5787,418,600056,5724,5786'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/DairyProducts.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def baking():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '424,5748,5904'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Baking.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def cakes():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '5749'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Cakes.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def sweets():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '4748,600176'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Sweets.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def alcohol():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '417,6761,2107,2605,2933,600122,1926,5887'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Alcohol.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def meat():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '5805,656797,4628'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Meat.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def fish():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '600065'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Fish.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def beer():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '414'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Beer.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def wine():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '421'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Wine.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def brandy():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '2364'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Brandy.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def fruitsAndVegetables():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '6633,6569,6610,6566,6572,6646,6586,6703,6655,6658,503759'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/FruitsAndVegetables.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def butterSpreadMargarine():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '5827'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/ButterSpreadMargarine.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def yogurtAndMore():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '1954'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/YogurtAndMore.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def sir():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '429'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Sir.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def kovbas():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '600060,600062,600114'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Kovbas.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def pechivo():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '2229,600057'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Pechivo.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def groats():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '6259,4682,4686,4688'),
        ('city_id', '438'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/Groats.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)

def produkts_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '430,6665,5793,6586,600196,2660,2126,431,4682,427,1568'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/produkts_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)

def produkts2_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '1876,2229,5904,4748,600124'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/produkts2_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)

def milk_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '429,428,1954'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/milk_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def meet_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '432,600060'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/meet_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def alcohol_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '414,5723,417,2364,2107,421'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/alcohol_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)

def ximia_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '630'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/ximia_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)


def kava_pr():
    params = (
        ('limit', '1000'),
        ('offset', '0'),
        ('pcategories_ids', '1868'),
        ('city_id', '15397'),
        ('fields',
         'id,name,name2,shops_ids,url,noted,discount_url,discount_name,date,notalladdr,image336,imagefull,brands,'
         'pricebefore,priceafter,discount_type,discount,externalurl,countPlus,countMinus,comments,desc,color,'
         'daystitle,liked'),
    )

    response = requests.get('https://gotoshop.ua/apiv3/products/', params=params)

    result_json = response.json()

    with open("gotoshop/kava_pr.json", "w", encoding="utf-8") as file_json:
        json.dump(result_json['products'], file_json, ensure_ascii=False, indent=8)

def updated():
    dairyProducts()
    sir()
    baking()
    sweets()
    alcohol()
    meat()
    fish()
    beer()
    wine()
    brandy()
    kovbas()
    cakes()
    pechivo()
    groats()
    fruitsAndVegetables()
    butterSpreadMargarine()
    yogurtAndMore()
    produkts_pr()
    produkts2_pr()
    milk_pr()
    meet_pr()
    alcohol_pr()
    ximia_pr()
    kava_pr()





def send_msg(chat_id, message):
    updater.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


def main():
    updated()



main()










