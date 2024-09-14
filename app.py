from flask import Flask
import requests
import time
import json

app = Flask(__name__)

# Rename to this application link
selfsite = 'https://keepalive-2hrf.onrender.com'

with open('./sites.json', 'r') as file:
	sites = dict(json.load(file))['sites']

@app.route('/')
def index():
	result = {}
	for site in sites:
		result[site[8:]] = requests.get(site).status_code
	return result

@app.route('/turnon')
def turn_on():
	time.sleep(5 * 60)
	requests.get(selfsite)
	requests.get(selfsite+'/turnon')

if __name__ == '__main__':
	app.run()
