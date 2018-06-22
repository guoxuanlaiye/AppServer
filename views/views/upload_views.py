import tornado.web
from tornado.escape import json_decode
import json
import os

from conf.base import (
    ERROR_CODE,
    SERVER_HEADER
)
from common.commons import (
    http_response,
    save_files
)

class UploadFileHandle(tornado.web.RequestHandler):

    def post(self):
        try:
            image_metas = self.request.files['image']
        except:
            http_response(self, ERROR_CODE['1001'], 1001)
            return

        # image_url = ""
        image_path_list = []
        if image_metas:
            # 获取当前的路径
            pwd = os.getcwd()
            save_image_path = os.path.join(pwd, "static/image/")
            file_name_list = save_files(image_metas, save_image_path)
            image_path_list = [SERVER_HEADER + "/static/image/" + i for i in file_name_list]
            ret_data = {"imageUrl": image_path_list}
            self.write(json.dumps({"data": {"msg": ret_data, "code": 0}}))
        else:
            http_response(self, ERROR_CODE['2001'], 2001)