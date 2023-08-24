import time
from PIL import Image, ImageDraw
from random import randint
from math import cos , sin , radians
from cmath import sqrt
#-------------------------------------------------------------------------------
# Triangle

def millieu (a,b):
    return ((a[0]+b[0])//2,(a[1]+b[1])//2)

def creation_triangle (rep,co,calc,couleur):
    if rep==0:
        if type(couleur)==str and couleur=="aléatoire":
            calc.polygon([co[0],co[1],co[2]],(randint(0,256),randint(0,256),randint(0,256)))
        elif type(couleur)==tuple and len(couleur)==3 :
            calc.polygon([co[0],co[1],co[2]],couleur)
        else:
            raise ValueError("la couleur es soit mal orthographié (aléatoire) ou le tuple est incorrecte")

    else:
        new_co1,new_co2,new_co3=\
        (co[0],millieu(co[0],co[1]),(millieu(co[0],co[2]))),\
        (millieu(co[0],co[1]),co[1],(millieu(co[1],co[2]))),\
        (millieu(co[0],co[2]),millieu(co[1],co[2]),co[2])
##        bas gauche,(bah gauche,bah droite,haut)
##        bas droite,(bah gauche,bah droite,haut)
##        haut,(bah gauche,bah droite,haut)
        creation_triangle(rep-1,new_co1,calc,couleur),creation_triangle(rep-1,new_co2,calc,couleur),creation_triangle(rep-1,new_co3,calc,couleur)

def Sierpiński(taille,repetition,fond=(0,0,0),coul=(255,255,255)):
    a=time.time()
    sierp=Image.new("RGB",taille,fond)
    triangle_dessin=ImageDraw.Draw(sierp)
    Point_tri=((0,taille[1]-1),(taille[0]-1,taille[1]-1),(taille[0]//2,0))
    creation_triangle(repetition,Point_tri,triangle_dessin,coul)
    sierp.save("triangle_{}_{}.jpg".format(taille,repetition))
    b=time.time()
    print(b-a)

#-------------------------------------------------------------------------------
#Cantor
#asymétrique
def cantor_tracer(calc,ab,h,coul):
    distance=ab[1]-ab[0]
    if distance<=1: return
    calc.rectangle((ab[0],h,ab[1],h+5),coul)
    cantor(calc,(ab[0],ab[0]+distance/3),h+15,coul)
    cantor(calc,(ab[0]+distance*2/3,ab[1]),h+15,coul)

def cantor(taille,font=(0,0,0),coul=(255,255,255),asymétrique=False):
    a=time.time()
    cant=Image.new("RGB",taille,font)
    trai=ImageDraw.Draw(cant)
    if asymétrique == False:
        cantor_tracer(trai,(0,taille[1]-1),0,coul)
    elif asymétrique == True:
        i=1
        ##cantor_tracer_asymétrique(trai,(0,taille[1]-1),0,coul)
    else:
        raise ValueError("asymétrique est un bool")
    cant.save("ensemble_de_cantor.jpg")
    b=time.time()
    print(b-a)

#-------------------------------------------------------------------------------
# Courbe du dragon

def courbe_dra(calc,AB,sense,rep):
    if rep==0:
        return calc.line(AB,(255,255,255),2)
    image_de_b=(AB[0][0] + sense * (AB[0][1] - AB[1][1]), AB[0][1] + sense * (- AB[0][0]  +AB[1][0]))
    mid=((AB[1][0]+image_de_b[0])/2,(AB[1][1]+image_de_b[1])/2)
    return courbe_dra(calc,[AB[0],mid],1,rep-1),courbe_dra(calc,[mid,AB[1]],-1,rep-1)

def courbe_du_dragon(taille,rep,fond=(0,0,0),coul=(255,255,255),sense=-1):
    a=time.time()
    img=Image.new("RGB",taille, (27,33,44))
    calc=ImageDraw.Draw(img)
    courbe_dra(calc,[(taille[0]/4,taille[1]/2),(taille[0]*0.75,taille[1]/2)],sense,rep)
    img.save("courbe_du_dragon_{}.jpg".format(rep))
    b=time.time()
    print(b-a)

def tapis_drag(nb,lh,taille=[10,10]):
    drag=Image.new("RGB",lh,(0,0,0))
    cal=ImageDraw.Draw(drag)
    longeur,hauteur=lh[0]/taille[0],lh[1]/taille[1]
    for i in range(taille[0]):
        for j in range (taille[1]+1):
            for puis in range (2):
                courbe_du_dragon(cal,[(longeur*i,hauteur*j),(longeur*(i+1),hauteur*j)],(-1)**puis,nb,(randint(0,255),randint(0,255),randint(0,255),75))
    drag.save("tapis.jpg")
#-------------------------------------------------------------------------------
#Arbre

def branche(calc,ab,rep,rad_angled,rad_angleg,coul,rapport):
    if rep==0:return
    calc.line(ab,coul,2)
    vecteur_ab=((ab[1][0]-ab[0][0])*rapport,(ab[1][1]-ab[0][1])*rapport)
    bp=(ab[1][0]+vecteur_ab[0],ab[1][1]+vecteur_ab[1])
    cd,sd,cg,sg=cos(rad_angled),sin(rad_angled),cos(rad_angleg),sin(rad_angleg)
    xd,yd,xg,yg=ab[1][0]+(bp[0]-ab[1][0])*cd-(bp[1]-ab[1][1])*sd,\
                ab[1][1]+(bp[1]-ab[1][1])*cd+(bp[0]-ab[1][0])*sd,\
                ab[1][0]+(bp[0]-ab[1][0])*cg-(bp[1]-ab[1][1])*sg,\
                ab[1][1]+(bp[1]-ab[1][1])*cg+(bp[0]-ab[1][0])*sg
    bd=(ab[1],(xd,yd))
    bg=(ab[1],(xg,yg))


    branche(calc,bd,rep-1,rad_angled,rad_angleg,coul,rapport)
    branche(calc,bg,rep-1,rad_angled,rad_angleg,coul,rapport)


def creation_arbre(taille,rep,angle=30,rapport=0.7,coul=(randint(10,256),randint(10,256),randint(10,256)),font=(0,0,0)):
    a=time.time()
    arbre=Image.new("RGB",taille,font)
    dessin=ImageDraw.Draw(arbre)
    ab=((taille[0]/2,taille[1]*0.9),(taille[0]/2,taille[1]*0.65))
    rad_angled,rad_angleg=radians(angle),radians(360-angle)
    branche(dessin,ab,rep,rad_angled,rad_angleg,coul,rapport)
    arbre.save('arbre fractal de {} iteration.jpg'.format(rep))
    b=time.time()
    print( b-a)

#-------------------------------------------------------------------------------
#arbre mandelbrot
def creation_arbre_mand(taille,rep,coul=(randint(10,256),randint(10,256),randint(10,256)),font=(0,0,0)):
    a=time.time()
    arbre_mand=Image.new("RGB",taille,font)
    dessin=ImageDraw.Draw(arbre_mand)
    ab=((taille[0]/2,taille[1]*0.9),(taille[0]/2,taille[1]*0.55))
    rad_angled,rad_angleg=radians(90),radians(270)
    branche(dessin,ab,rep,rad_angled,rad_angleg,coul,0.7)
    arbre_mand.save('arbre fractal de mandelbrot de {} iteration.jpg'.format(rep))
    b=time.time()
    print(b-a)

#-------------------------------------------------------------------------------
#Courbe koch

def courbe_ko(calc,ab,rep,coul):
    if rep==0:return calc.line(ab,coul,2)

    vecteur_3ab=((ab[1][0]-ab[0][0])*1/3,(ab[1][1]-ab[0][1])*1/3)
    c,f=(ab[0][0]+vecteur_3ab[0],ab[0][1]+vecteur_3ab[1]),\
        (ab[0][0]+2*vecteur_3ab[0],ab[0][1]+2*vecteur_3ab[1])
    d,e=(c[0] +(c[1] - ab[0][1]), c[1] +(- c[0]  +ab[0][0])),\
        (f[0] -(f[1] - ab[1][1]), f[1] -(- f[0]  +ab[1][0]))
    ac,cd,de,ef,fb=(ab[0],c),\
                    (c,d),\
                    (d,e),\
                    (e,f),\
                    (f,ab[1])
    courbe_ko(calc,ac,rep-1,coul)
    courbe_ko(calc,cd,rep-1,coul)
    courbe_ko(calc,de,rep-1,coul)
    courbe_ko(calc,ef,rep-1,coul)
    courbe_ko(calc,fb,rep-1,coul)
def creation_courbe_koch(taille,rep,coul=(randint(10,256),randint(10,256),randint(10,256)),font=(0,0,0)):
    ta=time.time()
    courbe_koch=Image.new("RGB",taille,font)
    dessin_courbe=ImageDraw.Draw(courbe_koch)
    a,b=(taille[0]*0.1,taille[1]*0.9),\
        (taille[0]*0.9,taille[1]*0.9)
    courbe_ko(dessin_courbe,(a,b),rep,coul)
    courbe_koch.save("courbe de koch {} iteration.jpg".format(rep))
    tb=time.time()
    print(tb-ta)


#-------------------------------------------------------------------------------
#fontion mathematique
def racine(x):
    y=1
    for i in range(50):
        y=0.5*(y+(x/y))
    return y

def pi():
    pi_val=0
    for i in range (10000000):
        j=i
        pi_val=pi_val+(4*((-1)**j))/(2*j+1)
    return pi_val

def ln (x):
        fract=(1-x)/(x + 1)
        nb_base=1
        somme=0
        for i in range(10000):
            somme=somme+(1/nb_base)*(fract**nb_base)
            nb_base+=2
        return -2*somme

#-------------------------------------------------------------------------------
#tapis de Sierpiński
def carré(calc,abcd,rep,coul):
    ab=(abcd[1][0]-abcd[0][0])/3
    if ab<1 or rep==0:return calc.rectangle((abcd[0],abcd[2]),coul)
    e,f=(abcd[0][0]+ab,abcd[0][1]),(abcd[0][0]+2*ab,abcd[0][1])
    l,k=(abcd[0][0],abcd[0][1]+ab),(abcd[0][0],abcd[0][1]+2*ab)
    g,h=(abcd[1][0],abcd[1][1]+ab),(abcd[1][0],abcd[1][1]+ab*2)
    j,i=(abcd[3][0]+ab,abcd[3][1]),(abcd[3][0]+2*ab,abcd[3][1])
    m,n,o,p=(e[0],l[1]),(f[0],l[1]),(f[0],k[1]),(e[0],k[1])
    aeml,efnm,fbgn,ngho,ohci,poij,kpjd,lmpk=(abcd[0],e,m,l),(e,f,n,m),(f,abcd[1],g,n),(n,g,h,o),(o,h,abcd[2],i),(p,o,i,j),(k,p,j,abcd[3]),(l,m,p,k)
    carres=[aeml,efnm,fbgn,ngho,ohci,poij,kpjd,lmpk]
    for x in range(8):
        carré(calc,carres[x],rep-1,coul)

def creation_tapi(rep=int,taille=1000,font=(0,0,0),coul=(255,255,255)):
    ima=Image.new("RGB",(taille,taille),font)
    calc=ImageDraw.Draw(ima)
    a,b,c,d=(20,20),(taille-20,20),(taille-20,taille-20),(20,taille-20)
    carré(calc,(a,b,c,d),rep,coul)
    ima.save("tapis de sierp{}.jpg".format(rep))

##def fibinv (n,a,b):
##    return a if(n == 1)else fibinv(n-1, a+b, a)
##def fibo(n):
##    return 0 if(n <= 0) else fibinv(n, 1, 0)
##
##def tracer_fibo(calc,mot_fibo,coul,points,indice,taille,pas):
##    if indice+1>len(mot_fibo):return
##    elif mot_fibo[indice]==0:
##        if indice%2==0:sense=1
##        else:sense=-1
##        nb_point=(points[1][0] + sense * (points[1][1] - points[0][1]), points[1][1] + sense * (- points[1][0]  +points[0][0]))
##    elif mot_fibo[indice]==1:
##        if points[0][0]==points[1][0]:
##            if points[0][1]<points[1][1]:
##                nb_point=(points[1][0],points[1][1]+pas)
##            elif points[0][1]>points[1][1]:
##                nb_point=(points[1][0],points[1][1]-pas)
##        elif points[0][1]==points[1][1]:
##            if points[0][0]<points[1][0]:
##                nb_point=(points[1][0]+pas,points[1][1])
##            elif points[0][0]>points[1][0]:
##                nb_point=(points[1][0]-pas,points[1][1])
##        else :
##            raise ValueError("probleme d'axes")
##    else: raise ValueError("probleme binaire")
##    if nb_point[0]<0 or nb_point[1]<0 or nb_point[0]>taille or nb_point[1]>taille:
##        return
##    points=((points[1],nb_point))
##    calc.line(points,coul)
##    tracer_fibo(calc,mot_fibo,coul,points,indice+1,taille,pas)
##
##
##
##
##
##def creation_Fibonacci(taille,rep,coul=(randint(10,256),randint(10,256),randint(10,256)),font=(0,0,0),pas=0):
##    a=time.time()
##    if type(rep)!=int or rep <= 0 : raise ValueError("{} est incorrecte".format(rep))
##    if pas ==0: pas=taille//150
##    mot=''
##    motfini=''
##    for i in range (rep+1):
##        mot+=str(fibo(i))
##    for j in mot:
##        if j == '0':
##            motfini+='01'
##        elif j == '1':
##            motfini+='2'
##        elif j == '2':
##            motfini+='23'
##        elif j == '3':
##            motfini+='4'
##        else: motfini+=j
##    mot_fibo=[]
##    for i in range(len(motfini)):
##        mot_fibo.append(int(motfini[i])%2)
##
##    image=Image.new("RGB",(taille,taille),font)
##    calc=ImageDraw.Draw(image)
##    points= [(int(taille//4),int(taille*0.7)),\
##            (int(taille//4+pas),int(taille*0.7))]
##    calc.line(points,coul)
##
##    tracer_fibo(calc,mot_fibo,coul,points,1,taille,pas)
##    image.save("fractal de Fibonacci {}.jpg".format(rep))
##    tb=time.time()
##    print(tb-a)
##int(int(7))
##creation_Fibonacci(1000,50)

#creation_tapi(15,10000)
#Sierpiński((1000,1000),5,(100,100,100),(200,200,200))
