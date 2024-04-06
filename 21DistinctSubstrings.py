def distinct(string):
  substrings=[]
  for i in range(len(string)):
    for j in range(i+1,len(string)+1):
      
      substring=string[i:j]
      
      if substring not in substrings:
        substrings.append(substring)
        
  return substrings
  
input_string=input("enter a string:")
result=distinct(input_string)
print("distinct  substring:",result)
print("total distinct substrings:",len(result))