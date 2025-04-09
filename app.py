from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    countries = []
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            countries.append({
                'name': row[0],
                'description': row[2],
                'image': 'uploads/' + row[1].lower().replace(' ', '_') + '.jpg'
            })
    return render_template('home.html', countries=countries)

@app.route('/country/<country_name>')
def country_detail(country_name):
    country = None
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].lower().replace(' ', '_') == country_name.lower():
                country = {
                    'name': row[0],
                    'description': row[2],
                    'image': 'uploads/' + row[1].lower().replace(' ', '_') + '.jpg'
                }
                break
    return render_template('country_detail.html', country=country)

if __name__ == '__main__':
    app.run()
