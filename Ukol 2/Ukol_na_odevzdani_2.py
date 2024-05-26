import json, requests

def find_legal_form(code, czech_polozkyCiselniku):
    for item in czech_polozkyCiselniku["ciselniky"][0]["polozkyCiselniku"]:
        if item["kod"] == code:
            return item["nazev"][0]["nazev"]
while True:
    leave = input("Would you like to search for a company? Please type 'yes' or 'no':\n")

    if leave.lower() == "yes":
        ico_vs_name = input("Would you like to search the company based on ICO or its name? Please type 'ICO' or 'name':\n")
        print()

        if ico_vs_name.upper() == "ICO": 
            ico = input("Type in the required ICO:\n")
            response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico)
            data = response.json()
            print("*********************")
            print(f"The requested ID belongs to {data["obchodniJmeno"]}, registered under {data["sidlo"]["textovaAdresa"]}")
            print("*********************")
            print()

        elif ico_vs_name.lower() == "name":
            name_of_organization = input("Please type in the name of organization:\n")

            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            requested_data = {"obchodniJmeno": name_of_organization}

            response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", json=requested_data, headers=headers)
            data_from_ares = dict(response.json())

            requested_data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'

            response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", data=requested_data, headers=headers)
            polozkyCiselniku = dict(response.json())

            print("*********************")
            print(f"In total we have found {data_from_ares["pocetCelkem"]} companies, which contain \"{name_of_organization}\":")
            for company in data_from_ares["ekonomickeSubjekty"]:
                law_form = find_legal_form(company["pravniForma"], polozkyCiselniku)
                print(f"{company["obchodniJmeno"]}, {company["ico"]}, {law_form}")
            print("*********************")

    elif leave == "no":
        print("Thank you for using our service!")
        exit()

