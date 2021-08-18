from flask import current_app as app
from flask.json import jsonify

@app.route('/divvy')
def divvy():
    return jsonify({ 'message': 'It works' })