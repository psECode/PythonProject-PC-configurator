import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import os

SqlAlchemyBase = dec.declarative_base()

__factory = None

global controlling_array
controlling_array = [0, 0, 0, 0, 0, 0, 0]  # plates, memory, power, shells, proccesors, coolers, graphic_cards

def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")
    if not os.path.exists(db_file):
        print("База данных не обнаружена")
        open(db_file, 'w').close()
    if not os.path.exists("static/programm_constants.txt"):
        open("static/programm_constants.txt", 'w').close()
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")


    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()