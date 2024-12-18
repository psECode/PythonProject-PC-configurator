import requests
from bs4 import BeautifulSoup
import re

from backend.models import Plate, GraphicCard, Proccesor, Cooler, Memory, Shell, Power


def get_plates():
    plates_data = []
    for i in range(1, 18):
        request = requests.get(
            f"https://www.knsperm.ru/catalog/komplektuyuschie/materinskie-platy/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_plate = Plate()
            buff_plate.price = int(plate.find("meta", itemprop="price")['content'])
            buff_plate.name = plate.find("span", itemprop="name").text
            if "MikroTik" not in buff_plate.name and "Advantech" not in buff_plate.name and "Esonic" not in buff_plate.name:
                name_preparation = '-'.join(buff_plate.name.split()[2:]).lower().strip()
                name_preparation = name_preparation.replace("/", "-")
                name_preparation = name_preparation.replace(".", "-")
                characteristics = requests.get(
                    f"https://www.knsperm.ru/product/materinskaya-plata-{name_preparation}/characteristics/")
                characteristics_soup = BeautifulSoup(characteristics.text, 'html.parser')
                if characteristics_soup.find('div', string=re.compile("МГц")):
                    mgc = characteristics_soup.find('div', string=re.compile("МГц")).text
                    mgc = mgc.replace("МГц", "").strip()
                    mgc = mgc.replace("+", "").strip()
                    mgc = mgc.replace("-", "").strip()
                    buff_min_max_memory = []
                    if len(mgc.split()) > 1:
                        buff_min_max_memory.append(mgc.split()[0])
                        buff_min_max_memory.append(mgc.split()[1])
                    else:
                        buff_min_max_memory.append(mgc)
                        buff_min_max_memory.append(mgc)
                    buff_plate.mgc = ' '.join(buff_min_max_memory)
                    description = plate.find("div", itemprop="description")
                    information = description.text.split(',')
                    buff_plate.form_factor = information[0].split()[1].strip()
                    buff_plate.chipset = information[1].split()[1].strip()
                    if 'сокет' in description.text:
                        socket = description.text.split('сокет')[1][1:].split(',')[0].strip()
                    else:
                        pass
                    buff_plate.socket = socket
                    if ':' in information[3]:
                        slots = information[3].split(':')[1].strip()
                    else:
                        pass
                    buff_plate.slots = slots[slots.find("DDR"):slots.find("DDR") + 4]
                    image = plate.find("img", itemprop="image")
                    buff_plate.img = image['src']
                    buff_plate.uid = plate.find('a', itemprop='url')['data-ga-id']
                    plates_data.append(buff_plate)
    return plates_data

def get_graphic_cards():
    ports = ["DisplayPort", "HDMI", "D-Sub", "DVI-D", "DVI", "VGA"]
    graphic_cards_data = []
    for i in range(1, 17):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/videokarty/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_card = GraphicCard()
            buff_card.name = plate.find("span", itemprop="name").text
            if "Видеоплата" not in buff_card.name and "Видеоплата" not in plate.find("div", itemprop="description").text:
                buff_card.price = int(plate.find("meta", itemprop="price")['content'])
                if "nVidia" in buff_card.name:
                    buff_card.nVidia = True
                else:
                    buff_card.nVidia = False
                description = plate.find("div", itemprop="description")
                information = description.text.split(':')
                buff_card.memory = information[1].strip().split()[0].strip()
                buff_card.memory_type = information[2].strip().split()[0].strip()
                buff_plugs = []
                for port in ports:
                    if port in information[-1].strip():
                        buff_plugs.append(port)
                buff_card.plugs = ' '.join(buff_plugs)
                image = plate.find("img", itemprop="image")
                buff_card.img = image['src']
                buff_card.uid = plate.find('a', itemprop='url')['data-ga-id']
                if buff_card.price <= 90000:
                    buff_card.power = int((buff_card.price - 2873) / 127127 * 400 + 150)
                    graphic_cards_data.append(buff_card)
    return graphic_cards_data

def get_proccesors():
    proccesors_data = []
    for i in range(1, 12):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/protsessory/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_procc = Proccesor()
            buff_procc.name = plate.find("span", itemprop="name").text
            buff_procc.price = int(plate.find("meta", itemprop="price")['content'])
            if "Xeon" not in buff_procc.name:
                description = plate.find("div", itemprop="description")
                information = description.text.split(',')
                buff_procc.core_count = information[1].strip().split('-')[0].strip()
                buff_procc.socket = information[0].split()[1].strip()
                buff_procc.mgc = int(information[2].replace('Performance-core', '').strip().split()[0].strip())
                power = description.text.split('Вт')[0].strip().split()[-1].strip()
                if '-' in power:
                    buff_procc.power = int(power.split('-')[1])
                else:
                    buff_procc.power = int(power)
                image = plate.find("img", itemprop="image")
                buff_procc.img = image['src']
                if 'Intel' in buff_procc.name:
                    buff_procc.intel = True
                buff_procc.uid = plate.find('a', itemprop='url')['data-ga-id']
                proccesors_data.append(buff_procc)

    return proccesors_data

def get_coolers():
    coolers_data = []
    for i in range(1, 29):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/kulery/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_cooler = Cooler()
            buff_cooler.vent_count = 1
            buff_cooler.name = plate.find("span", itemprop="name").text
            buff_cooler.price = int(plate.find("meta", itemprop="price")['content'])
            description = plate.find("div", itemprop="description")
            if len(description.text.split(
                    ',')) > 1 and "процессора" in description.text and 'СВО' not in description.text and "Кулер" in \
                    buff_cooler.name:
                sockets = description.text.split(':')[1].strip().split('количество')[0].strip()
                sockets = sockets.replace('/', ',')
                sockets = sockets.split(',')[:-1]
                buff_sockets = []
                for socket in sockets:
                    buff_sockets.append(socket.strip())
                buff_cooler.sockets = ' '.join(buff_sockets)
                if "количество вентиляторов" in description.text:
                    buff_cooler.vent_count = int(description.text.split('вентиляторов')[1].split(',')[0].strip())
                elif "количество тепловых трубок" in description.text:
                    buff_cooler.vent_count = 0
                buff_cooler.power = buff_cooler.vent_count * 15
                image = plate.find("img", itemprop="image")
                buff_cooler.img = image['src']
                buff_cooler.uid = plate.find('a', itemprop='url')['data-ga-id']
                coolers_data.append(buff_cooler)
    return coolers_data

def get_memory():
    memory_data = []
    for i in range(1, 50):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/pamyat/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_memory = Memory()
            buff_memory.name = plate.find("span", itemprop="name").text
            buff_memory.price = int(plate.find("meta", itemprop="price")['content'])
            description = plate.find("div", itemprop="description")
            if 'SODIMM' not in description.text:
                if "объём" in description.text and int(description.text.split('объём')[1][2:3]) == 2:
                    buff_memory.ddr = description.text.split(',')[0].strip()
                    mgc = description.text.split(',')[2].strip().split(':')[1].strip()
                    buff_memory.mgc = int(mgc.replace("MHz", "").strip())
                    image = plate.find("img", itemprop="image")
                    buff_memory.img = image['src']
                    buff_memory.uid = plate.find('a', itemprop='url')['data-ga-id']
                    memory_data.append(buff_memory)
    return memory_data

def get_shells():
    form_factors = ['Mini-ITX', 'ATX', 'mATX', 'E-ATX', 'Mini ITX', 'Micro-ATX', 'EATX', 'Standard-ATX', 'microATX',
                    'SSI-EEB', 'Mini-DTX']
    shells_data = []
    for i in range(1, 21):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/korpusa/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_shell = Shell()
            description = plate.find("div", itemprop="description")
            buff_shell.name = plate.find("span", itemprop="name").text
            buff_shell.price = int(plate.find("meta", itemprop="price")['content'])
            buff_form_factor = []
            for ff in form_factors:
                if ff in description.text:
                    buff_form_factor.append(ff)
            buff_shell.form_factor = ' '.join(buff_form_factor)
            buff_shell.img = plate.find("img")['src']
            buff_shell.uid = plate.find('a', itemprop='url')['data-ga-id']
            shells_data.append(buff_shell)
    return shells_data

def get_power():
    form_factors = ['Mini-ITX', 'ATX', 'mATX', 'E-ATX', 'Mini ITX', 'Micro-ATX', 'EATX', 'Standard-ATX', 'microATX',
                    'SSI-EEB', 'Mini-DTX', 'SFX', 'SFX-ATX', 'SFX-ITX', 'SFX-ATX-ITX']
    power_data = []
    for i in range(1, 15):
        request = requests.get(f"https://www.knsperm.ru/catalog/komplektuyuschie/bloki-pitaniya/page{i}")
        soup = BeautifulSoup(request.text, 'html.parser')
        all_plates = soup.find_all("div", itemtype="http://schema.org/Product")
        for plate in all_plates:
            buff_power = Power()
            description = plate.find("div", itemprop="description")
            buff_power.name = plate.find("span", itemprop="name").text
            buff_power.price = int(plate.find("meta", itemprop="price")['content'])
            if description.text[:8] == 'Мощность' and 'для материнской платы' in description.text:
                buff_power.power = int(
                    description.text.split(':')[1].split(',')[0].replace('Вт', '').replace('W', '').strip())
                buff_form_factor = []
                for ff in form_factors:
                    if ff in description.text:
                        buff_form_factor.append(ff)
                buff_power.form_factor = ' '.join(buff_form_factor)
                pos = description.text.find('материнской платы')
                buff_power.pins = int(
                    description.text[pos:].split(':')[1].split('pin')[0].replace('+', ' ').strip().split()[0])
                buff_power.img = plate.find("img")['src']
                buff_power.uid = plate.find('a', itemprop='url')['data-ga-id']
                power_data.append(buff_power)
    return power_data

if __name__ == "__main__":
    print(get_plates())