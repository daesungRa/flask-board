from flask import request, jsonify
from src import app
from src.service import autocomplete_service

auto_service = autocomplete_service.Autocomplete_service()

@app.route("/autocomplete", methods=['POST'])
def autocomplete():
    query = request.form['query']
    # result = autocomplete_result(query) # return tuple type data
    # result = auto_service.find({'name': {'$regex': query}})
    result = auto_service.find({'Name': {'$regex': query, '$options': 'i'}})
    print(result)

    return jsonify({'suggestions': result})

@app.route('/search', methods=['POST'])
def search():
    word = request.values.get('word')
    result = auto_service.find_one({'Name': {'$regex': word, '$options': 'i'}})
    print(result)

    return jsonify({'result': result})