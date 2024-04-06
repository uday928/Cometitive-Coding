class node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
    
def lb(root):#LEFT BOUNDARY
  if root:
    if root.left:
      print(root.data,end=" ")
      lb(root.left)

def rb(root):#RIGHT BOUNDARY
  if root:
    if root.right:
      print(root.data,end=" ")
      rb(root.right)
    
def leaf(root):#LEAF BOUNDARY
  if root:
    if root.left:
      leaf(root.left)
    if root.left is None and root.right is None:
      print(root.data,end=" ")
    leaf(root.right)
    
def pb(root):#PRINT BOUNDARY
  if root:
    print(root.data,end=" ")
    lb(root.left)
    leaf(root.left)
    leaf(root.right)
    rb(root.right)
    
root=node(1)
root.left=node(2)
root.left.left=node(3)
root.left.right=node(4)
root.right=node(5)
root.right.left=node(6)
root.right.right=node(7)


print("boundary order traversal is:",end=" ")  
pb(root)
    