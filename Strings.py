question = 'What is the air-speed velocity of an unladen swallow?'
fox = 'The quick brown fox jumps over the lazy dog'

len(question) #43
len(fox) #43

print(f"{question[10]=}")
print(f"{question[5:7]=}")
print(f"{question[-8:]=}")
print(f"{question[::10]=}")
print(f"{question[::-1]=}")
#question[10]='e'
#question[5:7]='is'
#question[-8:]='swallow?'
#question[::10]='Wed ao'
#question[::-1]='?wollaws nedalnu na fo yticolev deeps-ria eht si tahW'

print([i for i in range(len(question)) if question[i] == ' ']) # Positions of spaces 
#OR
print([i for i,c in enumerate(question) if c == ' ']) # Positions of spaces
#[4, 7, 11, 21, 30, 33, 36, 44]

print('city' in question)          # 'city' appears as part of the word 'velocity'
print('velociraptor' in question)  # the word 'velociraptor' is not in the question
#True
#False

cities_string = 'Sheffield,New York,  Paris, Hong Kong, Chicago,Los Angeles, Tokyo'
cities = [city.strip() for city in cities_string.split(',')] # Split on commas
print(cities)
print(str.join(' and ', cities)) # Join with ' and '
print(' and '.join(cities)) # Same thing
#['Sheffield', 'New York', 'Paris', 'Hong Kong', 'Chicago', 'Los Angeles', 'Tokyo']
#Sheffield and New York and Paris and Hong Kong and Chicago and Los Angeles and Tokyo
#Sheffield and New York and Paris and Hong Kong and Chicago and Los Angeles and Tokyo

request = 'Please can I have a cookie'
print(f'Original:         {request}')
print(f'Lower case:       {request.lower()}')
print(f'Upper case:       {request.upper()}')
print(f'Capitalize words: {request.title()}')
print(f'Improved:         {request.replace("cookie","chocolate cake")}')
print(f'Original:         {request}') # The original string is unchanged
#Original:         Please can I have a cookie
#Lower case:       please can i have a cookie
#Upper case:       PLEASE CAN I HAVE A COOKIE
#Capitalize words: Please Can I Have A Cookie
#Improved:         Please can I have a chocolate cake
#Original:         Please can I have a cookie
