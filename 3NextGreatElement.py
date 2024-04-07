def nge(list,n):
    for i in range (0,n):
        ele=list[i]
        next=-1
        for j in range (i,n):
            if list[j]>list[i]:
                next=list[j]
                break
        print(ele,"-->",next)
data=[7,5,1,9,10,12,8]
nge(data,len(data))