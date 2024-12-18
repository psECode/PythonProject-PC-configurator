from backend import db_session
from backend.parsers import get_plates, get_graphic_cards, get_memory, get_power, get_proccesors, get_coolers, \
    get_shells
from backend.models import Plate, GraphicCard, Memory, Power, Proccesor, Cooler, Shell
from backend.db_session import controlling_array, global_init


def get_plates_to_db():
    db_sess = db_session.create_session()
    try:
        plates_data = get_plates()
    except:
        print('Error while parsing plates')
        db_sess.close()
        pass
    for plate in plates_data:
        if db_sess.query(Plate).filter(Plate.uid == plate.uid).first() is None:
            db_sess.add(plate)
        else:
            db_sess
            db_sess.query(Plate).filter(Plate.uid == plate.uid).update({'name': plate.name, 'img': plate.img, 'price': plate.price,
                                                                       'form_factor': plate.form_factor, 'chipset': plate.chipset,
                                                                       'socket': plate.socket, 'slots': plate.slots,
                                                                       'mgc': plate.mgc})
    db_sess.commit()
    db_sess.close()



def get_graphic_cards_to_db():
    db_sess = db_session.create_session()
    try:
        graphic_cards_data = get_graphic_cards()
    except:
        print('Error while parsing graphic cards')
        db_sess.close()
        pass
    for card in graphic_cards_data:
        if db_sess.query(GraphicCard).filter(GraphicCard.uid == card.uid).first() is None:
            db_sess.add(card)
        else:
            db_sess.query(GraphicCard).filter(GraphicCard.uid == card.uid).update({'name': card.name, 'img': card.img, 'price': card.price,
                                                                       'memory_type': card.memory_type, 'memory': card.memory,
                                                                       'nVidia': card.nVidia, 'power': card.power,
                                                                       'plugs': card.plugs})
    db_sess.commit()
    db_sess.close()


def get_memory_to_db():
    db_sess = db_session.create_session()
    try:
        memory_data = get_memory()
    except:
        print('Error while parsing memory')
        db_sess.close()
        pass
    for mem in memory_data:
        if db_sess.query(Memory).filter(Memory.uid == mem.uid).first() is None:
            db_sess.add(mem)
        else:
            db_sess.query(Memory).filter(Memory.uid == mem.uid).update({'name': mem.name, 'img': mem.img, 'price': mem.price,
                                                                       'ddr': mem.ddr, 'mgc': mem.mgc})
    db_sess.commit()
    db_sess.close()


def get_power_to_db():
    db_sess = db_session.create_session()
    try:
        power_data = get_power()
    except:
        print('Error while parsing power')
        db_sess.close()
        pass
    for power in power_data:
        if db_sess.query(Power).filter(Power.uid == power.uid).first() is None:
            db_sess.add(power)
        else:
            db_sess.query(Power).filter(Power.uid == power.uid).update({'name': power.name, 'img': power.img, 'price': power.price,
                                                                       'form_factor': power.form_factor, 'power': power.power,
                                                                       'pins': power.pins})
    db_sess.commit()
    db_sess.close()


def get_proccesors_to_db():
    db_sess = db_session.create_session()
    try:
        proccesors_data = get_proccesors()
    except:
        print('Error while parsing proccesors')
        db_sess.close()
        pass
    for proccesor in proccesors_data:
        if db_sess.query(Proccesor).filter(Proccesor.uid == proccesor.uid).first() is None:
            db_sess.add(proccesor)
        else:
            db_sess.query(Proccesor).filter(Proccesor.uid == proccesor.uid).update({'name': proccesor.name, 'img': proccesor.img, 'price': proccesor.price,
                                                                       'power': proccesor.power, 'mgc': proccesor.mgc,
                                                                       'socket': proccesor.socket, 'core_count': proccesor.core_count,
                                                                       'intel': proccesor.intel})
    db_sess.commit()
    db_sess.close()


def get_coolers_to_db():
    db_sess = db_session.create_session()
    try:
        coolers_data = get_coolers()
    except:
        print('Error while parsing coolers')
        db_sess.close()
        pass
    for cooler in coolers_data:
        if db_sess.query(Cooler).filter(Cooler.uid == cooler.uid).first() is None:
            db_sess.add(cooler)
        else:
            db_sess.query(Cooler).filter(Cooler.uid == cooler.uid).update({'name': cooler.name, 'img': cooler.img, 'price': cooler.price,
                                                                       'power': cooler.power, 'sockets': cooler.sockets,
                                                                       'vent_count': cooler.vent_count})
    db_sess.commit()
    db_sess.close()


def get_shells_to_db():
    db_sess = db_session.create_session()
    try:
        shells_data = get_shells()
    except:
        print('Error while parsing shells')
        db_sess.close()
        pass
    for shell in shells_data:
        if db_sess.query(Shell).filter(Shell.uid == shell.uid).first() is None:
            db_sess.add(shell)
        else:
            db_sess.query(Shell).filter(Shell.uid == shell.uid).update({'name': shell.name, 'img': shell.img, 'price': shell.price,
                                                                       'form_factor': shell.form_factor})
    db_sess.commit()
    db_sess.close()


def get_plate_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Plate).filter(Plate.uid == uid).first()
    db_sess.close()
    return result


def get_memory_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Memory).filter(Memory.uid == uid).first()
    db_sess.close()
    return result

def get_graphic_card_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(GraphicCard).filter(GraphicCard.uid == uid).first()
    db_sess.close()
    return result

def get_power_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Power).filter(Power.uid == uid).first()
    db_sess.close()
    return result


