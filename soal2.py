import sqlite3

#  database
conn = sqlite3.connect('mahasiswa.db')

# object
cur = conn.cursor()

# tabel mahasiswa
cur.execute('''
    CREATE TABLE IF NOT EXISTS Mahasiswa (
        22030012,
        irma,
        kadekwahyuni2110@gmailcom
    )
''')

# masukan data
mahasiswas = [
    {'nim': '22030012', 'nama': 'irma', 'email': 'kadekwahyuni2110@gmailcom'},
    
]

for mahasiswa in mahasiswas:
    cur.execute('''
        INSERT INTO Mahasiswa (nim, nama, email)
        VALUES (?, ?, ?)
    ''', (mahasiswa['22030012'], mahasiswa['irma'], mahasiswa['kadekwahyuni2110@gmailcom']))


conn.commit()
conn.close()