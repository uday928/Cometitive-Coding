class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
node1=Node(5)
node2=Node(2)
node3=Node(3)
node4=Node(6)
node5=Node(7)
node6=Node(1)
node7=Node(None)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

head=node1
l1=[]

print("unsorted list 1")
while head.next!=None:
  print(head.data,end="-->")
  l1.append(head.data)
  head=head.next
print("None")

l1.sort()
print("sorted list 1")
for i in l1:
  print(i,end="-->")
print("None")

class Node1:
  def __init__(self,data):
    self.data=data
    self.next=None
node1=Node1(15)
node2=Node1(12)
node3=Node1(13)
node4=Node1(16)
node5=Node1(17)
node6=Node1(11)
node7=Node1(None)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

head=node1
l2=[]

print("unsorted list 2")
while head.next!=None:
  print(head.data,end="-->")
  l2.append(head.data)
  head=head.next
print("None")

l2.sort()

print("sorted list 2")
for i in l2:
  print(i,end="-->")
print("None")

l3=l1+l2
l3.sort()

print("sorted merged list:")
for i in l3:
  print(i,end="-->")
print("None")

print("sorted list's merge point")
print(l3[5:7:1])