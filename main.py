import datetime
import threading
from flask import Flask, render_template, redirect, request
from backend import db_session, bd_repository
from backend.bd_repository import get_plates_to_db, get_memory_to_db, get_power_to_db, get_shells_to_db, \
    get_proccesors_to_db, get_coolers_to_db, get_graphic_cards_to_db
from backend.db_session import controlling_array
from backend.models import Storage

buff_storage = Storage
buff_storage.plate = 0
buff_storage.memory = 0
buff_storage.power = 0
buff_storage.shell = 0
buff_storage.proccesor = 0
buff_storage.cooler = 0
buff_storage.graphic_card = 0
buff_storage.plates = []
buff_storage.memories = []
buff_storage.powers = []
buff_storage.shells = []
buff_storage.proccesors = []
buff_storage.coolers = []
buff_storage.graphic_cards = []
app = Flask("Конфигуратор ПК")
@app.get("/")
def root():
    with open("static/programm_constants.txt", "r") as f:
        constants = f.readlines()
        if len(constants) == 1:
            return redirect('/main_page')
        else:
            return render_template('ought.html')

def background_task(f):
    def background_f(*args, **kwargs):
        threading.Thread(target=f, args=args, kwargs=kwargs).start()
    return background_f

@background_task
@app.get("/parse")
def get_thing_to_db():
    get_plates_to_db()
    get_memory_to_db()
    get_power_to_db()
    get_shells_to_db()
    get_proccesors_to_db()
    get_coolers_to_db()
    get_graphic_cards_to_db()
    with open("static/programm_constants.txt", "w") as f:
        f.write(f"last_time_bd_update = {datetime.datetime.now().date()}")
    return redirect("/main_page")

@app.get("/get")
def choose_thing():
    thing = request.args.get('thing')
    uid = request.args.get('uid')
    if thing == 'plate':
        controlling_array[0] = int(uid)
    if thing == 'memory':
        controlling_array[1] = int(uid)
    if thing == 'power':
        controlling_array[2] = int(uid)
    if thing == 'shell':
        controlling_array[3] = int(uid)
    if thing == 'proccesor':
        controlling_array[4] = int(uid)
    if thing == 'cooler':
        controlling_array[5] = int(uid)
    if thing == 'graphic_card':
        controlling_array[6] = int(uid)
    return redirect("/main_page")

@app.get("/remove")
def remove_thing():
    thing = request.args.get('thing')
    if thing == 'plate':
        controlling_array[0] = 0
    if thing == 'memory':
        controlling_array[1] = 0
    if thing == 'power':
        controlling_array[2] = 0
    if thing == 'shell':
        controlling_array[3] = 0
    if thing == 'proccesor':
        controlling_array[4] = 0
    if thing == 'cooler':
        controlling_array[5] = 0
    if thing == 'graphic_card':
        controlling_array[6] = 0
    return redirect("/main_page")


@app.get("/main_page")
def main_page():
    summ = 0
    if controlling_array[0] != 0:
        buff_storage.plate = bd_repository.get_plate_from_db(controlling_array[0])
        summ += buff_storage.plate.price
    else:
        buff_storage.plates = bd_repository.choose_plates()
    if controlling_array[1] != 0:
        buff_storage.memory = bd_repository.get_memory_from_db(controlling_array[1])
        summ += buff_storage.memory.price
    else:
        buff_storage.memories = bd_repository.choose_memory()
    if controlling_array[2] != 0:
        buff_storage.power = bd_repository.get_power_from_db(controlling_array[2])
        summ += buff_storage.power.price
    else:
        buff_storage.powers = bd_repository.choose_power()
    if controlling_array[3] != 0:
        buff_storage.shell = bd_repository.get_shell_from_db(controlling_array[3])
        summ += buff_storage.shell.price
    else:
        buff_storage.shells = bd_repository.choose_shells()
    if controlling_array[4] != 0:
        buff_storage.proccesor = bd_repository.get_proccesor_from_db(controlling_array[4])
        summ += buff_storage.proccesor.price
    else:
        buff_storage.proccesors = bd_repository.choose_proccesors()
    if controlling_array[5] != 0:
        buff_storage.cooler = bd_repository.get_cooler_from_db(controlling_array[5])
        summ += buff_storage.cooler.price
    else:
        buff_storage.coolers = bd_repository.choose_coolers()
    if controlling_array[6] != 0:
        buff_storage.graphic_card = bd_repository.get_graphic_card_from_db(controlling_array[6])
        summ += buff_storage.graphic_card.price
    else:
        buff_storage.graphic_cards = bd_repository.choose_graphic_cards()
    with open("static/programm_constants.txt", "r") as f:
        constants = f.readlines()
        last_time_updated = constants[0].split("=")[1].strip()
        year = int(last_time_updated.split("-")[0])
        month = int(last_time_updated.split("-")[1])
        day = int(last_time_updated.split("-")[2])
        time_updated = datetime.date(year, month, day)
    return render_template('mainpage.html', controlling_array=controlling_array, buff_storage=buff_storage, sum=summ, last_time_updated=time_updated)


if __name__ == "__main__":
    db_session.global_init("db/components.db")
    app.run(host="0.0.0.0")


