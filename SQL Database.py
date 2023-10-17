import sqlite3
conn = sqlite3.connect('data.db')
curs = conn.cursor()

guide="""CREATE TABLE IF NOT EXISTS GUIDE (
                    name TEXT, 
                    degree TEXT, 
                    direction TEXT, 
                    department TEXT, 
                    post TEXT, 
                    country TEXT, 
                    city TEXT, 
                    adress TEXT, 
                    phone INT, 
                    email VARCHAR(20) 
                    );"""

# userguide1=('Irina',
#             'Bachelor',
#             'Medicine',
#             'Hospital',
#             'surgery',
#             'Spain',
#             'Madrid',
#             'Azalova St. 1',
#             87654321,
#             'irina@gmail.com')
# userguide2=('Mike',
#             'Bachelor',
#             'Power supply',
#             'Power plant',
#             'chief power engineer',
#             'UK',
#             'London',
#             'Rouge St. 2',
#             12356484,
#             'mike@gmail.com')
# userguide3=('Gleb',
#             'Bachelor',
#             'Power supply',
#             'Power plant',
#             'chief power engineer',
#             'Belarus',
#             'Minsk',
#             'Backery St. 3',
#             12345678,
#             'gleb@gmail.com')
# userguide4=('Arthur',
#             'Bachelor',
#             'Medicine',
#             'Hospital',
#             'surgery',
#             'Russia',
#             'Moskow',
#             'Russo St. 4',
#             87654321,
#             'arthur@gmail.com')
# userguide5=('Denis',
#             'Bachelor',
#             'Medicine',
#             'Hospital',
#             'surgery',
#             'UK',
#             'Amsterdam',
#             'Wall St. 5',
#             20508010,
#             'denis@gmail.com')
# userguide6=('Walter',
#             'Bachelor',
#             'Power supply',
#             'Power plant',
#             'chief power engineer',
#             'Argentina',
#             'Buenos Aires',
#             'Hight St. 6',
#             79461352,
#             'walter@gmail.com')
userguide=(('Irina',
            'Bachelor',
            'Medicine',
            'Hospital',
            'surgery',
            'Spain',
            'Madrid',
            'Azalova St. 1',
            87654321,
            'irina@gmail.com'),('Mike',
            'Bachelor',
            'Power supply',
            'Power plant',
            'chief power engineer',
            'UK',
            'London',
            'Rouge St. 2',
            12356484,
            'mike@gmail.com'),('Gleb',
            'Bachelor',
            'Power supply',
            'Power plant',
            'chief power engineer',
            'Belarus',
            'Minsk',
            'Backery St. 3',
            12345678,
            'gleb@gmail.com'),('Arthur',
            'Bachelor',
            'Medicine',
            'Hospital',
            'surgery',
            'Russia',
            'Moskow',
            'Russo St. 4',
            87654321,
            'arthur@gmail.com'),('Denis',
            'Bachelor',
            'Medicine',
            'Hospital',
            'surgery',
            'UK',
            'Amsterdam',
            'Wall St. 5',
            20508010,
            'denis@gmail.com'),('Walter',
            'Bachelor',
            'Power supply',
            'Power plant',
            'chief power engineer',
            'Argentina',
            'Buenos Aires',
            'Hight St. 6',
            79461352,
            'walter@gmail.com'))
guidedata= "INSERT INTO GUIDE VALUES (?,?,?,?,?,?,?,?,?,?);"

info="""CREATE TABLE IF NOT EXISTS INFO (
                    ifparticipant SMALLINT,
                    ifspeaker SMALLINT,
                    invitedate DATE,
                    receiptdate DATE,
                    report TEXT,
                    thesis SMALLINT,
                    arrivaldate DATE,
                    hotel SMALLINT,
                    leavedate DATE
                    );"""

# userinfo1=(True,
#         False,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         True,
#         '25.02.2022',
#         False,
#         '27.02.2022')
# userinfo2=(False,
#         True,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         False,
#         '25.02.2022',
#         True,
#         '27.02.2022')
# userinfo3=(True,
#         False,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         True,
#         '25.02.2022',
#         False,
#         '27.02.2022')
# userinfo4=(True,
#         False,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         True,
#         '25.02.2022',
#         False,
#         '27.02.2022')
# userinfo5=(True,
#         False,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         True,
#         '25.02.2022',
#         False,
#         '27.02.2022')
# userinfo6=(True,
#         False,
#         '20.02.2022',
#         '22.02.2022',
#         'lightning',
#         True,
#         '25.02.2022',
#         False,
#         '27.02.2022')
userinfo=((True,
        False,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        True,
        '25.02.2022',
        False,
        '27.02.2022'),(False,
        True,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        False,
        '25.02.2022',
        True,
        '27.02.2022'),(True,
        False,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        True,
        '25.02.2022',
        False,
        '27.02.2022'),(True,
        False,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        True,
        '25.02.2022',
        False,
        '27.02.2022'),(True,
        False,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        True,
        '25.02.2022',
        False,
        '27.02.2022'),(True,
        False,
        '20.02.2022',
        '22.02.2022',
        'lightning',
        True,
        '25.02.2022',
        False,
        '27.02.2022'))
