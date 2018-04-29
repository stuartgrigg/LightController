import json
import os
from flask import Flask, Response, send_from_directory
app = Flask(__name__, static_folder=None)

ON_PI = os.environ['ON_PI'] == 'true'

# Use conditional imports as if we are not on the Pi we do not
# want to import the Pi GPIO library.
if ON_PI:
    from .live_controller import LiveController
    controller = LiveController()
else:
    from .test_controller import TestController
    controller = TestController()


@app.route('/api/setlight/<on>', methods=['POST'])
def set_light(on):
    out_status = controller.set_on(on == 'true')
    return Response(
        json.dumps({'status': out_status}),
        mimetype='application/json'
    )


@app.route('/api/getlight', methods=['GET'])
def get_light():
    out_status = controller.get_on()
    return Response(
        json.dumps({'status': out_status}),
        mimetype='application/json'
    )


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('../client/build', path)
