from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select
from datetime import date, datetime


class TeaInfo(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    datetime: Optional[date] = Field(default_factory=datetime.utcnow)
    process: str


sqlite_file_name = "teapot.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_info(process):
    tea_info = TeaInfo(process=process)
    with Session(engine) as session:
        session.add(tea_info)
        session.commit()


def select_teainfo():
    with Session(engine) as session:
        statement = select(TeaInfo)
        results = session.exec(statement)
        for hero in results:
            print(hero)

def main():
    create_db_and_tables()
    create_info('hi')
    select_teainfo()


if __name__ == "__main__":
    main()
