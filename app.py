from flask import Flask, request
import requests
import time
import json

app = Flask(__name__)

with open('./sites.json', 'r') as file:
    sites = dict(json.load(file))['sites']

@app.route('/')
def index():
    result = {}
    for site in sites:
        result[site[8:]] = requests.get(site).status_code
    print(f'index:\n{result}')
    return result

@app.route('/turnon/')
def turn_on():
    while True:
        time.sleep(5*60)
        index()

if __name__ == '__main__':
    app.run()
