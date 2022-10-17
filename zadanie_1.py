# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
# logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
# obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def is_passed(self):
        if sum(self.marks)/len(self.marks)>50:
            return True
        else:
            return False
    def __str__(self):
        return f'Student  {self.name}, with marks {self.marks}'


student1 = Student('Julia',[100,200,300])
student2 = Student('Jakub', [3,4,6])

print(student1.is_passed())
print(student2.is_passed())