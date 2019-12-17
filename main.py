from flask import Flask, request, jsonify
from pub import Publisher
from datetime import datetime

app = Flask(__name__)

publisher = Publisher()


@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json(force=True)

    # Add time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    data['timestamp'] = timestamp

    # Add location
    data['location'] = "bedroom"

    publisher.publish_data(data)
    print(data)
    return jsonify(data)


@app.route('/status', methods=['GET'])
def status():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
