dictlist = dict()
for i in range(0,10):
    numbers = int(input())
    divisior = []
    for j in range(1,numbers+1):
        if (numbers % j) == 0 :
            count = 0
            for k in range(1,j):
                if (j % k) == 0:
                    count += 1
            if count <= 1 and j != 1:
                divisior.append(j)
            elif j == 2:
                divisior.append(j)
        dictlist[numbers] = len(divisior)
sorted_items = sorted(dictlist.items(), key=lambda x: (x[1],x[0]))
sorted_dict = dict(sorted_items)
last_key, last_value = list(sorted_dict.items())[-1]
print(last_key, last_value)