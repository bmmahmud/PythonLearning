lists = []
max= 0
for x in range(4):
    val = int(input())
    lists.append(val)
print(lists)
for num in lists:
    if num > max:
        max = num
max_index = lists.index(max)
print(max)
print(max_index+1)        
