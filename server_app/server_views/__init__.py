"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""
from flask.blueprints import Blueprint

fibp = Blueprint('fibp', __name__)

from server_app.server_views.views import *

fi_view = FileView.as_view('file_view')

fibp.add_url_rule('/<path:file_path>', view_func=fi_view)
# fibp.add_url_rule('/<path:file_path>/', view_func=fi_view)
fibp.add_url_rule('/', view_func=fi_view)
