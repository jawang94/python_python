# 1
class Node:
      def __init__(self, value):
    self.value = value
    self.next = None

class SList:
  def __init__(self,value):
    node = Node(value)
    self.head = node

  def addNode(self,value):
    node = Node(value)
    runner = self.head
    while runner.next != None:
      runner = runner.next
    runner.next = node

  def printAllValues(self):
    runner = self.head
    while runner.next != None:
      print(runner.value)
      runner = runner.next
    print(runner.value)

datlist = SList(0)
datlist.addNode(4)
datlist.addNode(123)
datlist.addNode(2103194183491)
datlist.printAllValues()

# 2
class Node:
      def __init__(self,value):
    self.value = value
    self.next = None

class SList:
  def __init__(self,value):
    node = Node(value)
    self.head = node

  def addNode(self,value):
    node = Node(value)
    runner = self.head
    while runner.next != None:
      runner = runner.next
    runner.next = node

  def removeNode(self, value):
    print("Removing", value, "from list")
    print("*"*50)
    print("New list:")

    # start with the head incase it is the one being removed
    temp = self.head 

    # if the matching node is the head, set new head to where old head was pointing
    if temp is not None:
        if temp.value == value: 
            self.head = temp.next
            temp = None
            return

    # searching for the matching node while keeping track of the previous node, so we can reassign it
    while temp is not None: 
        if temp.value == value: 
            break 
        prev = temp 
        temp = temp.next 

    # if no value match was found, end the method
    if(temp == None): 
        return 

    # unlinking the node to be deleted which is now contained in temp and linking the previous node with the next node. Essentially "drops" the matching node.
    prev.next = temp.next 

    # reset temp
    temp = None    
    

  def printAllValues(self):
    runner = self.head
    while runner.next != None:
      print(runner.value)
      runner = runner.next
    print(runner.value)

datlist = SList(0)
datlist.addNode(1)
datlist.addNode(2)
datlist.addNode(3)
datlist.addNode(4)
datlist.removeNode(3)
datlist.printAllValues()





