# 4 condition '(' , ')' , Operators, alphabates
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str  
output=[]
stack=[]
priority={
  ')':0,
  '+':1,
  '-':1,
  '*':2,
  '/':2,
  '^':3
}
exp1=input()
exp=reverse(exp1)
for ch in exp:
  if ch==')':
    stack.append(ch)
  elif ch=='(':
    while(stack[-1]!=')'):
      ele=stack.pop()
      output.append(ele)
    stack.pop()
  elif(ch=="+" or ch=="-" or ch=="/" or ch=="*" or ch=="^"):
    if len(stack)>0:
      while priority[stack[-1]]>=priority[ch]:
        ele=stack.pop()
        output.append(ele)
        if len(stack)==0:
          break
    stack.append(ch)  
  else:
    output.append(ch)
while len(stack)!=0:
  ele=stack.pop()
  output.append(ele)
angle=reverse(output)
print("Infix expression:")
print("prefix operation:", end=" ")
for i in angle:
  print(i,end="")