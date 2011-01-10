#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Le nombre de secondes est fourni au départ :
# (un grand nombre s'impose !)
nsd = 12345678912

# Nombre de secondes dans une journée :
nspj = 3600 * 24
# Nombre de secondes dans un an (soit 365 jours -
# on ne tiendra pas compte des années bissextiles) :
nspa = nspj * 365
# Nombre de secondes dans un mois (en admettant
# pour chaque mois une durée identique de 30 jours) :
nspm = nspj * 30
# Nombre d'années contenues dans la durée fournie :
na = nsd // nspa        # division <entière>
nsr = nsd % nspa        # n. de sec. restantes
# Nombre de mois restants :
nmo = nsr // nspm       # division <entière>
nsr = nsr % nspm        # n. de sec. restantes
# Nombre de jours restants :
nj = nsr // nspj        # division <entière>
nsr = nsr % nspj        # n. de sec. restantes
# Nombre d'heures restantes :
nh = nsr // 3600        # division <entière>
nsr = nsr % 3600        # n. de sec. restantes
# Nombre de minutes restantes :
nmi = nsr // 60         # division <entière>
nsr = nsr % 60          # n. de sec. restantes

print("Nombre de secondes à convertir :", nsd)
print("Cette durée correspond à", na, "années de 365 jours, plus")
print(nmo, "mois de 30 jours,", end=' ')
print(nj, "jours,", end=' ')
print(nh, "heures,", end=' ')
print(nmi, "minutes et", end=' ')
print(nsr, "secondes.")
