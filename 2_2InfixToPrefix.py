# 4 condition '(' , ')' , Operators, alphabates
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str  
output=[]
op=[]
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
    op.append(ch)
  elif ch=='(':
    while(op[-1]!=')'):
      ele=op.pop()
      output.append(ele)
    op.pop()
  elif(ch=="+" or ch=="-" or ch=="/" or ch=="*" or ch=="^"):
    if len(op)>0:
      while priority[op[-1]]>=priority[ch]:
        ele=op.pop()
        output.append(ele)
        if len(op)==0:
          break
    op.append(ch)  
  else:
    output.append(ch)
while len(op)!=0:
  ele=op.pop()
  output.append(ele)
angle=reverse(output)
print("Infix expression:")
print("prefix operation:", end=" ")
for i in angle:
  print(i,end="")