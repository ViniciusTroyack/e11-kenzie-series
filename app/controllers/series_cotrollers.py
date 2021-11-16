
from flask import request, jsonify
from app.models.series_models import Series


def get_all():

    return 'ok', 200


def create():
    data = request.get_json()

    user = Series(**data)

    return jsonify(user.create_serie()), 201


def series():
    try:
        return jsonify(Series.get_all()), 200
    except:
        return jsonify([]),200


def select_by_id(serie_id):
    try:
        return jsonify(Series.get_by_id(serie_id)), 200
    except:
        return {"error": "Not Found"}, 404
