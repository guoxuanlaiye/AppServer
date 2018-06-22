from conf.base import BaseDB, engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class Users(BaseDB):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    password = Column(String(50), nullable=True)
    createtime = Column(DateTime, nullable=True)

    def __init__(self, name, phone, password, createtime):
        self.name = name
        self.phone = phone
        self.password = password
        self.createtime = createtime

def initdb():
    BaseDB.metadata.create_all(engine)

# 当前文件作为主函数文件入口是调用测试
if __name__ == '__main__':
    pass
    # print("Initialize database.....")
    # initdb()
