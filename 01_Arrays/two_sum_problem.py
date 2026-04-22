a=[1,2,3,4,5,6,7,8,9,10]
pair=[]
seen=set()
target=10
for i in a:
    complement = target - i
    if complement in seen:
        pair.append((i, complement))
    seen.add(i)
print(pair)