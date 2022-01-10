import json
from flask import Flask, jsonify
from dotenv import load_dotenv
from pathlib import Path
from .Products.infrastructure.rest.create_product import blueprint_create_product
from .Products.infrastructure.rest.update_product import blueprint_update_product
from .Products.infrastructure.rest.delete_product import blueprint_delete_product
from .Products.infrastructure.rest.get_all_product import blueprint_get_all_product
from .Products.infrastructure.rest.get_by_id_product import blueprint_get_by_id_product
from .Products.infrastructure.rest.health import blueprint_health
from .Auth.infrastructure.rest.login import blueprint_login



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(blueprint_create_product, url_prefix='/v1/products')
app.register_blueprint(blueprint_update_product, url_prefix='/v1/products')
app.register_blueprint(blueprint_delete_product, url_prefix='/v1/products')
app.register_blueprint(blueprint_get_all_product, url_prefix='/v1/products')
app.register_blueprint(blueprint_get_by_id_product, url_prefix='/v1/products')
app.register_blueprint(blueprint_health, url_prefix='/v1/health')
app.register_blueprint(blueprint_login, url_prefix='/v1/auth/login')
env_path = Path('.') / '../.env'
load_dotenv(dotenv_path=env_path, verbose=True)

@app.errorhandler(500)
def unauthorized(error):
    data = json.loads(error.description)
    return jsonify(
        code=data.get('code'),
        message=data.get('message'),
        data=[]
    ), 500
