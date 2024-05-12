tedad = int(input())
flist = []
mlist = []

for i in range(0,tedad):
    vorodi  = str(input())
    vorodi = vorodi.split('.')
    vorodi[1] = vorodi[1].lower().capitalize()
    if vorodi[0] == 'f':
        flist.append(vorodi)
    elif vorodi[0] == 'm':
        mlist.append(vorodi)
sorted_flist = sorted(flist, key=lambda x: x[1])
sorted_mlist = sorted(mlist, key=lambda y: y[1])
for item in sorted_flist:
    print(' '.join(item))
for item in sorted_mlist:
    print(' '.join(item))