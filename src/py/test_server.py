from flask import  Flask, jsonify
import numpy as np

app = Flask(__name__)

rng = np.random.default_rng()

@app.route("/", methods=['GET'])
def data():
    '''
    simula el funcionamiento del esp8266
    '''
    return jsonify(
        {"data":rng.integers(0,100,(11)).tolist()}
    )

if __name__ =="__main__":
    app.run(debug=True, port=5000)