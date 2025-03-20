class List:
    def __init__(self, list1):
        self.list1=list1
    def append(self, num1):
        self.list1.append(num1)
        return self.list1

class MyList(List):
    def __init__(self, list1):
        super().__init__(list1)
    def append(self, num1):
        if num1 not in self.list1:
            self.list1.append(num1)
            return self.list1
        else:
            print("ElementDuplicationError")      

lst=List([1, 2, 3])
print(lst.append(3))

lst1=MyList([1, 2, 3])
print(lst1.append(3))

