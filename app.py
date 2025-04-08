from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Function to read data from data.csv
def get_country_data():
    countries = []
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            countries.append({
                'name': row['name'],
                'image': row['image'],
                'description': row['description']
            })
    return countries

# Homepage Route
@app.route('/')
def home():
    return render_template('home.html')

# Countries Page Route (to display country data)
@app.route('/countries')
def countries():
    countries_data = get_country_data()  # Read from data.csv
    return render_template('countries.html', countries=countries_data)

if __name__ == '__main__':
    app.run(debug=True)
