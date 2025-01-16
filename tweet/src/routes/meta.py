from routes.blueprint import bp
from src.conf import APP_NAME, VERSION, BUILD_NUMBER

@bp.route('/meta', methods=['GET'])
def meta():
    return jsonify({"name": APP_NAME,"buid": BUILD_NUMBER,"version": VERSION})