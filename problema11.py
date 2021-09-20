n=int(input('Dati numarul de elemente din vector='))
a=[]
if n<10:
   print('Introduceti ',n,' elemente pentru vectorul creat:')
   for i in range(0,n):
       n1=int(input('Dati elementul='))
       a.extend([n1])
print(a)
a1=a.copy()
print('b) Afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator=', a1[::-1])
print('c) Sorteaza componentele tabloului in ordine descrescatoare=')
a1.sort(reverse=True)
print(a1)
print('d) Afiseaza pe ecran doar componentele pare=')
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        d.append(a[i]) 
print(d) 
print('e) Afiseaza pe ecran media aritmetica a componentelor pare=')
e=sum(d)/len(d)
print(e)
print('f) Afiseaza pe ecran doar componentele impare=',)
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        f.append(a[i])
print(f)
x=int(input('x='))
y=int(input('y='))
print('g) Afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y (valorile x si y se citesc de la tastatura) este=')
g=[]
for i in range(0,len(a)):
    if (a[i]>x) and (a[i]%y!=0):
        g.append(a[i])
print(g)
print('h) Afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y (valorile x si y se citesc de la tastatura) este=')
h=[]
for i in range(0,len(a)):
    if(a[i>x]) and (a[i]<y):
        h.append(a[i])
print(h)
print('i) Afiseaza pe ecran pozitiile componentelor impare negative=')
impare_negative=[]
for i in range(0,len(a)):
    if(a[i]%2!=0) and (a[i]<0):
        impare_negative.append(i)
print(impare_negative)
print('j) Afiseaza pe ecran pozitiile componentelor ce contin doar doua cifre semnificative=')
j=[]
for i in range(0,len(a)):
    if (a[i]/10>=1) and (a[i]/10<10):
        q=a[i]
        j.extend([q])
    print(j)
print('k) Inlocuieste prima componenta a tabloului cu componenta de valoare minima din tabloul respectiv=')
r=a[:]
r[0]=min(r)
print(r)
print('l) Inlocuieste componenta de valoare minima din tabloul respectiv cu prima componenta a acestuia=')
r1=a[:]
r1[r1.index(min(r1))]=r1[0]
print(r1)


