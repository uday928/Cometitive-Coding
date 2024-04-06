a=[2,7,3,5,4,6,8]
n=int(len(a))
def NGE(a,n):
  for i in range(0,n):
    next=-1
    for j in range(i,n):
      if(a[j]>a[i]):
        next=a[j]
        break
    print(a[i],"-->",next)
NGE(a,n)