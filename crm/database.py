from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crm.models.base import Base


load_dotenv()

db_url = f"mysql+mysqlconnector://{os.getenv("DB_USER")}:{
    os.getenv("DB_PASSWORD")}@{
        os.getenv("DB_HOST")}:{
            os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)


print("success")
