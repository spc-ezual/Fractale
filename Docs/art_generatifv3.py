import time
from PIL import Image, ImageDraw
from random import randint,uniform
from cmath import cos, cosh,sinh,sin
from math import ceil
import numpy as np
#from noise import pnoise2


#------------------------------------------------------------------------------
#Equation quadratique qui verifie si un point part ou si il reste
#si il part on a le nombre i qui est le nombre nececaire d'itertion anvans que il ne parte

def quadratique(z,constante,pressision):
    i=0
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<4 and rep<=pressision:
        i=0
        rep+=1
        while dis<4 and i<271:
            z=z**2+constante
            i+=1
            dis=z.imag**2+z.real**2
    return i
#-------------------------------------------------------------------------------
#equation autres pour l'ensemble des fractal

def cosin(constante,pressision):
    if constante==complex(0,0):return 271
    i=0
    z=constante
    rep=1
    while z.imag**2+z.real**2<50 and rep<=pressision:
        i=0
        rep+=1
        while z.imag**2+z.real**2<50 and i<271:
            z=cosh(z/constante)
            i+=1
    return i+60

def puissance(z,constante,pressision):
    i=0
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        i=0
        rep+=1
        while dis<4 and i<271:
            z=z**2+constante**3-1.401155
            i+=1
            dis=z.imag**2+z.real**2
    return i

def conjug(z,constante,pressision):
    i=0
    rep=1
    z=complex(0,1)
    dis=constante.imag**2+constante.real**2
    while dis<5 and rep<=pressision:
        i=0
        rep+=1
        while dis<4 and i<271:
            z=z**2+sin(constante**3)
            z=z.conjugate()
            i+=1
            dis=z.imag**2+z.real**2
    return i

def sinu(z,constante,pressision,puissance):
    i=0
    if constante==0:return 271
    rep=1
    dis=constante.imag**2+constante.real**2
    while dis<200 and rep<=pressision:
        i=0
        rep+=1
        while dis<200 and i<271:
            z=sinh(z)+(1/(constante**puissance))
            i+=1
            dis=z.imag**2+z.real**2
    return i
#-------------------------------------------------------------------------------
#associer un nombre a une longeur d'onde pour créé un degrader
def coul(longeur_Onde):
    if longeur_Onde < 0:
        longeur_Onde = 0
    elif longeur_Onde > 271:
        longeur_Onde = 271
    
    white_value = int(longeur_Onde / 271 * 255)
    couleur = (white_value, white_value, white_value)
    return couleur

"""
def coul(longeur_Onde):
    couleur =()
    if longeur_Onde<60:couleur=(int((-longeur_Onde+60)/(60-0)*255),0,255)
    elif longeur_Onde<110:couleur=(0,int((longeur_Onde-60)/(110-60)*255),255)
    elif longeur_Onde<130:couleur=(0,255,int(-(longeur_Onde-130)/(130-110)*255))
    elif longeur_Onde<200:couleur=(int((longeur_Onde-130)/(200-130)*255),255,0)
    elif longeur_Onde<265:couleur=(255,int(-(longeur_Onde-265)/(265-200)*255),0)
    elif longeur_Onde<=270:couleur=(255,0,0)
    else:couleur=(0,0,0)
    return couleur
"""
#-------------------------------------------------------------------------------
#coordonner d'un pixel dans un plan de X sur Y longeur

def co_point(co,taille,debutx,finx,debuty,finy):
    r=debutx+((finx-debutx)/taille[0])*co[0]
    i=debuty+((finy-debuty)/taille[1])*co[1]
    return complex(r,i)

#-------------------------------------------------------------------------------
#Julia
#constante c toujours la meme

def creation_julia(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2,pressision=500,constante=complex(uniform(-1,1),uniform(-1,1))):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),(coul(quadratique(co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),constante,pressision))))
    return font_plan.save("julia_{}.jpg".format(constante))

#-------------------------------------------------------------------------------
#Mandelbrot
#constante c égale au point actuel

def creation_mandelbrot_carré(taille,debut_x=-2,debut_y=-1.5,fin_x=1,fin_y=1.5,pressision=500,nom="mandelbrot"):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(quadratique(complex(0,0),co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),pressision)))
    nom+=".jpg"
    font_plan.save(nom)

def creation_ensemble_cos(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2,pressision=500):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(cosin(co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),pressision)))
    return font_plan.save("ensemble cos.jpg")

def creation_ensemble_puissance(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2,pressision=500):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(puissance(complex(0,0),co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),pressision)))
    return font_plan.save("ensemble puissance .jpg")

def creation_ensemble_conjug(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2,pressision=500):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(conjug(complex(0,0),co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),pressision)))
    return font_plan.save("ensemble conjuge .jpg")

