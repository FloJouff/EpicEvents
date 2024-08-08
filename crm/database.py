from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_url = f"mysql+mysqlconnector://{os.getenv("DB_USER")}:{
    os.getenv("DB_PASSWORD")}@{
        os.getenv("DB_HOST")}:{
            os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()


def init_db():
    from crm.models.client import Client
    from crm.models.contract import Contract
    from crm.models.event import Event
    from crm.models.user import User
    from crm.models.role import Role

    Base.metadata.create_all(engine)


print("success")
