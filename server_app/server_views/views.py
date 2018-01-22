"""
CREAt: 2018/1/19
AUTHOR: Hehahutu
"""

from flask.views import MethodView
from flask import render_template, make_response, session, request
from server_app.helper.file_parser import get_file_list
import urllib.parse
from setting import BLANK_SIZE
from flask import send_file


class FileView(MethodView):
    def get(self, file_path=''):
        path = file_path
        data = get_file_list(path)
        # print(data, )
        last_path = session.get('last_path', request.path)
        spli = request.path.split('/')[:-2]
        last_url = '/'.join(spli) or '/'
        session['last_path'] = request.path
        if data:
            if data[0] == 'folder':
                return render_template('files.html', files=data[1], folders=data[2], last_path=last_path,
                                       last_url=last_url, path=request.path)
            elif data[0] == 'file':
                # filename = data[1]
                path = data[2]
                b_data = send_file(path)
                # resp = make_response(b_data, 200)
                # name = urllib.parse.quote(filename)
                #
                # resp.headers["Content-Disposition"] = f"attachment; filename*=utf-8''{name}"
                # resp.headers["Content-Type"] = f"application/octet-stream; charset=utf-8"
                # resp.headers["Connection"] = 'Keep-Alive'

                return b_data
        else:
            return 'URL错误,请检查路径是否正确!!!', 400


def poll_data(path):
    with open(path, 'rb') as f:
        while True:
            data = f.read(BLANK_SIZE)
            if data:
                yield data
            else:
                return None
