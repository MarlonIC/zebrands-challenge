import json
from flask import abort, jsonify


def authentication_failure():
    return jsonify(
        code=131,
        message='Authentication failure.',
        data=[]
    ), 401


def not_authorized():
    return jsonify(
        code=141,
        message='Not authorized.',
        data=[]
    ), 403


def resource_not_found():
    return jsonify(
        code=151,
        message='Resource not found.',
        data=[]
    ), 404


def user_not_found():
    return jsonify(
        code=152,
        message='User not found.',
        data=[]
    ), 404


def invalid_access_token():
    return jsonify(
        code=142,
        message='Invalid access token.',
        data=[]
    ), 403


def object_created(data=None):
    if data is None:
        data = []

    return jsonify(
        code=101,
        message='Object created.',
        data=data
    ), 201


def object_updated(data=None):
    if data is None:
        data = []

    return jsonify(
        code=102,
        message='Object updated.',
        data=data
    )


def object_deleted():
    return jsonify(
        code=103,
        message='Object deleted.',
        data=[]
    ), 204


def successful_request(data):
    return jsonify(
        code=100,
        message='Successful request.',
        data=data
    )


def resource_already_exits():
    return jsonify(
        code=161,
        message='The resource already exists.',
        data=[]
    ), 409


def abort_internal_server_error(exception):
    print(exception)
    error = json.dumps({'code': 166, 'message': str(exception)})
    abort(500, description=error)


# TODO: Standard not implemented
def invalid_request(field):
    return jsonify(
        code=111,
        message='Request with invalid data. Field {}'.format(field),
        data=[]
    ), 400
