class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None
    self.stack=[]

  def push(self, data) -> None:
    new_node=self.data
    if self.head != "None":
      new_node.next=self.head
      self.stack.append(new_node)
    else:
      new_node.next=None

  def pop(self) -> None:
    temp=0
    if self.head !="None":
      temp=self.head
      self.head=temp.next
      temp.pop()
   

  def status(self):
    """
    It prints all the elements of stack.
    """
    for i in self.stack[]:
      print(self.stack[i]"=>")

    
# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
