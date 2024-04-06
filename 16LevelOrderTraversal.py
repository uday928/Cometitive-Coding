class node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
    
def lorder(root):
  if root is None:
    return 0
  a=[]
  a.append(root)
    
  while len(a)>0:
    print(a[0].data,end=" ")
      
    node=a.pop(0)
    if node.left is not None:
      a.append(node.left)
    if node.right is not None:
      a.append(node.right)
      
root=node(1)
root.left=node(3)
root.right=node(4)
root.left.left=node(5)
root.left.right=node(6)
root.right.left=node(7)
root.right.right=node(8)
print("level order traversal of bst is:",end=" ")
lorder(root)
