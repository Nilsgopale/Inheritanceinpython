class Person(object):


    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)




class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post


        Person.__init__(self, name, idnumber)




a = Person('Nilesh','0064')

a.display()