def creation_ensemble_sinu(taille,debut_x=-2,debut_y=-2,fin_x=2,fin_y=2,pressision=500,puissance=2):
    font_plan=Image.new("RGB",taille)
    pressision=ceil(pressision/271)
    for k in range (taille[0]):
        for j in range (taille[1]):
            font_plan.putpixel((k,j),coul(sinu(complex(1,0.1),co_point([k,j],taille,debut_x,fin_x,debut_y,fin_y),pressision,puissance)))
    return font_plan.save("ensemble sinush .jpg")
#-------------------------------------------------------------------------------
#chemin auto évitant
def chemin(calc,taille,point,pas,coul):
    point_actuel=point[-1]
    possibiliter=[(point_actuel[0]-pas,point_actuel[1]),\
    (point_actuel[0],point_actuel[1]-pas),\
    (point_actuel[0]+pas,point_actuel[1]),\
    (point_actuel[0],point_actuel[1]+pas)]

    for i in range (0,4):
        if possibiliter[i][0]<0 or possibiliter[i][0]>taille[0] or possibiliter[i][1]<0 or possibiliter[i][1]>taille[1]:
            possibiliter[i]=0
        elif possibiliter[i] in point:
            possibiliter[i]=0
    while 0 in possibiliter:
        del possibiliter[possibiliter.index(0)]

    if len(possibiliter)==0: return calc.line(point,coul,2)
    alea=randint(0,len(possibiliter)-1)
    point.append((possibiliter[alea]))
    chemin(calc,taille,point,pas,coul)

