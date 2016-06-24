from flask import Flask
from pghbustime import *

my_key = "your_api_key"
api = BustimeAPI(my_key) #default is to return JSON

app = Flask(__name__)

@app.route('/')
def home_base():
    return 'All your base are belong to us'

@app.route('/stops/<stop_id>', methods=['GET'])
def get_stop_info(stop_id):
    return 'This is the info for stop %s' % stop_id



if __name__ == "__main__":
    app.run()


