#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Affichage d'un formulaire HTML simplifi� :
print "Content-Type: text/html\n"
print """
<H3><FONT COLOR="Royal blue">
Page web produite par un script Python
</FONT></H3>

<FORM ACTION="print_result.py" METHOD="post">
<P>Veuillez entrer votre nom dans le champ ci-dessous, s.v.p. :</P>
<P><INPUT NAME="visiteur" SIZE=20 MAXLENGTH=20 TYPE="text"></P>
<P>Veuillez �galement me fournir une phrase quelconque :</P>
<TEXTAREA NAME="phrase" ROWS=2 COLS=50>Mississippi</TEXTAREA>
<P>J'utiliserai cette phrase pour �tablir un histogramme.</P>
<INPUT TYPE="submit" NAME="send" VALUE="Action">
</FORM>
"""

