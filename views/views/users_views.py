import tornado.web
from tornado.escape import json_decode
from common.commons import http_response
from conf.base import ERROR_CODE
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from models import Users


##########  configure logging ##########
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath,
                                   when="D",
                                   interval=1,
                                   backupCount=30)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
########################################

class BaseHandle(tornado.web.RequestHandler):
    
    @property
    def db(self):
        session = self.application.dbSession()
        return session


class RegistHandle(BaseHandle):

    def post(self):
        try:
            args = json_decode(self.request.body)
            name = args['name']
            phone = args['phone']
            password = args['psw']
            print(args)
        except:
            logger.info("RegistHandle: request arg incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return

        ex_user = self.db.query(Users).filter(Users.phone==phone).first()
        if ex_user:
            http_response(self, ERROR_CODE['1002'], 1002)
            self.db.close()
            return
        else:
            create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_user = Users(name=name, phone=phone, password=password, createtime=create_time)
            self.db.add(add_user)
            self.db.commit()
            self.db.close()
            http_response(self, ERROR_CODE['0'], 0)


class LoginHandle(BaseHandle):


    def get(self):
        self.render("user/login.html")
    
    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            psw = args['psw']
            print("args = %s" % args)
        except:
            http_response(self, ERROR_CODE['1001'], 1001)
            return
        
        if phone:
            ex_user = self.db.query(Users).filter(Users.phone==phone).first()
            print("ex_user = %s, type = %s"%(ex_user, type(ex_user)))
            if ex_user:
                if ex_user.password == psw:
                    # 密码正确，登录成功
                    http_response(self, ERROR_CODE['0'], 0)
                else:
                    # 密码错误
                    http_response(self, ERROR_CODE['1004'], 1004)
            else:
                # 用户未注册
                http_response(self, ERROR_CODE['1003'], 1003)
        else:
            # 参数非法
            http_response(self, ERROR_CODE['1001'], 1001)


