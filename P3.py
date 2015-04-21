# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:20:14 2015
@author: GABRIEL
"""
import matplotlib.pyplot as plt
ss = open("imc.txt",encoding="utf-8",mode="w+")
a = open("usuario.csv",encoding="utf-8")
b= open("alimentos.csv")
c = a.readlines()
d = b.readlines() 


comidas = []
comidasl=[]

ingeridos = []
ingeridosl = []
t = []
user = []
for x in c:
    y = x.strip()
    if c != "":
        t.append(y)
        
for x in d:
    y = x.strip()
    if d != "":
        comidas.append(y)
        
for x in c[3::]:
    y = x.strip()
    if c != "":
        ingeridos.append(y)



for i in range(0,len(ingeridos)):
    x = ingeridos[i].split(',')
    ingeridosl.append(x)
    
for i in range(0,len(t)):
    x = t[i].split(',')
    user.append(x)
for i in range(2,len(comidas)):
    x = comidas[i].split(',')
    comidasl.append(x)    
          




a1=user[1][4].split(".")
a2=int((a1[0]+a1[1]))



if user[1][3] == "M":

    TMB = 88.36 + (13.4 * int(user[1][2])) + (4.8 * a2)-(5.7 * int(user[1][1]))


if user[1][3] == "F":
    
    TMB = 447.6 + (9.2 * user(int([1][2]))) + (3.1 * a2)-(4.3 * int(user[1][1]))
 

if user[1][5] == 'mínimo':
    tmbf = TMB*1.2
if user[1][5] == 'baixo':
    tmbf = TMB*1.375
if user[1][5] == 'médio':
    tmbf = TMB*1.55
if user[1][5] == 'alto':
    tmbf = TMB*1.725
if user[1][5] == 'muito ativo':
    tmbf = TMB*1.9

datas = {}
dias =[]
cdias = {}
dicteste = {}
data = []
comidasfinal= {}
dico = {}
calingeridas = []
somadia = []

foodq={}
foodcal={}
foodcarb={}
foodpro ={}
foodfat={}

for i in comidasl:
    foodq[i[0]]=i[1]
    foodcal[i[0]]=i[2]
    foodpro[i[0]]=i[3]
    foodcarb[i[0]]=i[4]
    foodfat[i[0]]=i[5]

  
x=0
for i in ingeridosl:
    d = i[0]
    
    if d not in datas:
        datas[d]=x
        x += 1
        dias.append({}) 
        data.append(d)
        
    if d in datas:
        dias[datas[d]][i[1]] = i[2]
        
    if d not in cdias:
        cdias[d] = {}
    cdias[d][i[1]] = i[2]

i=0
dif = []
while i < len(data):
    y = data[i]
    h=int(y[0:2])*1
    l=int(y[3:5])*100
    j=int(y[6:8])*1000
    k = h+l+j
    dicteste[k]=y
    i+=1

dictesteordem = sorted(dicteste.values()) 

for i in dictesteordem:
    u = comidasfinal
    u[i]=cdias[i]
    
i= 0    
while i < len(dictesteordem):
    
    dico[i]= i
    i+= 1
    
i = 0    

carbdia=[]
prodia=[]
fatdia=[]
y=0

for i in dictesteordem:
    
    somadia.append(0)
    carbdia.append(0)
    prodia.append(0)
    fatdia.append(0)
      
  
    o= 0    
        
    for n in comidasfinal[i]:
            
        
        
        p = float(foodq[n])
        q = float(foodcal[n])
        r = float(foodcarb[n])                   
        s = float(foodpro[n])
        t = float(foodfat[n])
        
        o= (float(comidasfinal[i][n])/p)*q
        
        carb = (float(comidasfinal[i][n])/p)*r
        pro = (float(comidasfinal[i][n])/p)*s
        fat = (float(comidasfinal[i][n])/p)*t
        
        somadia[y]+= o 
        carbdia[y]+=carb
        prodia[y]+= pro
        fatdia[y]+=fat
        
    dif.append(0)    
    
    
    dif[y]= o - tmbf
    
    if dif[y] > 0:
        ss.writelines("\nDia %s----> +%s calorias do que deveria."%(i,dif[y]))
        
    else:
        ss.writelines("\nDia %s----> %s calorias do que deveria."%(i,dif[y]))
    y +=1






imc= 1.3*float(user[1][2]) / float(user[1][4])**2
if imc < 18.5:
    print("Pessoa abaixo do peso")
    ss.writelines("\nPessoa abaixo do peso")
if 18.5 <= imc <= 24.9:
    print("Pessoa com peso normal")
    ss.writelines("\nPessoa com peso normal")
if 25 <= imc <= 29.9:
    print("Pessoa acima do peso")
    ss.writelines("\nPessoa acima do peso")
if imc > 30:
    print("Pessoa obesa")
    ss.writelines("\nPessoa obesa")
print("Dados de: %s"%user[1][0])
ss.close()
for i in range(0,len(somadia)):
    
    y=0    
    x = 0
    z=0
    w=0
    r=0
    y = int(somadia[i])
    
    if y > x:
        x = y
        
        
    y = int(carbdia[i])        
    if y > z:
        z = y
    y = int(prodia[i])        
    if y > w:
        w = y
    y = int(fatdia[i])        
    if y > r:
        r = y
        
        
    
    

if x > tmbf:
    
    calx =x +100
else:
    calx = tmbf + 100    
tmbfl = [tmbf]*len(dias)  


tempo = range(0, len(dias))


plt.plot(tempo, somadia)
plt.plot(tempo,tmbfl)
plt.axis([0, len(dias)-1, 0 , calx])
plt.ylabel('Calorias')
plt.xlabel('Dias')
plt.title(r'Calorias Consumidas')
plt.show()
#########################################################
plt.plot(tempo, prodia)
#plt.plot(tempo, pror)
plt.axis([0, len(dias)-1, 0 , w+100])
plt.ylabel('Proteínas [g]')
plt.xlabel('Dias')
plt.title(r'Proteína Consumida')
plt.show()

plt.plot(tempo, carbdia)
#plt.plot(tempo, carr)
plt.axis([0, len(dias)-1, 0 , z+100])
plt.ylabel('Carboidrato [g]')
plt.xlabel('Dias')
plt.title(r'Carboidrato Consumido')
plt.show()

plt.plot(tempo, fatdia)
#plt.plot(tempo, gorr)
plt.axis([0, len(dias)-1, 0 , r+100])
plt.ylabel('Gordura [g]')
plt.xlabel('Dias')
plt.title(r'Gordura Consumida')
plt.show()



     
