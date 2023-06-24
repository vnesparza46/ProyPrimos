try:
    n = input('Ingresa un numero: ')
    n = int(n)
except:
    n=1
totaldivisores=0
totaldivisores=int(totaldivisores)
contador=n
contador=int(contador)
while contador>0:
    if n%contador==0:
        totaldivisores+=1
    contador-=1
if totaldivisores==2 or totaldivisores==1:
    print('SI')
else:
    print('NO')
