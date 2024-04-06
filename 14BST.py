class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def insert(root,data):
  if not root:
    return Node(data)
  if data<root.data:
    root.left=insert(root.left,data)
  if data>root.data:
    root.right=insert(root.right,data)
  return root

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def Inorder(root):
  if root:
    Inorder(root.left)
    Inorder(root.right)
    
l=[15,12,1,9,7,3,4,18,16]
root=None
for i in l:
  root=insert(root,i)
inorder(root)
print("")
if l.sort()==Inorder(root):
  print("BST")