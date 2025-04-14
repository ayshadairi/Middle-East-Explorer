from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


initial_countries = [
    {
        "Name": "Syria",
        "Image": "syria.jpg",
        "Capital": "Damascus",
        "Population": "17500657",
        "Region": "Middle East",
        "Description": "Syria is a Middle Eastern country with a rich history, including ancient civilizations and landmarks like Damascus and Palmyra. Despite its cultural heritage, Syria has faced significant challenges in recent years due to conflict and humanitarian crises. Its resilient people and traditions remain deeply inspiring."
    },
    {
        "Name": "Lebanon",
        "Image": "lebanon.jpg",
        "Capital": "Beirut",
        "Population": "6825445",
        "Region": "Middle East",
        "Description":"Lebanon is a small Middle Eastern country on the Mediterranean coast, known for its rich history, vibrant culture, and ancient cities like Byblos and Baalbek. Despite facing challenges such as political instability and economic crises, Lebanon remains renowned for its resilience, natural beauty, and culinary heritage. Its diverse society and deep-rooted traditions make it a unique cultural hub in the region."
    },
    {
        "Name": "Jordan",
        "Image": "jordan.jpg",
        "Capital": "Amman",
        "Population": "10203134",
        "Region": "Middle East",
        "Description": "Jordan is a Middle Eastern country known for its historical treasures, including the ancient city of Petra and the Roman ruins of Jerash. Renowned for its stability in a turbulent region, Jordan boasts diverse landscapes, from the Dead Sea to the Wadi Rum desert. Its culture reflects a rich blend of tradition and modernity."
    },
    {
        "Name": "Iraq",
        "Image": "iraq.jpg",
        "Capital": "Baghdad",
        "Population": "40222503",
        "Region": "Middle East",
        "Description": "Iraq, Located in the heart of the Middle East, is known as the cradle of civilization, with ancient Mesopotamian cities like Babylon and Ur. Despite its rich cultural heritage and vast oil reserves, Iraq has endured challenges such as conflict and political instability in recent decades. Its people, history, and landscapes remain deeply significant to the region's identity."
    },
    {
        "Name": "Egypt",
        "Image": "egypt.jpg",
        "Capital": "Cairo",
        "Population": "104124000",
        "Region": "North Africa",
        "Description": "Egypt, located in North Africa, is famous for its ancient civilization, including the iconic pyramids of Giza, the Sphinx, and the Nile River. As a cultural crossroads of Africa, the Middle East, and the Mediterranean, Egypt boasts a rich heritage and vibrant traditions. Despite modern challenges, its historical significance and diverse society continue to captivate the world."
    },
    {
        "Name": "Saudi Arabia",
        "Image": "saudi-arabia.jpg",
        "Capital": "Riyadh",
        "Population": "34813871",
        "Region": "Middle East",
        "Description": "Saudi Arabia, located in the Arabian Peninsula, is known as the birthplace of Islam and home to its two holiest cities, Mecca and Medina. Renowned for its vast deserts, oil wealth, and cultural heritage, the kingdom plays a significant role in the global economy and Islamic traditions. Recent years have seen efforts toward modernization and economic diversification while preserving its deep-rooted traditions."
    },
    {
        "Name": "Palestine",
        "Image": "palestine.jpg",
        "Capital": "Ramallah",
        "Population": "5000000",
        "Region": "Middle East",
        "Description": "Palestine, located in the Middle East, is a region with deep historical and cultural significance, home to ancient cities like Jerusalem and Bethlehem. Despite enduring decades of conflict and hardship, its people maintain a strong sense of identity and resilience. Palestine's rich heritage and traditions continue to inspire and connect communities worldwide."
    },
    {
        "Name": "UAE",
        "Image": "uae.jpg",
        "Capital": "Abu Dhabi",
        "Population": "9770529",
        "Region": "Middle East",
        "Description": "The United Arab Emirates (UAE), located in the Arabian Peninsula, is a federation of seven emirates, including Dubai and Abu Dhabi. Known for its rapid development, futuristic architecture, and thriving economy fueled by oil and tourism, the UAE blends modern innovation with cultural traditions. It is a global hub for business, luxury, and multicultural experiences."
    },
    {
        "Name": "Kuwait",
        "Image": "kuwait.jpg",
        "Capital": "Kuwait City",
        "Population": "4137300",
        "Region": "Middle East",
        "Description": "Located in the Arabian Peninsula, Kuwait is a small yet wealthy nation known for its vast oil reserves and modern urban development. Despite its size, it plays a prominent role in the region's economy and culture."
    },
    {
        "Name": "Oman",
        "Image": "oman.jpg",
        "Capital": "Muscat",
        "Population": "5106622",
        "Region": "Middle East",
        "Description": "Situated on the southeastern tip of the Arabian Peninsula, Oman is renowned for its stunning natural beauty, including deserts, mountains, and coastlines. Known for its rich history and peaceful diplomacy, Oman preserves strong cultural traditions while embracing modernity."
    },
    {
        "Name": "Yemen",
        "Image": "yemen.jpg",
        "Capital": "Sana'a",
        "Population": "29825968",
        "Region": "Middle East",
        "Description": "Yemen, at the southern edge of the Arabian Peninsula, is home to ancient history, diverse landscapes, and unique architecture, such as the city of Sana'a. However, it faces ongoing conflict and humanitarian challenges that impact its people and heritage."
    },
    {
        "Name": "Qatar",
        "Image": "qatar.jpg",
        "Capital": "Doha",
        "Population": "2881053",
        "Region": "Middle East",
        "Description": "A small Gulf nation, Qatar is known for its immense wealth derived from natural gas and oil, as well as its rapid modernization. It has gained global attention for hosting events like the FIFA World Cup, blending innovation with cultural traditions."
    },
    {
        "Name": "Bahrain",
        "Image": "bahrain.jpg",
        "Capital": "Manama",
        "Population": "1641160",
        "Region": "Middle East",
        "Description": "Bahrain is an island nation in the Persian Gulf, famous for its rich history, pearl diving heritage, and modern financial sector. Despite its small size, Bahrain is a cultural and economic hub in the region."
    }
]



@app.before_request
def initialize_session():
    if "countries" not in session:
        session["countries"] = initial_countries.copy()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/countries")
def show_countries():
    return render_template("countries.html", countries=session["countries"])

@app.route("/add", methods=["GET", "POST"])
def add_country():
    if request.method == "POST":
        name = request.form["name"]
        capital = request.form["capital"]
        population = request.form["population"]
        region = request.form["region"]
        description = request.form["description"]

        image_file = request.files["image"]
        image_filename = None
        if image_file and image_file.filename != "":
            image_filename = image_file.filename
            image_path = os.path.join('static/uploads', image_filename)
            image_file.save(image_path)

        if name and image_filename and capital and population and region and description:
            session["countries"].append({
                "Name": name,
                "Image": image_filename,
                "Capital": capital,
                "Population": population,
                "Region": region,
                "Description": description
            })
            session.modified = True
            return redirect(url_for("show_countries"))

    return render_template("add_country.html")


@app.route("/delete/<name>", methods=["POST"])
def delete_country(name):
    session["countries"] = [c for c in session["countries"] if c["Name"] != name]
    session.modified = True
    return redirect(url_for("show_countries"))

if __name__ == "__main__":
    app.run()