def get_proccesor_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Proccesor).filter(Proccesor.uid == uid).first()
    db_sess.close()
    return result

def get_cooler_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Cooler).filter(Cooler.uid == uid).first()
    db_sess.close()
    return result

def get_shell_from_db(uid):
    db_sess = db_session.create_session()
    result = db_sess.query(Shell).filter(Shell.uid == uid).first()
    db_sess.close()
    return result

def choose_coolers():
    db_sess = db_session.create_session()
    if controlling_array[4] != 0:
        proc = db_sess.query(Proccesor).filter(Proccesor.uid == controlling_array[4]).first()
        coolers = db_sess.query(Cooler).filter(Cooler.sockets.contains(proc.socket)).all()
        db_sess.close()
        return coolers
    if controlling_array[0] != 0:
        plate = db_sess.query(Plate).filter(Plate.uid == controlling_array[0]).first()
        coolers = db_sess.query(Cooler).filter(Cooler.sockets.contains(plate.socket)).all()
        db_sess.close()
        return coolers
    coolers = db_sess.query(Cooler).all()
    db_sess.close()
    return coolers

def choose_memory():
    db_sess = db_session.create_session()
    mems = db_sess.query(Memory).all()
    if controlling_array[0] != 0:
        plate = db_sess.query(Plate).filter(Plate.uid == controlling_array[0]).first()
        mems = [x for x in mems if (int(plate.mgc.split()[1].strip()) >= x.mgc >= int(plate.mgc.split()[0].strip()))]
    db_sess.close()
    return mems

def choose_graphic_cards():
    db_sess = db_session.create_session()
    cards = db_sess.query(GraphicCard).all()
    db_sess.close()
    return cards

def choose_power():
    db_sess = db_session.create_session()
    powers = db_sess.query(Power).all()
    summ = 0
    if controlling_array[0] != 0:
        plate = db_sess.query(Plate).filter(Plate.uid == controlling_array[0]).first()
        powers = [x for x in powers if plate.form_factor in x.form_factor]
    if controlling_array[4] != 0:
        proc = db_sess.query(Proccesor).filter(Proccesor.uid == controlling_array[4]).first()
        summ += proc.power
    if controlling_array[5] != 0:
        cooler = db_sess.query(Cooler).filter(Cooler.uid == controlling_array[5]).first()
        summ += cooler.power
    if controlling_array[6] != 0:
        graphic_card = db_sess.query(GraphicCard).filter(GraphicCard.uid == controlling_array[6]).first()
        summ += graphic_card.power
    powers = [x for x in powers if summ + 50 <= x.power]
    db_sess.close()
    return powers

def choose_shells():
    db_sess = db_session.create_session()
    if controlling_array[0] != 0:
        plate = db_sess.query(Plate).filter(Plate.uid == controlling_array[0]).first()
        shells = db_sess.query(Shell).filter(Shell.form_factor.contains(plate.form_factor)).all()
        db_sess.close()
        return shells
    if controlling_array[2] != 0:
        shells = []
        power = db_sess.query(Power).filter(Power.uid == controlling_array[2]).first()
        shells.extend(db_sess.query(Shell).filter(Shell.form_factor.contains(power.form_factor)).all())
        db_sess.close()
        return shells
    shells = db_sess.query(Shell).all()
    db_sess.close()
    return shells


def choose_proccesors():
    db_sess = db_session.create_session()
    if controlling_array[0] != 0:
        plate = db_sess.query(Plate).filter(Plate.uid == controlling_array[0]).first()
        procs = db_sess.query(Proccesor).filter(Proccesor.socket == plate.socket and int(plate.mgc.split()[1].strip()) >= Proccesor.mgc >= int(plate.mgc.split()[0].strip())).all()
        db_sess.close()
        return procs
    if controlling_array[2] != 0:
        power = db_sess.query(Power).filter(Power.uid == controlling_array[2]).first()
        procs = db_sess.query(Proccesor).filter(power.socket.contains(Proccesor.socket)).all()
        db_sess.close()
        return procs
    procs = db_sess.query(Proccesor).all()
    db_sess.close()
    return procs

def choose_plates():
    db_sess = db_session.create_session()
    plates = db_sess.query(Plate).all()
    if controlling_array[1] != 0: # memory
        mem = db_sess.query(Memory).filter(Memory.uid == controlling_array[1]).first()
        plates =  [x for x in plates if (mem.ddr == x.slots and (int(x.mgc.split()[1].strip()) >= mem.mgc >= int(x.mgc.split()[0].strip())))]
    if controlling_array[2] != 0: # power
        power = db_sess.query(Power).filter(Power.uid == controlling_array[2]).first()
        plates = [x for x in plates if power.form_factor == x.form_factor]
    if controlling_array[3] != 0: # shell
        shell = db_sess.query(Shell).filter(Shell.uid == controlling_array[3]).first()
        plates = [x for x in plates if x.form_factor in shell.form_factor]
    if controlling_array[4] != 0 and controlling_array[5] != 0: # proccesor
        proc = db_sess.query(Proccesor).filter(Proccesor.uid == controlling_array[4]).first()
        plates = [x for x in plates if (proc.socket == x.socket and int(x.mgc.split()[1].strip()) >= proc.mgc >= int(x.mgc.split()[0].strip()))]
    if controlling_array[5] != 0 and controlling_array[4] == 0: # cooler and not procc
        cooler = db_sess.query(Cooler).filter(Cooler.uid == controlling_array[5]).first()
        plates = [x for x in plates if x.socket in cooler.sockets]
    db_sess.close()
    return plates