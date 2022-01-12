#!/usr/bin/env python3

import webbrowser
from time import sleep


# user chooses a category of websites to be opened
def offercategory():
    print(f"( 1 ) Social networks\n"
          f"( 2 ) Crypto currency\n"
          )

    return


def askcategory():
    category = input("Please choose a category: ")

    return category


def menu(category):
    match category:
        case "1":
            print(f"\nYou chose Social Networks")
            socialnetworks()
            yesorno = input(f"\nDo you want to open another batch of websites? Please type \"y\" for yes or \"n\" for no: ")
            match yesorno:
                case "y":
                    offercategory()
                    additional_category = askcategory()
                    menu(additional_category)
                case "n":
                    exit()
                case _:
                    print(f"Please type \"y\" for yes or \"n\" for no")
                    additional_category = askcategory()
                    menu(additional_category)
        case "2":
            print(f"\nYou chose Crypto currency")
            cryptocurrency()
            yesorno = input(f"\nDo you want to open another batch of websites? Please type \"y\" for yes or \"n\" for no: ")
            match yesorno:
                case "y":
                    offercategory()
                    additional_category = askcategory()
                    menu(additional_category)
                case "n":
                    exit()
                case _:
                    print(f"Please type \"y\" for yes or \"n\" for no")
                    additional_category = askcategory()
                    menu(additional_category)
        case _:
            print(f"Please choose a given number.")


def socialnetworks():
    # reddit
    sleep(1)
    webbrowser.open_new('https://reddit.com')

    # twitch
    sleep(1)
    webbrowser.open_new('https://twitch.tv')

    # twitter
    sleep(1)
    webbrowser.open_new('https://twitter.com')

    # youtube
    sleep(1)
    webbrowser.open_new('https://youtube.com')

    return


def cryptocurrency():
    # CoinMarketCap
    sleep(1)
    webbrowser.open_new('https://coinmarketcap.com/')

    # cointelegraph
    sleep(1)
    webbrowser.open_new('https://cointelegraph.com/')

    # fear & greed index
    sleep(1)
    webbrowser.open_new('https://alternative.me/crypto/fear-and-greed-index/')

    # binance
    sleep(1)
    webbrowser.open_new('https://www.binance.com/en')

    return


print(f"\nHello! This script should be a handy little helper. Its task is to quickly open a couple of websites you "
      f"often visit. Please choose one category.\nAfter choosing a category a couple of handy websites will be opened in"
      f"your primary browser. After that you get the chance to choose another category or close this program.\n")

offercategory()

category_chosen = askcategory()

menu(category_chosen)