infodata= "INSERT INTO INFO VALUES (?,?,?,?,?,?,?,?,?);"


conf="""CREATE TABLE IF NOT EXISTS CONF (
                    conftitle TEXT,
                    eventdate DATE,
                    venue TEXT,
                    organizers TEXT,
                    sponsors TEXT,
                    confdays INT,
                    participantnum INT,
                    speakernum INT 
                    );"""

# conf1=('lighting equipment',
#     '26.02.2022',
#     'Vilnus',
#     'OVERONE',
#     'SpaseX',
#     1,
#     10,
#     20)
# conf2=('lighting equipment',
#     '26.02.2022',
#     'Rome',
#     'OVERONE',
#     'SpaseX',
#     1,
#     12,
#     21)
# conf3=('lighting equipment',
#     '26.02.2022',
#     'New-York',
#     'OVERONE',
#     'SpaseX',
#        1,
#        120,
#        200)
# conf4=('lighting equipment',
#     '26.02.2022',
#     'Vilnus',
#     'OVERONE',
#     'SpaseX',
#     1,
#     10,
#     20)
# conf5=('lighting equipment',
#     '26.02.2022',
#     'Vilnus',
#     'OVERONE',
#     'SpaseX',
#     1,
#     10,
#     20)
# conf6=('lighting equipment',
#     '26.02.2022',
#     'Vilnus',
#     'OVERONE',
#     'SpaseX',
#     1,
#     10,
#     20)
Conf=(('lighting equipment',
    '26.02.2022',
    'Vilnus',
    'OVERONE',
    'SpaseX',
    1,
    10,
    20),('lighting equipment',
    '26.02.2022',
    'Rome',
    'OVERONE',
    'SpaseX',
    1,
    12,
    21),('lighting equipment',
    '26.02.2022',
    'New-York',
    'OVERONE',
    'SpaseX',
       1,
       120,
       200),('lighting equipment',
    '26.02.2022',
    'Vilnus',
    'OVERONE',
    'SpaseX',
    1,
    10,
    20),('lighting equipment',
    '26.02.2022',
    'Vilnus',
    'OVERONE',
    'SpaseX',
    1,
    10,
    20),('lighting equipment',
    '26.02.2022',
    'Vilnus',
    'OVERONE',
    'SpaseX',
    1,
    10,
    20))
confdata= "INSERT INTO CONF VALUES (?,?,?,?,?,?,?,?);"

curs.execute(guide)
conn.commit()
curs.execute(conf)
conn.commit()
curs.execute(info)
conn.commit()

for i in userguide:
    conn.execute(guidedata,i)
    conn.commit()
for j in userinfo:
    conn.execute(infodata,j)
    conn.commit()
for n in Conf:
    conn.execute(confdata,n)
    conn.commit()

# fetch1="""SELECT * FROM GUIDE;"""
# curs.execute(fetch1)
# Fetch1=curs.fetchall()
# print(Fetch1)
# print('*'*1000)
# fetch2="""SELECT * FROM CONF WHERE venue='Rome';"""
# curs.execute(fetch2)
# Fetch2=curs.fetchall()
# print(Fetch2)
#
guidelite="""DELETE FROM GUIDE WHERE direction = 'Power supply';"""
curs.execute(guidelite)
conn.commit()
guideupdate="""UPDATE GUIDE SET name='user' WHERE direction='Medicine'; """
curs.execute(guideupdate)
conn.commit()
infodelite="""DELETE FROM INFO WHERE hotel=False;"""
curs.execute(infodelite)
conn.commit()
infoupdate="""UPDATE INFO SET leavedate='30.02.2023' WHERE hotel=True;"""
curs.execute(infoupdate)
conn.commit()
confdelete="""DELETE FROM CONF WHERE speakernum=20;"""
curs.execute(confdelete)
conn.commit()
confupdate="""UPDATE CONF SET conftitle='IT progress' WHERE organizers='OVERONE';"""
curs.execute(confupdate)
conn.commit()

curs.close()
conn.close()