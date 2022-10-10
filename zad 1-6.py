# 1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
# wyświetlić ( print )

def przywitanie(name:str, surname:str):
    return f" Cześć {name} {surname}!"

czesc = przywitanie('Julia','Duch')
print(czesc)

# 2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
# mnożenia obu liczb.

def mnozenie(l:int, n:int):
    return l*n

print(mnozenie(4,6))

# 3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"


def parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

wynik = parzysta(5)

print("Liczba parzysta") if wynik == True else print("Liczba nieparzysta")

# 4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
# pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool

def suma(l1:int,l2:int,l3:int):
    if l1+l2>=l3:
        return True
    else:
        return False

print(suma(6,7,8))

# 5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
# . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
# pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.

def zawiera(lista:list,element:int):
    if lista.__contains__(element):
        return True
    else:
        return False

print(zawiera([1,2,3,4,5],9))

# 6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.

def operacje(lista1:list, lista2:list):
    nowa_lista = lista1+lista2
    nowa_lista = list(dict.fromkeys(nowa_lista))
    nowa_lista = [el**3 for el in nowa_lista]
    return nowa_lista

print(operacje([1,2,3,4,5],[0,9,8,2,2,3]))

