import requests


def fetch_metar_data(icao_code):
    url = f"https://aviationweather.gov/api/data/metar?ids={icao_code}&format=raw&taf=false&date=0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    icao_code = input("Enter the ICAO code of the airport: ")
    metar_data = fetch_metar_data(icao_code)
    if metar_data:
        print("METAR Data: ")
        print(metar_data)
    else:
        print("Failed to fetch METAR data.")


if __name__ == "__main__":
    main()
