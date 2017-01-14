fruits=['apple','banana','mango','watermelon','pineapple']
numbers=[1,2,3,4,5,6,7,8,9,10]
mix=[1,'ram',2,'seeta',3,'lakshman']

for f in fruits:
    print"%s"%f
for n in numbers:
    print"%d"%n
for m in mix:
    print"%r"%m
print fruits[0]
new=[]
for i in range(0,len(fruits)):
    new.append(fruits[i])
    print new[i]
