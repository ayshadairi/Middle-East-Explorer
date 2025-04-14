from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/countries')
def countries():
    countries = []
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)  # Use DictReader to get field names
        for row in reader:
            countries.append({
                'name': row['Name'],
                'image': 'uploads/' + row['Image'].lower().replace(' ', '_') + '.jpg',
                'capital': row['Capital'],
                'population': row['Population'],
                'region': row['Region'],
                'description': row['Description']
            })
    return render_template('countries.html', countries=countries)

if __name__ == '__main__':
    app.run()


