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
        print("Removing", val)
        runner = self.head  # generate a runner
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
#LET'S GO!!!