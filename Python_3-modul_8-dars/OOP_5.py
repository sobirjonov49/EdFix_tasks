class List:
    def __init__(self, list1):
        self.list1=list1
    def remove(self, num1):
        self.list1.remove(num1)
        return self.list1

class MyList(List):
    def __init__(self, list1):
        super().__init__(list1)
    def remove(self, num1):
        self.list1=[i for i in self.list1 if i!=num1]
        return self.list1

lst = List([1,2,3,1,2,2,21,1,2,2,3,2,1])
print(lst.remove(2))

lst = MyList([1,2,3,1,2,2,21,1,2,2,3,2,1])
print(lst.remove(2))

            