def creation_chemin(taille,font=(0,0,0),coul=(randint(10,256),randint(10,256),randint(10,256)),pas=10):
    a=time.time()
    chemin_auto=Image.new("RGB",taille,font)
    dessin=ImageDraw.Draw(chemin_auto)
    depart=[(taille[0]//2,taille[1]//2)]
    chemin(dessin,taille,depart,pas,coul)
    chemin_auto.save("chemin auto evitant.jpg")
    b=time.time()
    toto=b-a
    print(toto)
#-------------------------------------------------------------------------------
#noise map

def map_noise(taille,echelle,couche,impacte,lacunariter,graine):
    world = np.zeros(taille)
    x_idx,y_idx = np.linspace(0, 1, taille[0]),np.linspace(0, 1, taille[1])
    monde_x, monde_y = np.meshgrid(x_idx, y_idx)
    world = np.vectorize(pnoise2)(monde_x*echelle,monde_y*echelle,octaves=couche,\
    persistence=impacte,lacunarity=lacunariter,repeatx=taille[0],repeaty=taille[1],base=graine)
    return np.floor((world+0.5) * 255).astype(np.uint8)

def coul_terrain(nb,matrice):
    if nb<matrice[0]:
        return (0,0,128)
    if nb<matrice[1]:
        return (0,148,149)
    if nb<matrice[2]:
        return (255,255,26)
    if nb<matrice[3]:
        return (0,128,0)
    if nb<matrice[4]:
        return (45,43,34)
    return (255,255,255)


def creation_map(taille,sortie="Couleur",couche=4,impacte=0.5,lacunariter=2,matrice=(60,120,140,170,210),graine=randint(0,100),echelle=2):
    a=time.time()
    map_neb=Image.fromarray(map_noise(taille,echelle,couche,impacte,lacunariter,graine),mode="L")
    if sortie=="Couleur":
        data=[]
        for i in range (taille[0]):
            for j in range(taille[1]):
                data.append(coul_terrain(map_neb.getpixel((i,j)),matrice))
        map_coul=Image.new("RGB",taille)
        map_coul.putdata(data)
        map_coul.save("carte aleatoire.jpg")
    else:map_neb.save("noise.jpg")
    b=time.time()
    toto=b-a
    print(toto)

##creation_julia((2500,2500),constante=complex(0,1))
##creation_chemin((250,250),(27,33,44))
#-------------------------------------------------------------------------------
#graphe nombre complexe


#racine(z)=y
#y=a+ib
#y²=(a²-b²)+ i*2ab
#y²=z
#z=c+id
#c+id=(a²-b²)+ i*2ab
#module(z)=racine(c²+d²)
#c=a²-b²
#d=2ab
#module(z)=a²+b²

#a=racine((module(z)+c)/2)
#b=racine((module(z)-c)/2)
#si d est negatif alors Y=a-ib



def pi():
    pi_val=0
    for i in range (1000000):
        j=i
        pi_val=pi_val+(4*((-1)**j))/(2*j+1)
    return pi_val

def ln (x):
    if type(x)==int and x<=0:raise ValueError
    fract=(1-x)/(x + 1)
    nb_base=1
    somme=0
    for i in range(10000):
        somme=somme+(1/nb_base)*(fract**nb_base)
        nb_base+=2
    if somme==0:return somme
    return -2*somme

def racine(x):
    y=1
    for i in range(50):
        y=0.5*(y+(x/y))
    return y

##def co_inverse(comp,taille,co):
##    x,y=co
##    point_x,point_y=comp.real,comp.imag
##    if point_x>=0:
##        point_x=point_x+x/2
##    else:
##        point_x=-1*point_x
##    if point_y>=0:
##        point_x=point_y+x/2
##    else:
##        point_x=-1*point_y
##    coefx,coefy=point_x/x,point_y/y
##    return (taille[0]*coefx,taille[1]*coefy)
##
##def fonction_quadratique(calc,c,comp,type_tracer,repetition,distance_max,taille,co_xy,couleur):
##    point=[]
##    nb_rep=0
##    distance=racine(comp.imag**2+comp.real**2)
##    while nb_rep!=repetition and distance<distance_max:
##        nb_rep+=1
##        point.append(co_inverse(comp,taille,co_xy))
##        comp=comp**2+c
##        distance=racine(comp.imag**2+comp.real**2)
##    if type_tracer=="Point":
##        calc.point(point,couleur)
##    elif type_tracer=="Ligne":
##        calc.line(point,couleur)
##    else:
##        raise ValueError
##
##
##def fonction_nieme(calc,c,comp,type_tracer,repetition,distance_max,taille,co_xy,couleur,n):
##    point=[]
##    nb_rep=0
##    distance=racine(comp.imag**2+comp.real**2)
##    while nb_rep!=repetition and distance<distance_max:
##        nb_rep+=1
##        point.append(co_inverse(comp,taille,co_xy))
##        comp=comp**n+c
##        distance=racine(comp.imag**2+comp.real**2)
##    if type_tracer=="Point":
##        calc.point(point,couleur)
##    elif type_tracer=="Ligne":
##        calc.line(point,couleur)
##    else:
##        raise ValueError
##
##def fonction_lorentzienne(calc,pi,pic,largeur,comp,type_tracer,repetition,distance_max,taille,co_xy,couleur):
##    point=[]
##    nb_rep=0
##    distance=racine(comp.imag**2+comp.real**2)
##    while nb_rep!=repetition and distance<distance_max*5:
##        nb_rep+=1
##        point.append(co_inverse(comp,taille,co_xy))
##        comp=(2/pi*largeur)/(1+(comp-pic/largeur/2))
##        distance=racine(comp.imag**2+comp.real**2)
##
##    if type_tracer=="Point":
##        calc.point(point,couleur)
##    elif type_tracer=="Ligne":
##        calc.line(point,couleur)
##    else:
##        raise ValueError
##
##def fonction_rationnelle(calc,fonction,pi,pic,n,c,largeur,comp,type_tracer,repetition,distance_max,taille,co_xy,couleur):
##    point=[]
##    nb_rep=0
##    distance=racine(comp.imag**2+comp.real**2)
##
##    while nb_rep!=repetition and distance<distance_max*5:
##        nb_rep+=1
##        point.append(co_point_inverse(comp,taille,co_xy))
##
##        distance=racine(comp.imag**2+comp.real**2)
##
##    if type_tracer=="Point":
##        calc.point(point,couleur)
##    elif type_tracer=="Ligne":
##        calc.line(point,couleur)
##    else:
##        raise ValueError
##
##def graphe_complexe(taille,type_fonction="quadratique",type_tracer="Ligne",repetition=500,co_max_min=(30,30)\
##,couleur=(255,255,255),fond=(0,0,0),pic=0,n=1,c=complex(0,0),largeur=1,comp=None,dessin_axe=False,distance_max=50):
##    if comp==None:
##        comp=complex(uniform(-1*co_max_min[0]/2,co_max_min[0]/2),uniform(-1*co_max_min[1]/2,co_max_min[1]/2))
##    graph=Image.new("RGB", taille,fond)
##    dessin=ImageDraw.Draw(graph)
##    if type_fonction=="quadratique":fonction_quadratique(dessin,c,comp,type_tracer,repetition,distance_max,taille,co_max_min,couleur)
##    elif type_fonction=="nieme":fonction_nieme(dessin,c,comp,type_tracer,repetition,distance_max,taille,co_max_min,couleur,n)
##    elif type_fonction=="lorentzienne":fonction_lorentzienne(dessin,pi(),pic,largeur,comp,type_tracer,repetition,distance_max,taille,co_max_min,couleur)
##    graph.save("graph {} du point {}.jpg".format(type_fonction,comp))



pi_val=3.1415926535897932384626433832795028841971
#creation_mandelbrot_carré([1000,1000],pressision=250)
creation_julia((16000,16000),-1.2,-1.2,1.2,1.2,2  ,complex(0.285 ,0.01))
print('ok')
#creation_mandelbrot_carré((3000,3000),pressision=1200,nom="Mandfond2")
print(78)