#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Le nombre de secondes est fourni au d�part :
# (un grand nombre s'impose !)
nsd = 12345678912

# Nombre de secondes dans une journ�e :
nspj = 3600 * 24
# Nombre de secondes dans un an (soit 365 jours -
# on ne tiendra pas compte des ann�es bissextiles) :
nspa = nspj * 365
# Nombre de secondes dans un mois (en admettant
# pour chaque mois une dur�e identique de 30 jours) :
nspm = nspj * 30
# Nombre d'ann�es contenues dans la dur�e fournie :
na = nsd / nspa         # division <enti�re>
nsr = nsd % nspa        # n. de sec. restantes
# Nombre de mois restants :
nmo = nsr / nspm        # division <enti�re>
nsr = nsr % nspm        # n. de sec. restantes
# Nombre de jours restants :
nj = nsr / nspj         # division <enti�re>
nsr = nsr % nspj        # n. de sec. restantes
# Nombre d'heures restantes :
nh = nsr / 3600         # division <enti�re>
nsr = nsr % 3600        # n. de sec. restantes
# Nombre de minutes restantes :
nmi = nsr /60           # division <enti�re>
nsr = nsr % 60          # n. de sec. restantes

print "Nombre de secondes � convertir :", nsd
print "Cette dur�e correspond �", na, "ann�es de 365 jours, plus"
print nmo, "mois de 30 jours,",
print nj, "jours,",
print nh, "heures,",
print nmi, "minutes et",
print nsr, "secondes."
