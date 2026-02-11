#docs.python.org/3/library/string.html#formatspec
ans = 32
print(f"the answer to life the universe and everything is {ans}")
print(f"the answer to life the universe and everything is {ans:010d}") #print in 10 digit form, pad number to length 10 
print(f"the answer to life the universe and everything is {ans:.2e}") #e notation, 2 dp 

l = [5, 6, 7, 8]
print('the list ' + repr(l) + ' contains ' + repr(len(l)) + ' elements') #repr : string representation #or
print('the list ' + str(l) + ' contains ' + str(len(l)) + ' elements') #or
print(f'the list {l} contains {len(l)} elements')

chr(65) #A 
ord('A') #65
[chr(65+i) for i in range(26)] #list all alphabets 
