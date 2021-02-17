import thepileoffunctions

k=int(input())
array = []
array[:k] = thepileoffunctions.create(0,0) * k
s = thepileoffunctions.create(0, 1)
for i in range(0, k):
    array[i] = thepileoffunctions.inp()
    s=thepileoffunctions.add(array[i], s)
print("1/sum = ")
print(thepileoffunctions.prt(thepileoffunctions.div(thepileoffunctions.create(1, 1), s)))
input()