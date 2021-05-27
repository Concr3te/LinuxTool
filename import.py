import csv, sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE ipv4 (start_range, end_range, country_code, country_name);")

with open('IP2LOCATION-LITE-DB1.CSV','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['start_range'], i['end_range'], i['country_code'], i['country_name']) for i in dr]

cur.executemany("INSERT INTO ipv4 (start_range, end_range, country_code, country_name) VALUES (?,?,?,?);", to_db)
con.commit()

con = sqlite3.connect("database.db") 
cur = con.cursor()
cur.execute("CREATE TABLE ipv6 (start_range, end_range, country_code, country_name);")

with open('IP2LOCATION-LITE-DB1.IPV6.CSV','r') as fin:
    dr = csv.DictReader(fin) 
    to_db = [(i['start_range'], i['end_range'], i['country_code'], i['country_name']) for i in dr]

cur.executemany("INSERT INTO ipv6 (start_range, end_range, country_code, country_name) VALUES (?,?,?,?);", to_db)
con.commit()

con.close()
