genres = {"Horror": 0 , "Romance" : 0 , "Comedy" : 0 , "History" : 0 , "Adventure" : 0 , "Action" : 0}
namefavelist = []
pnumbers = int(input())
for i in range(0,pnumbers):
    pnamefave = str(input())
    namefavelist.append(pnamefave)
for j in range(0,len(namefavelist)):
    temp = str(namefavelist[j])
    temp = temp.split()
    temp.pop(0)
    for item in temp:
        genres[item] += 1

sorted_genres = sorted(genres.items(), key=lambda x: (-x[1], x[0]))

for genre, count in sorted_genres:
    print(f"{genre} : {count}")