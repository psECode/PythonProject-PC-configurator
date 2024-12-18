from backend.db_session import SqlAlchemyBase
import sqlalchemy



class Plate(SqlAlchemyBase):
    __tablename__ = 'plates'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    form_factor = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chipset = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    socket = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    slots = sqlalchemy.Column(sqlalchemy.String, nullable=True) #ddr
    mgc = sqlalchemy.Column(sqlalchemy.String, nullable=True) # two_integers
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

class GraphicCard(SqlAlchemyBase):
    __tablename__ = 'graphic_cards'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    memory_type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    memory = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    power = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    plugs = sqlalchemy.Column(sqlalchemy.String, nullable=True) # список портов
    nVidia = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

class Proccesor(SqlAlchemyBase):
    __tablename__ = 'proccesors'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    power = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    socket = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    core_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    mgc = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    intel = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)

class Cooler(SqlAlchemyBase):
    __tablename__ = 'coolers'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    sockets = sqlalchemy.Column(sqlalchemy.String, nullable=True) # список сокетов
    power = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    vent_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=1)

class Shell(SqlAlchemyBase):
    __tablename__ = 'shells'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    form_factor = sqlalchemy.Column(sqlalchemy.String, nullable=True) # список форм факторов

class Memory(SqlAlchemyBase):
    __tablename__ = 'memory'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    ddr = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    mgc = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

class Power(SqlAlchemyBase):
    __tablename__ = 'power'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    power = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    form_factor = sqlalchemy.Column(sqlalchemy.String, nullable=True) # список форм факторов
    pins = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

class Storage:
    plate: Plate
    shell: Shell
    memory: Memory
    power: Power
    proccesor: Proccesor
    cooler: Cooler
    graphic_card: GraphicCard

    plates: list[Plate]
    shells: list[Shell]
    memories: list[Memory]
    powers: list[Power]
    proccesors: list[Proccesor]
    coolers: list[Cooler]
    graphic_cards: list[GraphicCard]