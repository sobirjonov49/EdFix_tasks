class Person:
    def __init__(self, ism, familya, email, oylik):
        self.first_name = ism
        self.last_name = familya
        self.email = email
        self.solary = oylik
    def get_info(self):
        print(f"{self.first_name} {self.last_name} Email: {self.email}, solary: {self.solary}$")

person1=Person("Patten","Chapiro","pchapiro0@sun.com",1831.03)
person2=Person("Patsy","Lemmer","plemmer1@issuu.com",5429.65)
person3=Person("Carroll","Gooble","cgooble2@google.es",4866.85)
person4=Person("Urban","LLelweln","ullelweln3@prnewswire.com",3009.55)
person5=Person("Dolf","Gullan","dgullan4@cafepress.com",2492.22)

person1.get_info()
person2.get_info()
person3.get_info()
person4.get_info()
person5.get_info()