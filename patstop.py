from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_base():
    return 'All your base are belong to us'

@app.route('/stops/<stop_id>', methods=['GET'])
def get_stop_info(stop_id):
    return 'This is the info for stop %s' % stop_id



if __name__ == "__main__":
    app.run()
