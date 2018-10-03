class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node

        return self

    def removeNode(self, value):
        print("Removing", value, "from list")
        print("*"*50)
        print("New list:")
        runner = self.head
        if runner != None:
            if runner.value == value:
                self.head = runner.next
                runner = None
                return self

        while runner != None:
            if runner.value == value:
                break
            prev = runner
            runner = runner.next
        if(runner == None):
            return self

        prev.next = runner.next
        runner = None

        return self

    def toFront(self, value):
        node = Node(value)

        node.next = self.head

        self.head = node

        return self

    def insertNode(self, value, index):
        node = Node(value)
        runner = self.head
        if index == 0:
            node.next = self.head
            self.head = node
            return self
        count = 0
        while count < index-1:
            prev = runner
            runner = runner.next
            count += 1

        node.next = prev.next
        prev.next = node

        return self

    def printAllValues(self):
        runner = self.head
        while runner.next != None:
            print(runner.value)
            runner = runner.next
        print(runner.value)

        return self


datlist = SList(0)
datlist.addNode(1)
datlist.addNode(2)
datlist.addNode(3)
datlist.addNode(4)
datlist.removeNode(3)
datlist.insertNode(4444554, 2)
datlist.printAllValues()
