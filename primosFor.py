try:
    n = input('Ingresa un numero: ')
    n = int(n)
except:
    n=1
totaldivisores=0
totaldivisores=int(totaldivisores)
for i in range(n):
    if n%(i+1)==0:
        totaldivisores+=1
if totaldivisores==2 or totaldivisores==1:
    print('SI')
else:
    print('NO')
