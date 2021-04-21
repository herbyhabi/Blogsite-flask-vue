from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Integer, Text, DateTime
from sqlalchemy import Column, String
from datetime import datetime
import init

# Base = init.setup_db()
# app, db = init.create_app()


engine = create_engine('mysql+pymysql://root:testtest@127.0.0.1:3306/Blog_db?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)


# 创建表
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    status = Column(String(255), nullable=True)

    def __init__(self, title, content, status):
        self.title = title
        self.content = content
        self.status = status





