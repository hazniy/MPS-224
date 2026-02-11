#only list and sets are mutable 
l = [11,22,33,44]
l #[11, 22, 33, 44]
l[-1] = 4444 #[11, 22, 33, 4444]
l.append(-9) #[11, 22, 33, 4444, -9]

s = {5,6,7,8,9}
s #{5,6,7,8,9}
s.add(10) {5, 6, 7, 8, 9, 10}

x = "abcdef"
print(x) #abcdef
print(x[2]) #c
print(x.upper()) #ABCDEF

id(x) #unique id for the specified object 

#Tuple & string not mutable 
t = (11, 22, 33, 44)
u = "The cat sat on the mat"
