class DNode:
    def __init__(self, val, nxt=None, prv=None):
        self.val = val
        self.nxt = nxt
        self.prv = prv

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,val):
        node = DNode(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prv = self.tail
            node.nxt = None
            self.tail.nxt = node
            self.tail = node
        return self

    def removeNode(self,val):
      print("Removing", val)
      runner = self.head
      while runner != None:
        if runner.val == val:
          break
        runner = runner.nxt
      if runner.prv == None:
        self.head = runner.nxt
      else:
        runner.prv.nxt = runner.nxt
      if runner.nxt == None:
        self.tail = runner.prv
      else:
        runner.nxt.prv = runner.prv      
      return self
      

    def showListForward(self):
      runner = self.head
      while runner != None:
        print(runner.val)
        runner = runner.nxt
      return self

    def showListBackward(self):
      runner = self.tail
      while runner != None:
        print(runner.val)
        runner = runner.prv
      return self

    
datlist = DList()
datlist.addNode(0).addNode(1).addNode(2).addNode(3).addNode(4).addNode(5)
datlist.showListForward()
datlist.removeNode(2)
datlist.showListBackward()

