import requests
import json
import argparse
import pprint


def get_card_info(card):
    try:
        print(f"Get card info {card} ", end="")
        url = f"https://lookup.binlist.net/{card}"
        request = requests.get(url, headers={'Accept-Version': "3"})
        data = json.loads(request.content.decode())
        print(f"-> Ok ({request.status_code})")
    except json.decoder.JSONDecodeError as ex:
        data = {"Error": ex.msg}
        print(f"->Error ({request.status_code})")
    return data


def get_cards_from_file(filename):
    banks = set()
    with open (filename, "r") as file:
        cards = json.load(file)
        for card in cards:
            card_number = str(card["CreditCard"]["CardNumber"])
            data = get_card_info(card_number[0:8])
            if "bank" in data:
                banks.add(data["bank"]["name"])
    return sorted(banks)


def get_card_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--card", type=str, dest="card", help="Card name")
    parser.add_argument("-f", "--file", type=str, dest="file", help="File name")
    args = parser.parse_args()
    if args.card is not None:
        return get_card_info(args.card)
    elif args.file is not None:
        return get_cards_from_file(args.file)


if __name__ == "__main__":
    info = get_card_data()
    print("-"*70)
    pprint.pprint(info)
