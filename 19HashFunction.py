class Hashing:
  def __init__(self):
    self.Dict={"Employee":{ }}
  def insert(self,name,ID,salary,profile):
    self.Dict["Employee"][name]={"ID":ID,"Salary":salary,"Profile":profile}
  def delete(self,name):
    self.Dict["Employee"].pop(name)
  def update(self,name,key,value):
    self.Dict["Employee"][name][key]=value
  def Show(self):
    for i in self.Dict["Employee"].items():
      print(i)
h=Hashing()
h.insert("raj","5674","100k","Developer")
h.insert("jay","7865","300k","peon")
h.insert("prakash","3452","150k","manager")
h.insert("ram","5436","350k","technician")
print("after insertion:")
h.Show()
h.update("ram","Salary","200k")
h.delete("jay")
print("after modificaton:")
h.Show()

print("----------------------------------------------------------------")

emp_detials={"Employee":{"raj":{"ID":"5674","Salary":"100k","Profile":"Developer"},"prakash":{"ID":"3452","Salary":"150k","Profile":"manager"},"ram":{"ID":"5436","Salary":"200k","Profile":"technician"}}}
import pandas as pd
df=pd.DataFrame(emp_detials["Employee"])
print("in table form:")
print(df)