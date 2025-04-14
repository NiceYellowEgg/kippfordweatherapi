from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
URL = "https://scaur.kippfordweather.uk/index.htm"

def get_temperature():
    try:
        response = requests.get(URL, timeout = 10)
        soup = BeautifulSoup(response.content, "html.parser")
    
        for row in soup.find_all("tr", class_="td_temperature_data"):
            cells = row.find_all("td")
      
            if cells and "Temperature" in cells[0].text:
                return cells[1].text.strip()
   
    except Exception as e:
        return f"Error: {e}"

    return "Unavailable"
      
@app.route("/kippford/weather/temperature")
def temperature():
    return jsonify({"temperature": get_temperature})
