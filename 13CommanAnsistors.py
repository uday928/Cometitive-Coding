#13th
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None  

def lca(root,a,b):
  if root is None:
    return 0
  if root.data==a or root.data==b:
    return root 
  else:
    Llca=lca(root.left,a,b)
    Rlca=lca(root.right,a,b)
    if Llca and Rlca:
      return root 
    return Llca if Llca else Rlca 
  
Root=Node(1)
Root.left=Node(2)
Root.right=Node(3)
Root.left.left=Node(4)
Root.left.right=Node(5)
Root.right.left=Node(6)
Root.right.right=Node(7)

print("Lowest common ansistor for 5 and 6 is",lca(Root,5,6).data)
print("Lowest common ansistor for 4 and 5 is",lca(Root,4,5).data)
print("Lowest common ansistor for 6 and 7 is",lca(Root,6,7).data)

