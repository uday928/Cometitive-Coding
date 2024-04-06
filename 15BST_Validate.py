class Node:
  def __init__(self,data):
    self.data=data
    self.right=None
    self.left=None
    
def isValid(root,left,right):
  if root is None:
    return 1 
  if left!=None and root.data<=left.data:
    return 0
  if right!=None and root.data>=right.data:
    return 0
  return isValid(root.left,left,root) and isValid(root.right,root,right)
    
root=Node(10)
root.left=Node(8)
root.right=Node(19)

if isValid(root,None,None):
  print("Valid BST")
else:
  print("Invalid BST")