from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:@localhost:3306/test?charset=utf8', encoding='utf8', echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
    "0": "ok",
    "1001": "参数非法",
    "1002": "用户已存在，请直接登录",
    "1003": "用户未注册，请先注册"
}