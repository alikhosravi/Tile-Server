import os.path
from pathlib import Path
from flask import Flask, send_file
from flask_cors import CORS, cross_origin

from waitress import serve


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)


@app.route('/tiles/<style>/<zoom>/<y>/<x>', methods=['GET', 'POST'])
@cross_origin()
def tiles(style, zoom, y, x):
    #print('x: ',x, 'y: ',y, 'zoom:',zoom)
    default = 'tiles\\default.png' # this is a blank tile, change to whatever you want
    filename = 'tiles\\{}\\{}\\{}\\{}.png'.format(style, zoom, x, y)
    
    #print(filename)
    if Path.exists(Path(filename)):
        print('exist')
        return send_file(filename)
    else:
        return send_file(default)

@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')

'''
if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8080)
'''

serve(app, host='0.0.0.0', port=8080, threads=1)