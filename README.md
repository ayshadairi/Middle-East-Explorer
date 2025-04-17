# Middle East Explorer 🌍

A simple Flask web app where you can explore countries in the Middle East. You can add, view, and delete countries with pictures and descriptions.

---

## 🚀 How to Get It Running

### 1. First, grab the project

Download the code to your computer with this command:

```bash
git clone https://github.com/ayshadairi/Middle-East-Explorer.git
```

### 2. Install the stuff the app needs
Go into the project folder, then run this to install everything the app uses:
```bash
pip install -r requirements.txt
```

### 3. (Optional) Set up a virtual environment
This keeps things clean and avoids messing up other Python projects.

Create one like this:
```bash
python -m venv venv
```
Then activate it:
* On Windows:
```bash
venv\Scripts\activate
```
* On macOS/Linux:
```bash
source venv/bin/activate
```
And install the requirements again just to be safe:

### 4. Add a secret key so sessions work
The app needs a secret key for handling sessions. You can generate one like this:
```bash
import os
print(os.urandom(24))
```
Take the key it gives you and paste it in your app.py like this:
```bash
app.secret_key = b'your_generated_key_here'
```
### 5. Run the app 🎉
Start the Flask server with this command:
```bash
flask run
```
Then open this link in your browser:
```bash
http://127.0.0.1:5000/
```
### 6. Check it out in your browser
If everything worked, you should see the homepage of the Middle East Explorer app.

### 7. Try adding and removing stuff
Play around with the app! Try doing things like:

* Adding new countries

* Uploading images

* Deleting entries

Just make sure everything looks and works the way you want.

### 8. See what’s inside the project
Here’s what all the files and folders are for:
```bash
Middle-East-Explorer/
│
├── static/uploads/       # Where uploaded images are stored
├── templates/            # The HTML templates for the app
├── app.py                # The main Flask app code
├── requirements.txt      # The list of Python packages
└── initial_data.py       # Some sample countries to start with
```
### 9. If something’s not working...
Here are a few things to try:

* Make sure you installed everything from requirements.txt

* Check that your secret key is set correctly

* Make sure you're using Python 3.7 or higher


