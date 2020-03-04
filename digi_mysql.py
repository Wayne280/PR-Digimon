# PR 3: digimon
#14 col = 13 col + 1 picture
# format: http://digidb.io/digimon-list/
# => json
# => csv
# => excel
# => mongodb db=digimon col=digimon
# => mysql db=digimon col=digimon

from bs4 import BeautifulSoup
import requests

url = 'http://digidb.io/digimon-list/'
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

#find table where the data is located
table = soup.find(id='digiList') #digilist merupakan judul id tabel pada html

label = []
for i in table.find_all('th'): #th merupakan header
    label.append(i.text)
label.insert(1, 'Picture')

#Ambil gambar
img = []
for i in table.find_all('img'): #ambil semua image
    img.append(i.get('src'))

data = []
for i in table.find_all('td'): #ambil semua td di dalam table
    data.append(i.text)

num = []
indexnum = list(range(0,len(data), 13))
digimon = []
indexdigimon = list(range(1, len(data),13))
stage = []
indexstage = list(range(2, len(data),13))
type_ = []
indextype_ = list(range(3, len(data),13))
attribute = []
indexattribute = list(range(4, len(data),13))
memory = []
indexmemory = list(range(5, len(data), 13))
equip_slot = []
indexequip_slot = list(range(6, len(data), 13))
hp = []
indexhp = list(range(7, len(data),13))
sp = []
indexsp = list(range(8, len(data),13))
atk = []
indexatk = list(range(9, len(data),13))
def_ = []
indexdef_ = list(range(10, len(data),13))
int_ = []
indexint_ = list(range(11, len(data),13))
spd = []
indexspd = list(range(12, len(data),13))

for i in range (len(data)):
    if i in indexnum:
        num.append(data[i][1:])
    elif i in indexdigimon:
        digimon.append(data[i][2:])
    elif i in indexstage:
        stage.append(data[i])
    elif i in indextype_:
        type_.append(data[i])
    elif i in indexattribute:
        attribute.append(data[i])
    elif i in indexmemory:
        memory.append(data[i])
    elif i in indexequip_slot:
        equip_slot.append(data[i])
    elif i in indexhp:
        hp.append(data[i])
    elif i in indexsp:
        sp.append(data[i])
    elif i in indexatk:
        atk.append(data[i])
    elif i in indexdef_:
        def_.append(data[i])
    elif i in indexint_:
        int_.append(data[i])
    elif i in indexspd:
        spd.append(data[i])

datadigimon = []
for i in range (len(num)):
    datadigimon.append({
        label[0] : num[i],
        label[1] : img[i],
        label[2] : digimon[i],
        label[3] : stage[i],
        label[4] : type_[i],
        label[5] : attribute[i],
        label[6] : memory[i],
        label[7] : equip_slot[i],
        label[8] : hp[i],
        label[9] : sp[i],
        label[10] : atk[i],
        label[11] : def_[i],
        label[12] : int_[i],
        label[13] : spd[i],
    })

#convert list of dictionary to list of tuple
convert = []
for i in datadigimon:
    x = i.values()
    x = tuple(x)
    convert.append(x)
print(convert)

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = 'Kadalapi280', 
    database = 'digi_mysql'
)

# cursor = mydb.cursor()

# cursor.execute('create table mydigimon(No int, image varchar(100), Digimon varchar(100),Stage varchar(100), Type_ varchar(100), Attribute varchar(100), Memory varchar(100), Equip_slots int,HP int, SP int, Atk int, Def_ int, Int_ int, Spd int)')

# sql = 'Insert into mydigimon (No, image, Digimon,Stage, Type_, Attribute, Memory, Equip_slots,HP, SP, Atk, Def_, Int_, Spd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# val = convert
# cursor.executemany(sql, val)
# mydb.commit()
# print(cursor.rowcount, "Data tersimpan!")