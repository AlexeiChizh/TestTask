

import sqlite3

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Personal(id int, firstname Varchar(32), lastname Varchar(32), skill Varchar(32))''')
cursor.executemany('''INSERT INTO Personal VALUES (?,?,?,?,)''', [(1, 'Ivan', 'Ivanov', 'electronics'),
																  (2, 'Petr', 'Petrov', 'electrician'),
																  (3, 'Sidor', 'Sidorov', 'administrator'),
																  (4, 'Fedor', 'Fedorov', 'consultant')
																  ])																  

cursor.execute('''CREATE TABLE Project(id int, title Varchar(50))''')
cursor.executemany('''INSERT INTO Project VALUES (?,?)''', [(1, 'computer_repair'),
														    (2, 'softwear_instalation'),
														    (3, 'server_repair'),
														    (4, 'low-current_electrics'),
														    (5, 'user_consultation')
														    ])

cursor.execute('''CREATE TABLE Object(id int, name Varchar(50), region Varchar(32), subregion Varchar(32), city Varchar(32), street Varchar(32), building int))''')
cursor.executemany('''INSERT INTO Object VALUES (?,?,?,?,?,?,?)''', [(1, 'Ilon Limited', 'Russia', 'Moscow Region', 'Moscow', 'Leninsky', 45),
																     (2, 'Mask Limited', 'Russia', 'Moscow Region', 'Domodedovo', 'Pervaya', 4),
																     (3, 'Donald Limited', 'Russia', 'Moscow Region', 'Moscow', 'Dmitrovskoe', 90),
																     (4, 'Trump Limited', 'Russia', 'Moscow Region', 'Podolsk', 'Industrialnaya', 21),
																     (5, 'Blackmore Limited, Russia', 'Moscow Region', 'Odintsovo', 'Vesennaya', 145),
																     (6, 'Derris Limited', 'Russia', 'Moscow Region', 'Moscow', 'Kashirskoe', 32),
																     (7, 'Marcus Limited', 'Russia', 'Moscow Region', 'Golitsyno', 'Lesnaya', 111)
																     ])


cursor.execute('''CREATE TABLE Accordance(personal_id int, project_id int, object_id int)''')
cursor.executemany('''INSERT INTO Accordance VALUES (?, ?, ?)''', [(1, 3, 5),
																   (2, 4, 6),
																   (3, 5, 5),
																   (4, 1, 3),
																   (2, 4, 1)
																   ])

conn.commit()

conn.close()
