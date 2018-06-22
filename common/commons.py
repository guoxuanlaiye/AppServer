import json
import os

def http_response(self, msg, code, data=None):
    
    self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
    self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    self.write(json.dumps({"message": msg, "code": code, "data":data}))

def save_files(file_metas, in_rel_path, type='image'):
    
    file_path = ""
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join(in_rel_path, file_name)
        file_name_list.append(file_name)
        # with open(file_path, 'wb') as up:
        #     up.write(meta['body'])
    return file_name_list

if __name__ == '__main__':
    pass
    # http_response()
