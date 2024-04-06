#10
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None  
def Inorder(root):
  #Left root right
  if root:
    Inorder(root.left)
    print(root.data,end="-->")
    Inorder(root.right)
def Preorder(root):
  #Root left Right
  if root:
    print(root.data,end="-->")
    Preorder(root.left)
    Preorder(root.right)
def Postorder(root):
  #left right root
  if root:
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end="-->")
Root=Node(6)
Root.left=Node(2)
Root.right=Node(3)
Root.left.left=Node(4)
Root.left.right=Node(9)
Root.right.left=Node(7)
print("Inorder:")
Inorder(Root)
print("None")
print("\n")
print("Preorder:")
Preorder(Root)
print("None")
print("\n")
print("Postorder:")
Postorder(Root)
print("None")
print("\n")