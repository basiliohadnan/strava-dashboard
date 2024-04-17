from flask import Flask, render_template
import requests
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_athlete_data')
def get_athlete_data():
    # URL to fetch athlete data from Strava API
    url = 'https://www.strava.com/api/v3/athlete'
    
    # Header with bearer token
    headers = {'Authorization': f'Bearer {config.BEARER_TOKEN}'}
    
    # Send GET request to fetch athlete data
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        athlete_data = response.json()
        return f'Athlete data: {athlete_data}'
    else:
        return f'Error: {response.text}'

if __name__ == '__main__':
    app.run(debug=True)
