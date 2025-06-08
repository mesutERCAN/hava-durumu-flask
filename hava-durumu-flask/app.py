from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "API_KEYİNİ_BURAYA_YAZ"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city.title(),
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
