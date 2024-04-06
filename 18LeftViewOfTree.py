class node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def LB(root):
  if root:
    if root.left:
      print(root.data,end=" ")
      LB(root.left)
def Leave(root):
  if root:
    if root.left:
      Leave(root.left)
    if root.left is None and root.right is None:
      print(root.data,end=" ")
def PB(root):
  if root:
    print(root.data,end=" ")
    LB(root.left)
    Leave(root.left)
root=node(1)
root.left=node(2)
root.right=node(5)
root.left.left=node(3)
root.left.left=node(3)
root.left.right=node(4)
root.right.left=node(6)
root.right.right=node(7)
print(" left Boundary :",end=" ")
PB(root)
