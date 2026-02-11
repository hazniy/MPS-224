list(range(1,20))
[i for i in range(1,20)] #same output different writing 
squares = [i ** 2 for i in range(1,20)]
squares

odd_squares = [i ** 2 for i in range(1,20) if i % 2 == 1]
odd_squares
odd_squares1 = [j for j in squares if j % 2 == 1] #other way
odd_squares1 #print vertically 
print(f"List of cubes: {odd_squares1}") #other way to print, horizontally

squares_odd = sorted(list(set(squares) & set(odd_squares)))
squares_odd 
#{1, 9, 25, 49, 81, 121, 169, 225, 289, 361} with only set
#[1, 225, 289, 9, 169, 361, 81, 49, 121, 25] with list 
#[1, 9, 25, 49, 81, 121, 169, 225, 289, 361] with sorted list 

long_name = "Nur Farhazni Najwa binti farhan"
len(long_name) #the length 
[s for s in long_name] #one by one char
[s for s in long_name if s.isupper()] #list upper case letter 
''.join([s for s in long_name if s.isupper()]) #join the upper case char together  
long_name.split(' ') #split the word one by one 
[s[0] for s in long_name.split(' ')] #take the initial of every word only 
