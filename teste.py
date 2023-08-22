import cmath

c1 = complex(3, 4)
c2 = complex(1, 2)

print(f"c1 = {c1}")
print(f"c2 = {c2}")

addition = c1 + c2
soustraction = c1 - c2
multiplication = c1 * c2
division = c1 / c2

print(f"Addition : {addition}")
print(f"Soustraction : {soustraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")

norme_c1 = abs(c1)
conjugue_c2 = c2.conjugate()

print(f"Norme de c1 : {norme_c1}")
print(f"Conjugé de c2 : {conjugue_c2}")

racine_carree_c1 = cmath.sqrt(c1)
racine_carree_c2 = cmath.sqrt(c2)

print(f"Racine carrée de c1 : {racine_carree_c1}")
print(f"Racine carrée de c2 : {racine_carree_c2}")

cosinus_c1 = cmath.cos(c1)
sinus_c2 = cmath.sin(c2)

print(f"Cosinus de c1 : {cosinus_c1}")
print(f"Sinus de c2 : {sinus_c2}")
