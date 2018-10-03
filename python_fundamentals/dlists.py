class DNode:
    def __init__(self, val, nxt=None, prv=None):
        self.val = val  # value of node
        self.nxt = nxt  # next anchor of node
        self.prv = prv  # prev anchor of node


class DList:
    def __init__(self):
        self.head = None  # start of linked list
        self.tail = None  # end of linked list

    def appendNode(self, val):  # can only create first node, or append nodes (not insert)
        node = DNode(val)  # creating a new doubly linked node
        if self.head is None:  # if the list is empty, set the node to be both head & tail
            self.head = self.tail = node
        else:  # if not empty
            node.prv = self.tail  # prev anchor of new node attaches to tail
            node.nxt = None  # next anchor unattached because this node will inherit tail
            self.tail.nxt = node  # current tail's next anchor attaches to new node
            self.tail = node  # set tail to be the new node
        return self

    def removeNode(self, val):
        print("Removing", val,"...")
        runner = self.head  # generate a runner
        if runner == None:
            print("Linked List is empty. No node removed.")
            return self
        while runner != None:  # running through the linked list starting from the head
            if runner.val == val:  # if value of runner's current node is the node being removed, stop running
                break
            runner = runner.nxt  # otherwise keep running
        if runner.prv == None:  # edge case where node being removed is the head
            self.head = runner.nxt  # set head to the next node
        else:  # otherwise
            runner.prv.nxt = runner.nxt   # next anchor of the previous node attaches to runner's next node
        if runner.nxt == None:  # edge case where node being removed is the tail
            self.tail = runner.prv    # set new tail to be the prior node, thereby dropping the current tail
        else:  # otherwise
            runner.nxt.prv = runner.prv    # prev anchor of runner's next node attaches to runner's previous node
        return self

    def insertAfter(self,pos,newVal):
        print("Inserting",newVal,"after",pos,"...")
        newNode = DNode(newVal)  # generating new node
        runner = self.head  # generate runner on head
        while runner.val != None:  # running through the linked list
            if runner.val == pos:  # if position value found, stops running
                break
            runner = runner.nxt  # running forward
        if runner.nxt == None:  # for edge case where we are inserting after tail
            newNode.nxt = None  # set nxt anchor of newNode to None
            self.tail = newNode  # set newNode to be the new tail
        else:  # if position of insert is not after tail,
            newNode.nxt = runner.nxt  # set newNode's nxt anchor to whatever runner's nxt anchor is currently pointing to
            runner.nxt.prv = newNode  # set the prv anchor of runner's nxt node target to point at the newNode
        newNode.prv = runner  # set newNode's prev anchor to runner (carried by runner to position)
        runner.nxt = newNode  # finally, reset runner node's nxt anchor to point at newNode
        return self

    def insertBefore(self,pos,newVal):
        print("Inserting",newVal,"before",pos,"...")
        newNode = DNode(newVal)  # generating new node
        runner = self.tail  # generate runner on tail
        while runner != None:  # running through the linked list
            if runner.val == pos:  # if position value found, stops running
                break
            runner = runner.prv  # running backwards
        if runner == None:  # for edge case where we are inserting before head
            newNode.prv = None  # set prv anchor of newNode to None
            self.head = newNode  # set newNode to be the new tail
        else:  # if position of insert is not before head,
            newNode.prv = runner.prv  # set newNode's prv anchor to point at what runner's prv anchor is currently pointing to
            runner.prv.nxt = newNode  # set the nxt anchor of runner's prv node target to point at the newNode
        newNode.nxt = runner  # set newNode's nxt anchor to runner (carried by runner to position)
        runner.prv = newNode  # finally, reset runner node's prv anchor to point back at newNode
        return self

    def insertAtHead(self,newVal):
        print("Inserting",newVal,"at head ...")
        newNode = DNode(newVal)
        runner = self.head
        newNode.nxt = runner
        runner.prv = newNode
        self.head = newNode
        return self

    def insertAtTail(self,newVal):
        print("Inserting",newVal,"at tail ...")
        newNode = DNode(newVal)
        runner = self.tail
        newNode.prv = runner
        runner.nxt = newNode
        self.tail = newNode
        return self

    # basically running through the linked list starting from head
    def showListForward(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.nxt
        return self

    # basically running through the linked list starting from tail
    def showListBackward(self):
        runner = self.tail
        while runner != None:
            print(runner.val)
            runner = runner.prv
        return self


datlist = DList()
datlist.appendNode(0).appendNode(1).appendNode(2).appendNode(3).appendNode(4).appendNode(5)
datlist.showListForward()
datlist.removeNode(5)
datlist.showListBackward()
datlist.insertAfter(1,12)
datlist.showListForward()
datlist.insertBefore(1,10)
datlist.showListBackward()
datlist.insertAtHead(2301)
datlist.showListForward()
datlist.insertAtTail(101)
datlist.showListBackward()
# LET'S GO!!!

# datlist.removeNode(5).showListForward()