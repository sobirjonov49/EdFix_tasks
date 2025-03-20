matn=input('Matn kirit:')
matn=matn.replace(" ", "").lower()
harf_soni={}

for i in matn:
    if i in harf_soni:
        harf_soni[i]+=1
    else:
        harf_soni[i]=1
print(harf_soni)