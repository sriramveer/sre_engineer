import requests
import json

def fetch_country_data():
    url = "https://www.travel-advisory.info/api"
    response = requests.get(url)
    return response.json()

def lookup_country_codes(country_codes):
    data = fetch_country_data()
    result = {}

    for country_code in country_codes:
        for country in data:
            if country["country_code"].lower() == country_code.lower():
                result[country_code] = country["country_name"]
                break

    return result

def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    country_codes = ["AU", "US", "GB"]
    result = lookup_country_codes(country_codes)

    print("Result:")
    for country_code, country_name in result.items():
        print(f"{country_code}: {country_name}")

    data = fetch_country_data()
    save_data_to_file(data, "data.json")