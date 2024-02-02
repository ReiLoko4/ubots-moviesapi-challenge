from sqlmodel import Session, SQLModel, create_engine
from MovieApi.constants import database_url


connect_args = {'check_same_thread': False}
engine = create_engine(database_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
        