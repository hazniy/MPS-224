Part 1
- boop to kebab : improve check 2 elements in tuple, and ensure x and y positive. 
- kebab to boop : learn how to use reversed() function ; https://www.w3schools.com/python/ref_func_reversed.asp
- kebab to pronk : 
  - improvise my initial code checking only "E" and "W" in the string :
  str1 = "WEED"
  for i in range (len(str1)):
      if str1[i] == "E" or str1[i] == "W":
          i = i + 1
      else:
          print("Invalid character found: " + str1[i])
  with : 
  if any(c not in "EW" for c in S):
      raise ValueError("S must contain only 'E' and 'W'")
  - learn how to use startswith() method, which return boolean value ; https://www.w3schools.com/python/ref_string_startswith.asp

Part 2
There's actually a better way to do this, AI skip pronk and suggested helper function translating kebabs to number, but I want to stick with my logic.

Part 3
- frond : learn how to use itertools.product() ; https://www.geeksforgeeks.org/python/python-itertools-product/
- print spork : refer to 1st year python notes about pascal's triangle for adjusting the gap and center the triangle like shape. 

Part 4 
- number to pronk : learn to use limit_denominator()
- hoopy frood : learn how to use enumerate()
- 
