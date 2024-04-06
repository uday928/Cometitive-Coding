# 4 condition '(' , ')' , Operators, alphabates
output=[]
op=[]
priority={
  '(':0,
  '+':1,
  '-':1,
  '*':2,
  '/':2,
  '^':3
}
exp=input()
for ch in exp:
  if ch=='(':
    op.append(ch)
  elif ch==')':
    while(op[-1]!='('):
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
print("Infix expression:")
print("postfix operation:", end=" ")
for i in output:
  print(i,end="")