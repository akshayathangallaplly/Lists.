'''
list
'''
#a=[]
#print(type(a))
a=[10,20,30,40,"sweety"]
print(a[4])
print(a[0:4:2])#[start:stop:skip]
'''
append
extend
count
insert
pop
remove
index
'''
#append
s=[10,20,30,40,"fruit"]
s.append("python")
print(s)
 
#extend
s=[10,20,30,40,"fruit"]
s.extend([5,36,36,4646])
print(s)

#insert
s=[10,20,30,40,"fruit"]
s.insert(2,70)
print(s)

#count
s=[10,20,10,30,40,"fruit"]
print(s.count(10))

#remove
s=[10,20,30,40,"fruit"]
s.remove(20)
print(s)

#pop
s=[10,20,30,40,"fruit"]
s.pop()
print(s)

#index
s=[10,20,30,40,"fruit"]
print(s.index(40))

#for
for i in [100,200,300,400,500,"sweety"]:
    print(i)