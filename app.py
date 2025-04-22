import requests, re
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)
URL = "https://scaur.kippfordweather.uk/index.htm"

def get_windchill():
    try:
        response = requests.get(URL, timeout = 10)
        soup = BeautifulSoup(response.content, "html.parser")
    
        for row in soup.find_all("tr", class_="td_temperature_data"):
            cells = row.find_all("td")
      
            if cells and "Windchill" in cells[0].text:
                return re.findall(r"[\d]*[.][\d]+", cells[1].text.strip())
   
    except Exception as e:
        return f"Error: {e}"

    return "Unavailable"
      
@app.route("/kippford/weather")
def temperature():
    return jsonify({"windchill": get_windchill()})
