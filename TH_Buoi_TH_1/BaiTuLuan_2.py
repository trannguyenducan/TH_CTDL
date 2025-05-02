from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def getYob(self):
        return self._yob
    
    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob:int, grade:str):
        super().__init__(name=name, yob=yob)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - Yob: {self._yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob:int, subject:str):
        super().__init__(name=name, yob=yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - Yob: {self._yob} - Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob:int, specialist:str):
        super().__init__(name=name, yob=yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - Yob: {self._yob} - Specialist: {self._specialist}")

class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__listPeople = list()
    
    def addPerson(self, person:Person):
        self.__listPeople.append(person)
    
    def describe(self):
        print(f"Ward - Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def countDoctor(self):
        counter = 0
        for p in self.__listPeople:
            if  isinstance(p, Doctor):
                counter += 1
        return counter
    
    def sortAge(self):
        self.__listPeople.sort(key=lambda x: x.getYob(), reverse=True)

    def computeAverage(self):
        total = 0
        count = 0
        for p in self.__listPeople:
            if isinstance(p, Teacher):
                total += p.getYob()
                count += 1
        return total / count if count > 0 else 0

#Examples
# 2( a )
student1 = Student ( name =" studentA ", yob =2010 , grade =" 7 ")
student1.describe()
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher1.describe()
doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1.describe()
# 2( b )
print ()
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward(name =" Ward1 ")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()
# 2( c )
print ( f" \ nNumber of doctors : { ward1 . countDoctor () } ")
# 2( d )
print (" \ nAfter sorting Age of Ward1 people ")
ward1.sortAge ()
ward1.describe ()
# 2( e )
print ( f" \ nAverage year of birth ( teachers ) : { ward1.computeAverage () } ")