"""App to serve models based on user input"""

from flask import Flask, request, jsonify
from .predictions import get_prediction
from .functions import disease_filter

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'This Works'

    @app.route('/prediction', methods=['GET', 'POST'])
    def api_return():
        data = request.args or request.form or request.json
        prediction = get_prediction(data)
        disease = disease_filter(data.get('disease'))
        json = jsonify(strains=prediction, info=disease)
        return json

    @app.route('/altpredict', methods=['GET', 'POST'])
    def json_return():
        json_form = request.form
        json_args = request.args
        pure_json = request.json
        # This returns a dict from the front-end
        print(json_form)
        print(json_args)
        print(pure_json)

        sample =  {'disease':'Glaucoma',
        'effect1':'Creative',
        'effect2':'Energetic',
        'effect3':'Tingly',
        'effect4':'Euphoric',
        'effect5':'Relaxed',
        'flavor1':'Earthy',
        'flavor2':'Sweet',
        'flavor3':'Citrus'}
        # Transforms the json received from users
        prediction = get_prediction(json_form)
        disease = disease_filter(request.form.get('disease'))
        # Stores predict_dict in the session, so it can be gotten from /data
        # session['price'] = predict_dict
        altjson = jsonify(strains=prediction, info=disease)
        return altjson

    """
    #test POST method with json data
    test_case = {'disease':'Glaucoma',
                'effect1':'Creative',
                'effect2':'Energetic',
                'effect3':'Tingly',
                'effect4':'Euphoric',
                'effect5':'Relaxed',
                'flavor1':'Earthy',
                'flavor2':'Sweet',
                'flavor3':'Citrus'
                }
    test_result = {'info': 'Daily Dosage: 5mg THC. Take 1 capsule.',
                  'strains': ['Blueberry-Trainwreck', 
                              'Boggle-Gum',
                              'Kid-N-Cookies',
                              'Cronuts',
                              'Huckleberry-Hound']
                              }
    with app.test_client() as c:
        rv = c.post('/prediction', json=test_case)
        json_data = rv.get_json()
        assert json_data == test_result
    """
    
    return app
