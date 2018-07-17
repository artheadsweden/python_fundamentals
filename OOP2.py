
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "The name is " + self.name + " and the age is " + str(self.age)

    def __del__(self):
        print(self.name, "is dead")

    def print_it(self):
        print("Hi", self.name)

class Employee(Person):
    def __init__(self, name, age, emp_no):
        super().__init__(name, age)
        self.emp_no = emp_no

    def __str__(self):
        return "Employee " + self.name + " has employee number " + self.emp_no

    def work(self):
        print(self.name, "is working")

def my_func():
    p = Person("John", 14)

def main():
    p1 = Person("Sue", 25)
    p2 = Person("Bob", 34)
    my_func()
    print(p1)
    print(p2)

    e1 = Employee("John", 44, "12344")
    print(e1)
    e1.work()
    e1.print_it()

    emp_list = []
    for i in range(100):
        e = Employee(str(i), i, str(i))
        emp_list.append(e)

    for emp in emp_list:
        print(emp)


if __name__ == '__main__':
    main()