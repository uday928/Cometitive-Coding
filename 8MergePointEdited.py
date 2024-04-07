class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
node1=node(10)
node2=node(20)
node3=node(30)
node4=node(50)
node5=node(40)
node6=node(None)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6 

head=node1
l1=[]
while head.next!=None:
    print(head.data,end="-->")
    l1.append(head.data)
    head=head.next 
print("None")
l1.sort()
mergepoint=[]
for i in range (0,len(l1)):
    if i==len(l1)-1:
        mergepoint.append(l1[i])
    print(i,end="-->")
print("None")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
node7=Node(5)
node8=Node(15)
node9=Node(25)
node10=Node(45)
node11=Node(35)
node12=Node(None)

node7.next=node8
node8.next=node9
node9.next=node10
node10.next=node11
node11.next=node12

Head=node7
l2=[]
while Head.next!=None:
    print(Head.data,end="-->")
    l2.append(Head.data)
    Head=Head.next
print("None")

l2.sort()
for i in range (0,len(l2)):
    if i==0:
        mergepoint.append(l2[i])
print("None")

l3=l1+l2
for i in l3:
    print(i,end="-->")
print("None")
print(l3[5:7:1])
l3.sort()
for i in l3:
    print(i,end="-->")
print("None")
print(mergepoint)