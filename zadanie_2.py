#2. a Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich.

def print_names(names):
    for name in names:
        print(name)

print_names(['Julia','Magda','Ola','Asia','Paulina'])

# 2. b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży
# przez 2, a na końcu ją zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę składaną.

def multiply(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    return numbers

def multiplyD(numbers):
    numbers = [number*2 for number in numbers]
    return numbers


print(multiply([1, 2, 3, 4, 5]))
print(multiplyD([1, 2, 3, 4, 5]))

# c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range ),
# a następnie wyświetli jedynie parzyste elementy.


def parzyste(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i])


parzyste([10, 12, 14, 13, 11, 8, 7, 9, 0, 2])


# d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range ),
# a następnie wyświetli co drugi element.

def every_other_el(numbers):
    print(numbers[1::2])


every_other_el([10, 12, 14, 13, 11, 8, 7, 9, 0, 2])