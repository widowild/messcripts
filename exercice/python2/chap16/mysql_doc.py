db = MySQLdb.Connect(user="freddy", passwd="bcz45", db="club"
                        [, host="192.168.0.125", port=3306, unix_socket=..)


# cr�ation du curseur :
cursor = db.cursor()

# affichage des champs pr�sents dans la table active : 
for cursorFieldName in cursor.description:
    print cursorFieldName

# requ�te type :
ref = cursor.execute("SELECT * FROM membres")
# ref contiendra le n� de r�f�rence du dernier enreg. trouv�

# autre exemple avec une variable python :
max_price = 5
cursor.execute("""SELECT spam, eggs, sausage FROM breakfast
            WHERE price < %s""", (max_price,))

# pourquoi un tuple pour s% ?
# parce que les param�tres attendus par la DB API sont des s�quences

# transfert du r�sultat de la requ�te de s�lection dans un tuple de tuples :
res = cursor.fetchall()

# tables accessibles (c'est une requ�te comme une autre) :
cursor.execute("show tables")
print cursor.fetchall()			# il s'agira d'un tuple

# fermetures :
db.commit()		# termine la transaction
db.rollback()		# annule la transaction (pas toujours possible)
cursor.close() 
db.close()

Fetch row as dictionary :
not standard; alternate cursor class DictCursor
provides a dictionary interface,keys are "column" or "table.column"
if there are two columns with the same name; use SQL AS to rename fields.


