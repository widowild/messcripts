from math import sin, cos, tan, pi

# Construction de l'en-t�te du tableau avec les titres de colonnes :
print """<TABLE BORDER="1" CELLPADDING="5">
<TR><TD>Angle</TD><TD>Sinus</TD><TD>Cosinus</TD><TD>Tangente</TD></TR>"""

for angle in range(0,62,10):    
    # conversion des degr�s en radians :
    aRad = angle * pi / 180
    # construction d'une ligne de tableau, en exploitant le formatage des
    # cha�nes de caract�res pour fignoler l'affichage :
    print "<TR><TD>%s</TD><TD>%8.7f</TD><TD>%8.7f</TD><TD>%8.7g</TD><TR>" %\
        (angle, sin(aRad), cos(aRad), tan(aRad))
    
print "</TABLE>"




