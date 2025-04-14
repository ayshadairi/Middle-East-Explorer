from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add_country.html')
@app.route('/add', methods=['POST'])
def add_country():
    name = request.form['name']
    capital = request.form['capital']
    population = request.form['population']
    region = request.form['region']
    description = request.form['description']

    image = request.files['image']
    image_filename = secure_filename(image.filename)

    if not image_filename.lower().endswith(tuple(ALLOWED_EXTENSIONS)):
        return "Invalid image format."

    image_path = os.path.join(UPLOAD_FOLDER, image_filename)
    image.save(image_path)

    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, image_filename, capital, population, region, description])

    return redirect(url_for('countries'))

@app.route('/countries')
def countries():
    countries = []
    with open('data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) < 6:
                continue
            countries.append({
                'name': row[0],
                'image': url_for('static', filename='uploads/' + row[1]),
                'capital': row[2],
                'population': row[3],
                'region': row[4],
                'description': row[5],
            })
    return render_template('countries.html', countries=countries)
@app.route('/remove/<country_name>', methods=['POST'])
def remove_country(country_name):
    new_rows = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            if row[0].lower().replace(' ', '_') != country_name.lower():
                new_rows.append(row)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(new_rows)

    return redirect(url_for('countries'))

if __name__ == '__main__':
    app.run()







