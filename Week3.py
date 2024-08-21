from abc import ABC, abstractmethod
#1
class Manufacturer(ABC):
    def __init__(self,identity,location):
        self.identity = identity
        self.location = location
    @abstractmethod
    def describe():
        pass
class Device(Manufacturer):
    def __init__(self,name,price,identity,location):
        super().__init__(identity,location)
        self.name = name
        self.price = price
    def describe(self):
        print(f"Name: {self.name} - Price: {self.price}")
        print(f"Identity: {self.identity} - Location: {self.location}")


device1 = Device ( name =" mouse ", price =2.5 , identity =9725 , location =" Vietnam ")
device1 . describe ()
device2 = Device ( name =" monitor ", price =12.5 , identity =11 , location =" Germany ")
device2 . describe ()
#2
class Person:
    def __init__(self,name,yob):
        self.name = name
        self.yob = yob
    def addPerson(self,job,name,yob,describe):
        if job == "Student":
            list.append(Student(name,yob,describe))
        elif job == "Teacher":
            list.append(Teacher(name,yob,describe))
        elif job == "Doctor":
            list.append(Doctor(name,yob,describe))
        else:
            print("Title Error")
class Student(Person):
    def __init__(self,name,yob,grade):
        super().__init__(name,yob)
        self.grade = grade
    def describe(self):
        print(f"Student - Name : {self.name} - YoB : {self.yob} - Grade : {self.grade}")
class Teacher(Person):
    def __init__(self,name,yob,subject):
        super().__init__(name,yob)
        self.subject = subject
    def describe(self):
        print(f"Teacher - Name : {self.name} - YoB : {self.yob} - Subject : {self.subject}")
class Doctor(Person):
    def __init__(self,name,yob,specialist):
        super().__init__(name,yob)
        self.specialist = specialist
    def describe(self):
        print(f"Doctor - Name : {self.name} - YoB : {self.yob} - Specialist : {self.specialist}")
class Ward:
    list_person = [
        Student("A", 2010, "7"),
        Teacher("B", 1976, "Math"),
        Doctor("C", 1963, "Endocrinologists")
    ]
    def __init__(self,name):
        self.name_ward = name
    def addPerson(self,obj):
        self.list_person.append(obj)
    def describe(self):
        print(f"Ward Name: {self.name_ward}")
        for i in self.list_person:
            if str(i.__class__) == "<class '__main__.Student'>":
                print(f"Student - Name: {i.name} - YoB: {i.yob} - Grade: {i.grade}")
            elif str(i.__class__) == "<class '__main__.Teacher'>":
                print(f"Teacher - Name: {i.name} - YoB: {i.yob} - Subject: {i.subject}")
            elif str(i.__class__) == "<class '__main__.Doctor'>":
                print(f"Doctor - Name: {i.name} - YoB: {i.yob} - Specialist: {i.specialist}")
            else:
                print("Not Found")
    def countDoctor(self):
        cnt =0
        for i in self.list_person:
            if str(i.__class__) == "<class '__main__.Doctor'>":
                cnt +=1
        return cnt
    def sortAge(self):
        self.list_person.sort(key=lambda obj: obj.yob,reverse=True)
    def aveTeacherYearOfBirth(self):
        cnt = 0
        total = 0
        for i in self.list_person:
            if str(i.__class__) == "<class '__main__.Teacher'>":
                cnt +=1
                total += i.yob
        return int(total/cnt)
#a
student1 = Student( name =" studentA ", yob =2010 , grade="7")
student1.describe ()
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher1 . describe ()
doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1 . describe ()
#b
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward ( name =" Ward1 ")
ward1 . addPerson ( student1 )
ward1 . addPerson ( teacher1 )
ward1 . addPerson ( teacher2 )
ward1 . addPerson ( doctor1 )
ward1 . addPerson ( doctor2 )
ward1 . describe ()
#c
print ( f"\nNumber of doctors : { ward1 . countDoctor ()}")
print ("\nAfter sorting Age of Ward1 people ")
ward1 . sortAge ()
ward1 . describe ()
#d
print ( f"\nAverage year of birth ( teachers ): { ward1 . aveTeacherYearOfBirth ()}")
#3
class MyStack:
    list = []
    def __init__(self,capacity):
        self.capacity = capacity
    def isEmpty(self):
        return len(self.list)==0
    def isFull(self):
        return len(self.list)==self.capacity
    def pop(self):
        return self.list.pop()
    def push(self,value):
        return self.list.append(value)
    def top(self):
        return self.list[-1]

stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())
#4
class MyQueue:
    list = []
    def __init__(self,capacity):
        self.capacity = capacity
    def isEmpty(self):
        return len(self.list)==0
    def isFull(self):
        return len(self.list)==self.capacity
    def dequeue(self):
        return self.list.pop(0)
    def enqueue(self,value):
        return self.list.append(value)
    def front(self):
        return self.list[0]

queue1 = MyQueue ( capacity =5)
queue1 . enqueue (1)
queue1 . enqueue (2)
print ( queue1 . isFull () )
print ( queue1 . front () )
print ( queue1 . dequeue () )
print ( queue1 . front () )
print ( queue1 . dequeue () )
print ( queue1 . isEmpty () )

