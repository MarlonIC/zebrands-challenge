from flask import Blueprint, jsonify

blueprint_health = Blueprint('health', __name__)


@blueprint_health.route('', methods=['GET'])
def health():
    return jsonify(
        health=True
    )
