# show the frequency of the word as dictionary given below as string
s = "apple banana apple orange banana apple kiwi kiwi beetroot carrot beetroot carrot carrot"
l = s.split()#converted them into list
d = {}

print(l)

temp=[]

for i in l: 
    if i not in temp:
        d.update({i:l.count(i)})
        temp.append(i)
del temp
print(d)