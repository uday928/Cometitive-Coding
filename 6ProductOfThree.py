# 6th 
# tuples are imutable / in this programme a list contains tuple with two arguments: Data, priority
# insert function to append maximum element we need 
# 1 means data, 2 priority (tuple index start from 1)
class PQueue:
  def __init__(self):
    self.array=[]
    
  def isEmpty(self):
    if len(self.array)==0:
      return True
    else:
      return False
      
  def enqueue(self,data,priority):
    self.index=0
    while self.index<len(self.array) and self.array[self.index][1]<=priority:
      #INDEX SHOULD BE LESS THAN LENGTH OF ARRAY 
      #INDEX'S FRIST ELEMENT
      self.index+=1 
    self.array.insert(self.index,(data,priority))
      
  def deQueue(self):
    if self.isEmpty():
      print("queue underflow")
    else:
      return self.array.pop(0)[0]
      
  def size(self):
    return len(self.array)
pq=PQueue()
pq.enqueue(10,5)
pq.enqueue(12,2)
pq.enqueue(13,1)
pq.enqueue(7,3)
pq.enqueue(54,4)
l=[]
while not pq.isEmpty():
  m=pq.deQueue()
  print(m)
  l.append(m)
  
p=1
for i in range(0,(len(l)-1)):
  if i<3:
    p=p*l[i]
    
print(p)
# print(pq.size())