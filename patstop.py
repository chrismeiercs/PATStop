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

#Get the next bus arriving at your stop
@app.route('/stops/<stop_id>/next', methods=['GET'])
def get_next_bus(stop_id):
    current_stop = Stop.get(api, stop_id)
    next_buses = current_stop.predictions()
    next_bus = next_buses.next()

    return 'The next bus is %s arriving at %s' % (next_bus.route, next_bus.eta)

#Get the next specified bus arriving at your stop
@app.route('/stops/<stop_id>/<route>', methods=['GET'])
def get_next_route(stop_id, route):
    current_stop = Stop.get(api, stop_id)
    
    try:
        next_route = current_stop.predictions(route=route).next()
        return 'The next %s is arriving at %s' % (route, next_route.eta)
    except:
        return "Route Does Not Stop Here"


if __name__ == "__main__":
    app.run(debug=True)


