# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:@localhost:3306/test?charset=utf8', encoding='utf8', echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
    "0": "登录成功",
    "1001": "参数非法",
    "1002": "用户已存在，请直接登录",
    "1003": "用户未注册，请先注册",
    "1004": "输入密码有误",
    "2001": "上传图片不能为空"
}
SERVER_HEADER = "http://127.0.0.1:8998"