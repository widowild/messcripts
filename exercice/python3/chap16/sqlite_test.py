#! /usr/bin/env python
# -*- coding:Utf8 -*-

import sqlite3

# Création d'un objet "connexion" (objet-interface) :
dataFile ="sqlite_data"
conn = sqlite3.connect(dataFile)
# Également possible : création d'une base de données en RAM :
#conn = sqlite3.connect(:memory:)

conn.isolation_level =None          # => autocommit        
# Création d'un "curseur"
c = conn.cursor()

# Création d'une table
try:
    c.execute("create table stocks (date text, trans text, symbol text, "\
              "qty real, price real)")
except:
    pass
# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")
# Save (commit) the changes
#conn.commit()


# Never do this -- insecure!
# symbol = 'IBM'
# c.execute("... where symbol = '%s'" % symbol)
# Do this instead
# t = (symbol,)
# c.execute('select * from stocks where symbol=?', t)

# Larger example
for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
         ]:
    c.execute('insert into stocks values (?,?,?,?,?)', t)
# Save (commit) the changes
#conn.commit()

c.close()              # Refermer le curseur
conn.close()           # Fermer la connexion avec la BD

# Ré-ouvrir la BD :
conn = sqlite3.connect(dataFile)
c = conn.cursor()
c.execute("SELECT * FROM stocks ORDER BY price")
# Le curseur est un itérateur : =>
#for row in c:
#    print(row)

rows =list(c)
print(rows)

c.close()              # Refermer le curseur
conn.close()           # Fermer la connexion avec la BD

