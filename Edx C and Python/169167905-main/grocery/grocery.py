items=[]
try:
    while True:
        item = input().upper()
        items.append(item)
except EOFError:
    pass

items_dict = {}
items_copy=[]
for i in items:
    if not(i in items_copy):
        items_copy.append(i)
    try:
        items_dict[i]+=1
    except:
        items_dict[i]=1
items_copy.sort()
for i in items_copy:
    print(items_dict[i], i)
