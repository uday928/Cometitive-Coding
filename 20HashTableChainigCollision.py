def sum(nums,target):
  hashmap={}
  
  for i,num in enumerate(nums):
    complement=target-num
  
    if complement in hashmap:
      return [hashmap[complement],i]
    hashmap[num]=i
  return None
  
nums=[2,9,3,7]
target=12
result=sum(nums,target)

if result:
  print("sum of 2 index for",target,"are:",result)
else:
  print("No target matches.")