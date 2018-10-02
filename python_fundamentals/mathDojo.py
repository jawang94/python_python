class MathDojo:
    def __init__(self):
      self.value = 0

    def add(self,arg, *args):
      self.value += arg
      for i in range(0,len(args)):
        self.value += args[i]
      return self

    def subtract(self,arg, *args):
      self.value -= arg
      for i in range(0,len(args)):
        self.value -= args[i]
      return self

    def result(self):
      return self.value

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x) # should print 5

